import json
import queue
import threading
import time
import unittest
from unittest import mock

import coinbase.deribit.ws_client as wsmod
from coinbase.deribit.errors import DeribitConnectionError

from ..constants import TEST_API_KEY, TEST_API_SECRET


class FakeWS:
    """In-process stand-in for a websockets sync connection."""

    def __init__(self, auth_error=None, closes_on_logout=True):
        self.q = queue.Queue()
        self.sent = []
        self._closed = threading.Event()
        self.auth_error = auth_error
        self.closes_on_logout = closes_on_logout

    def send(self, data):
        obj = json.loads(data)
        self.sent.append(obj)
        rid, method = obj.get("id"), obj["method"]
        if method == "public/auth" and self.auth_error:
            self.q.put(
                json.dumps({"jsonrpc": "2.0", "id": rid, "error": self.auth_error})
            )
        elif method == "public/auth":
            self._reply(rid, {"access_token": "TOK", "expires_in": 900})
        elif method == "private/subscribe":
            # Like production: the trading host only subscribes user.* channels.
            chans = obj["params"]["channels"]
            self._reply(rid, [c for c in chans if c.startswith("user.")])
        elif method == "public/subscribe":
            # Like production: the streams host only subscribes market data.
            chans = obj["params"]["channels"]
            self._reply(rid, [c for c in chans if not c.startswith("user.")])
        elif method == "private/buy":
            self._reply(rid, {"order": {"order_id": "E1"}})
        elif method in ("public/test", "never_answers"):
            pass
        elif method == "private/logout":
            if self.closes_on_logout:
                self._closed.set()  # gateway closes the socket with no reply
        else:
            self._reply(rid, {})

    def _reply(self, rid, result):
        self.q.put(json.dumps({"jsonrpc": "2.0", "id": rid, "result": result}))

    def push(self, obj):
        self.q.put(json.dumps(obj))

    def recv(self, timeout=None):
        try:
            return self.q.get(timeout=timeout)
        except queue.Empty:
            raise TimeoutError()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                return self.q.get(timeout=0.05)
            except queue.Empty:
                if self._closed.is_set():
                    raise OSError("closed")

    def close(self):
        self._closed.set()

    @property
    def closed(self):
        return self._closed.is_set()


def wait_for(predicate, timeout=3.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if predicate():
            return True
        time.sleep(0.02)
    return predicate()


class DeribitWSClientTest(unittest.TestCase):
    def _client(self, fake):
        self._patch = mock.patch.object(wsmod, "ws_connect", return_value=fake)
        self._patch.start()
        self.addCleanup(self._patch.stop)
        c = wsmod.DeribitRetailWSClient(TEST_API_KEY, TEST_API_SECRET)
        c.open()
        self.addCleanup(c.close)
        return c

    def test_authenticated_production_client_uses_trading_host(self):
        client = wsmod.DeribitRetailWSClient(TEST_API_KEY, TEST_API_SECRET)
        self.assertEqual(client.url, "wss://drb.coinbase.com/ws/api/v2")

    def test_unauthenticated_production_client_uses_streams_host(self):
        client = wsmod.DeribitRetailWSClient(api_key=None, api_secret=None)
        self.assertEqual(client.url, "wss://streams.drb.coinbase.com/ws/api/v2")

    def test_authenticates_on_open(self):
        fake = FakeWS()
        self._client(fake)
        self.assertEqual(fake.sent[0]["method"], "public/auth")
        self.assertEqual(fake.sent[0]["params"]["grant_type"], "coinbase_cdp")

    def test_typed_call_over_socket(self):
        fake = FakeWS()
        c = self._client(fake)
        buy = c.private_buy(instrument_name="ETH-PERPETUAL", amount=1, type="market")
        self.assertEqual(buy.result.order.order_id, "E1")

    def test_subscription_dispatch(self):
        fake = FakeWS()
        c = self._client(fake)
        received = []
        c.subscribe(
            ["user.orders.BTC-PERPETUAL.raw"],
            lambda data, ch: received.append((ch, data)),
        )
        fake.push(
            {
                "jsonrpc": "2.0",
                "method": "subscription",
                "params": {
                    "channel": "user.orders.BTC-PERPETUAL.raw",
                    "data": {"mark_price": 42000},
                },
            }
        )
        deadline = time.monotonic() + 2
        while not received and time.monotonic() < deadline:
            time.sleep(0.02)
        self.assertEqual(received[0][0], "user.orders.BTC-PERPETUAL.raw")
        self.assertEqual(received[0][1]["mark_price"], 42000)

    def test_heartbeat_test_request_is_answered(self):
        fake = FakeWS()
        c = self._client(fake)
        fake.push(
            {
                "jsonrpc": "2.0",
                "method": "heartbeat",
                "params": {"type": "test_request"},
            }
        )
        deadline = time.monotonic() + 2
        while time.monotonic() < deadline:
            if any(s["method"] == "public/test" for s in fake.sent):
                break
            time.sleep(0.02)
        self.assertTrue(any(s["method"] == "public/test" for s in fake.sent))

    def test_inflight_call_fails_loud_on_disconnect(self):
        fake = FakeWS()
        c = self._client(fake)
        c._reconnect = lambda: False  # don't loop reconnecting in the test
        result = {}

        def do_call():
            try:
                c.call("never_answers", {}, timeout=5)
            except Exception as e:
                result["err"] = type(e).__name__

        t = threading.Thread(target=do_call)
        t.start()
        time.sleep(0.2)
        fake.close()  # simulate disconnect while the call is in flight
        t.join(timeout=3)
        self.assertEqual(result.get("err"), "DeribitConnectionError")

    def test_logout_returns_ok_and_does_not_reconnect(self):
        fake = FakeWS()
        c = self._client(fake)
        reconnected = []
        c._reconnect = lambda: reconnected.append(True) or True

        result = c.private_logout()

        self.assertEqual(result, {"result": "ok"})
        self.assertTrue(any(s["method"] == "private/logout" for s in fake.sent))
        # The 1000 close is the expected end of the session, not a drop.
        self.assertFalse(reconnected)
        self.assertFalse(c._running)

    def _client_seq(self, fakes):
        """Client whose successive ws_connect calls return the given fakes."""
        self._patch = mock.patch.object(wsmod, "ws_connect", side_effect=list(fakes))
        self._patch.start()
        self.addCleanup(self._patch.stop)
        for name, value in (
            ("DERIBIT_WS_RETRY_BASE", 0.01),
            ("DERIBIT_WS_RETRY_CAP", 0.01),
        ):
            p = mock.patch.object(wsmod, name, value)
            p.start()
            self.addCleanup(p.stop)
        c = wsmod.DeribitRetailWSClient(TEST_API_KEY, TEST_API_SECRET)
        self.addCleanup(c.close)
        return c

    def test_reconnect_restores_subscriptions(self):
        first, second = FakeWS(), FakeWS()
        c = self._client_seq([first, second]).open()
        got = []
        c.subscribe(["user.orders.BTC-PERPETUAL.raw"], lambda d, ch: got.append(d))

        first.close()  # unexpected drop

        self.assertTrue(
            wait_for(
                lambda: any(s["method"] == "private/subscribe" for s in second.sent)
            ),
            "subscription was not restored on the new socket",
        )
        self.assertEqual(
            [s["method"] for s in second.sent], ["public/auth", "private/subscribe"]
        )
        second.push(
            {
                "jsonrpc": "2.0",
                "method": "subscription",
                "params": {"channel": "user.orders.BTC-PERPETUAL.raw", "data": 42},
            }
        )
        self.assertTrue(wait_for(lambda: got == [42]))
        self.assertTrue(c._running)
        # RPCs work on the new socket afterwards.
        self.assertIn("order", c.call("private/buy", {})["result"])

    def test_call_registered_before_disconnect_is_never_sent_later(self):
        old, new = FakeWS(), FakeWS()
        c = self._client_seq([old]).open()
        self.addCleanup(old.close)  # the test swaps it out; let the reader exit
        real_send = c._send

        def disconnect_then_send(obj, gen=None):
            # A disconnect + reconnect lands between registering and sending.
            c._fail_pending(wsmod.DeribitConnectionError("websocket disconnected"))
            with c._send_lock:
                c._ws = new
            return real_send(obj, gen=gen)

        c._send = disconnect_then_send
        with self.assertRaises(wsmod.DeribitConnectionError) as ctx:
            c.call("private/buy", {"instrument_name": "BTC-PERPETUAL"})
        self.assertIn("not sent", str(ctx.exception))
        self.assertEqual(new.sent, [])
        self.assertFalse(any(s["method"] == "private/buy" for s in old.sent))

    def test_bad_frames_do_not_kill_the_reader(self):
        fake = FakeWS()
        c = self._client(fake)
        fake.q.put("not json")
        fake.q.put(json.dumps(["batch", 1]))
        fake.q.put(json.dumps({"id": "no-such-call", "result": 1}))
        self.assertIn("order", c.call("private/buy", {}, timeout=2)["result"])
        self.assertTrue(c._reader.is_alive())

    def test_failed_open_cleans_up_and_can_retry(self):
        bad = FakeWS(auth_error={"code": 13004, "message": "invalid_credentials"})
        good = FakeWS()
        c = self._client_seq([bad, good])
        with self.assertRaises(wsmod.DeribitAuthError):
            c.open()
        self.assertTrue(bad.closed)
        self.assertFalse(c._running)
        self.assertIsNone(c._ws)
        c.open()
        self.assertTrue(c._running)
        self.assertIn("order", c.call("private/buy", {})["result"])

    def test_auth_error_redacts_echoed_jwt(self):
        jwt = "eyJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJvcmdhbml6YXRpb25zIn0.c2lnbmF0dXJlLXNpZw"
        bad = FakeWS(auth_error={"code": 13004, "message": f"bad token {jwt}"})
        c = self._client_seq([bad])
        with self.assertRaises(wsmod.DeribitAuthError) as ctx:
            c.open()
        self.assertNotIn(jwt, str(ctx.exception))
        self.assertIn("<redacted>", str(ctx.exception))

    def test_call_from_subscription_callback_raises_immediately(self):
        fake = FakeWS()
        c = self._client(fake)
        errors = []

        def cb(data, channel):
            started = time.monotonic()
            try:
                c.call("private/buy", {})
            except RuntimeError as e:
                errors.append((str(e), time.monotonic() - started))

        c.subscribe(["user.orders.BTC-PERPETUAL.raw"], cb)
        fake.push(
            {
                "jsonrpc": "2.0",
                "method": "subscription",
                "params": {"channel": "user.orders.BTC-PERPETUAL.raw", "data": 1},
            }
        )
        self.assertTrue(wait_for(lambda: errors))
        self.assertIn("reader thread", errors[0][0])
        self.assertLess(errors[0][1], 1)

    def test_call_timeout_raises_builtin_timeout_error(self):
        c = self._client(FakeWS())
        with self.assertRaises(TimeoutError):
            c.call("never_answers", {}, timeout=0.1)
        self.assertEqual(c._pending, {})

    def test_logout_closes_socket_when_gateway_does_not(self):
        fake = FakeWS(closes_on_logout=False)
        c = self._client(fake)
        c._logout_close_wait = 0.1
        self.assertEqual(c.private_logout(), {"result": "ok"})
        self.assertTrue(fake.closed)
        self.assertIsNone(c._ws)
        self.assertTrue(wait_for(lambda: not c._reader.is_alive()))

    def test_logout_raises_when_not_sent(self):
        c = self._client(FakeWS())
        c.close()
        with self.assertRaises(wsmod.DeribitConnectionError):
            c.private_logout()

    def test_stale_reauth_failure_does_not_close_new_socket(self):
        old, new = FakeWS(), FakeWS()
        c = self._client_seq([old]).open()
        self.addCleanup(old.close)  # the test swaps it out; let the reader exit

        def failing_call(method, params=None, timeout=None):
            with c._send_lock:
                c._ws = new  # a reconnect happened while re-auth was in flight
            raise wsmod.DeribitConnectionError("websocket disconnected")

        c.call = failing_call
        c._reauth()
        self.assertFalse(new.closed)

    def test_failed_reauth_drops_current_socket(self):
        fake = FakeWS()
        c = self._client(fake)
        c._reconnect = lambda: False
        c.call = mock.Mock(side_effect=wsmod.DeribitConnectionError("boom"))
        c._reauth()
        self.assertTrue(fake.closed)

    def test_authenticated_client_uses_private_subscribe(self):
        fake = FakeWS()
        c = self._client(fake)
        out = c.subscribe(["user.changes.BTC-PERPETUAL.raw"])
        self.assertEqual(list(out), ["private"])
        self.assertEqual(fake.sent[-1]["method"], "private/subscribe")
        c.unsubscribe(["user.changes.BTC-PERPETUAL.raw"])
        self.assertEqual(fake.sent[-1]["method"], "private/unsubscribe")

    def test_dropped_channels_raise_and_are_forgotten(self):
        fake = FakeWS()
        c = self._client(fake)
        with self.assertRaises(wsmod.DeribitSubscriptionError) as ctx:
            c.subscribe(
                ["user.orders.any.any.raw", "ticker.BTC-PERPETUAL.100ms"],
                lambda d, ch: None,
            )
        err = ctx.exception
        self.assertEqual(err.rejected, ["ticker.BTC-PERPETUAL.100ms"])
        self.assertEqual(err.accepted, ["user.orders.any.any.raw"])
        self.assertIn("unauthenticated", str(err))
        self.assertEqual(list(c._subscriptions), ["user.orders.any.any.raw"])

    def test_unauthenticated_client_uses_public_subscribe(self):
        fake = FakeWS()
        self._patch = mock.patch.object(wsmod, "ws_connect", return_value=fake)
        self._patch.start()
        self.addCleanup(self._patch.stop)
        c = wsmod.DeribitRetailWSClient(api_key=None, api_secret=None).open()
        self.addCleanup(c.close)
        out = c.subscribe(["ticker.BTC-PERPETUAL.100ms"])
        self.assertEqual(list(out), ["public"])
        self.assertEqual(fake.sent[-1]["method"], "public/subscribe")
        with self.assertRaises(wsmod.DeribitSubscriptionError) as ctx:
            c.subscribe(["user.orders.any.any.raw"])
        self.assertIn("API keys", str(ctx.exception))
        c.unsubscribe(["ticker.BTC-PERPETUAL.100ms"])
        self.assertEqual(fake.sent[-1]["method"], "public/unsubscribe")

    def test_reconnect_drops_and_warns_on_unrestored_channel(self):
        first, second = FakeWS(), FakeWS()
        c = self._client_seq([first, second]).open()
        c.subscribe(["user.orders.any.any.raw"])
        with c._sub_lock:  # simulate a channel the gateway now refuses
            c._subscriptions["ticker.BTC-PERPETUAL.100ms"] = []
        with self.assertLogs("coinbase.deribit.WSClient", level="WARNING") as logs:
            first.close()
            self.assertTrue(
                wait_for(
                    lambda: any(s["method"] == "private/subscribe" for s in second.sent)
                )
            )
            wait_for(lambda: "ticker.BTC-PERPETUAL.100ms" not in c._subscriptions)
        self.assertTrue(any("did not restore" in line for line in logs.output))
        self.assertEqual(list(c._subscriptions), ["user.orders.any.any.raw"])
        self.assertTrue(c._running)

    def test_unsubscribe_all_clears_registry_and_uses_client_scope(self):
        fake = FakeWS()
        c = self._client(fake)
        c.subscribe(["user.orders.any.any.raw"], lambda d, ch: None)
        out = c.unsubscribe_all()
        self.assertEqual(list(out), ["private"])
        self.assertEqual(fake.sent[-1]["method"], "private/unsubscribe_all")
        self.assertEqual(c._subscriptions, {})

    def test_failed_unsubscribe_keeps_callbacks(self):
        fake = FakeWS()
        c = self._client(fake)
        c.subscribe(["user.orders.any.any.raw"], lambda d, ch: None)
        c.call = mock.Mock(side_effect=wsmod.DeribitConnectionError("down"))
        with self.assertRaises(wsmod.DeribitConnectionError):
            c.unsubscribe(["user.orders.any.any.raw"])
        with self.assertRaises(wsmod.DeribitConnectionError):
            c.unsubscribe_all()
        self.assertIn("user.orders.any.any.raw", c._subscriptions)


if __name__ == "__main__":
    unittest.main()
