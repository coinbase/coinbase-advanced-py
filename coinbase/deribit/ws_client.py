import concurrent.futures
import itertools
import json
import logging
import os
import threading
import time
from concurrent.futures import Future
from typing import Any, Callable, List, Optional, Type

from websockets.exceptions import ConnectionClosed
from websockets.sync.client import connect as ws_connect

from coinbase.api_base import APIBase, get_logger
from coinbase.constants import API_ENV_KEY, API_SECRET_ENV_KEY
from coinbase.deribit._generated.rest_methods import (
    GeneratedRESTMixin,
    GeneratedWSMixin,
)
from coinbase.deribit._model import DeribitModel
from coinbase.deribit.auth.token_cache import build_auth_params
from coinbase.deribit.constants import (
    DERIBIT_AUTH_METHOD,
    DERIBIT_TOKEN_REFRESH_RATIO,
    DERIBIT_WS_CALL_TIMEOUT,
    DERIBIT_WS_OPEN_TIMEOUT,
    DERIBIT_WS_RETRY_BASE,
    DERIBIT_WS_RETRY_CAP,
    DERIBIT_WS_RETRY_FACTOR,
    DERIBIT_WS_RETRY_MAX,
    GRANT_TYPE_CDP,
    select_environment,
)
from coinbase.deribit.errors import (
    DeribitAuthError,
    DeribitConnectionError,
    DeribitRPCError,
    DeribitSubscriptionError,
    redact_secrets,
    rpc_error_from,
)

logger = get_logger("coinbase.deribit.WSClient")


class DeribitRetailWSClient(APIBase, GeneratedRESTMixin, GeneratedWSMixin):
    """Synchronous, thread-backed WebSocket client for the Deribit Retail gateway.

    This is the primary transport. Every Deribit RPC method is available as a typed
    method (mixed in from the generated layer) and runs over the socket; subscription
    channels deliver to per-channel callbacks.

    Concurrency model: a single background reader thread reads frames and
    demuxes them by JSON-RPC ``id`` onto the matching :class:`Future`; :meth:`call`
    blocks on that future. Notifications (no ``id``) go to the subscription dispatcher,
    which also answers heartbeat ``test_request`` messages.

    Write safety: an in-flight call is never auto-resent across a reconnect. On
    disconnect every pending future fails with :class:`DeribitConnectionError` and the
    caller decides whether to retry (reconcile by ``label`` first). Each connection
    has a generation number, so a call registered before a disconnect is never sent
    on the replacement socket.

    Subscription callbacks run on the reader thread. They must not call :meth:`call`
    or any RPC method (the reply could never be read); hand that work to another
    thread. Doing so raises ``RuntimeError`` immediately.
    """

    def __init__(
        self,
        api_key: Optional[str] = os.getenv(API_ENV_KEY),
        api_secret: Optional[str] = os.getenv(API_SECRET_ENV_KEY),
        key_file: Optional[Any] = None,
        environment: str = "production",
        url: Optional[str] = None,
        timeout: Optional[int] = DERIBIT_WS_CALL_TIMEOUT,
        verbose: bool = False,
    ) -> None:
        # environment picks the gateway; an explicit url overrides it.
        environment_config = None
        if url is None:
            environment_config = select_environment(environment)
            url = environment_config["ws_url"]
        super().__init__(
            api_key=api_key,
            api_secret=api_secret,
            key_file=key_file,
            base_url=url,
            timeout=timeout,
            verbose=verbose,
        )
        if verbose:
            logger.setLevel(logging.DEBUG)

        # Public, unauthenticated market-data sessions use the dedicated streams
        # host. Authenticated RPC and user-channel sessions use the trading host.
        if environment_config is not None and not self.is_authenticated:
            url = environment_config["stream_ws_url"]
        self.url = url
        self._call_timeout = timeout or DERIBIT_WS_CALL_TIMEOUT

        self._ws = None
        self._reader: Optional[threading.Thread] = None
        self._running = False

        self._ids = itertools.count(1)
        self._id_lock = threading.Lock()
        self._send_lock = threading.Lock()
        self._pending = {}  # id -> Future
        self._pending_lock = threading.Lock()
        # Bumped (under _send_lock + _pending_lock) whenever pending calls are
        # failed, so a call registered on an old connection can't be sent later.
        self._gen = 0
        self._lifecycle_lock = threading.RLock()

        # channel -> list[callback(data, channel)]
        self._subscriptions = {}
        self._sub_lock = threading.Lock()

        self._reauth_timer: Optional[threading.Timer] = None
        # Seconds private_logout waits for the gateway to close before closing
        # locally.
        self._logout_close_wait = 5.0

    def open(self) -> "DeribitRetailWSClient":
        """Connect, authenticate (if keys were provided), and start the reader.

        If connecting or authenticating fails, the socket is closed and the error
        propagates; calling ``open()`` again retries from scratch.
        """
        with self._lifecycle_lock:
            if self._running:
                return self
            self._connect_and_auth()
            self._running = True
            self._reader = threading.Thread(
                target=self._run, name="deribit-ws-reader", daemon=True
            )
            self._reader.start()
            return self

    def close(self) -> None:
        """Stop the reader, close the socket, and fail any pending calls."""
        with self._lifecycle_lock:
            self._running = False
            self._cancel_reauth()
            self._close_ws(self._ws)
            self._fail_pending(DeribitConnectionError("client closed"))
            reader = self._reader
        self._join_reader(reader)

    def __enter__(self):
        return self.open()

    def __exit__(self, *exc):
        self.close()

    def private_logout(self, invalidate_token=None):
        """Log out and tear down the session.

        The gateway forwards the logout to Deribit and closes the socket (1000
        "logout") with no JSON-RPC reply, so this can't go through :meth:`call`
        (which would block for a reply that never arrives and then surface the
        close as a :class:`DeribitConnectionError`). We stop the reader from
        reconnecting, send the frame fire-and-forget so the backend still tears
        down COD-safely, wait briefly for the server to close, then close the
        socket locally either way.

        Raises :class:`DeribitConnectionError` if the logout frame could not be
        sent (the local session is still torn down).
        """
        with self._lifecycle_lock:
            self._running = False
            self._cancel_reauth()
            reader = self._reader
        params = {
            k: v
            for k, v in {"invalidate_token": invalidate_token}.items()
            if v is not None
        }
        send_error = None
        try:
            self._send(
                {
                    "jsonrpc": "2.0",
                    "id": self._next_id(),
                    "method": "private/logout",
                    "params": params,
                }
            )
        except Exception as e:
            send_error = e
        finally:
            # Give the gateway a moment to close (1000 "logout"), then make sure
            # the socket and reader are gone even if it never does.
            self._join_reader(reader, self._logout_close_wait)
            self._close_ws(self._ws)
            self._join_reader(reader)
            self._fail_pending(DeribitConnectionError("client logged out"))
        if send_error is not None:
            raise DeribitConnectionError(
                f"logout was not sent: {send_error}"
            ) from send_error
        return {"result": "ok"}

    def call(
        self, method: str, params: Optional[dict] = None, timeout: Optional[int] = None
    ) -> dict:
        """Send one JSON-RPC call and block for the reply.

        Returns the full response envelope dict (``id``/``jsonrpc``/``result``).
        Raises a :class:`DeribitRPCError` subclass on a JSON-RPC error,
        :class:`DeribitConnectionError` if the request was not sent or the socket
        drops while waiting, and ``TimeoutError`` if no reply arrives in
        ``timeout`` seconds. Must not be called from a subscription callback.
        """
        if threading.current_thread() is self._reader:
            raise RuntimeError(
                f"{method} called on the WebSocket reader thread (e.g. from a "
                "subscription callback). Its reply could never be read; run the "
                "call from another thread."
            )
        rid = self._next_id()
        fut: Future = Future()
        with self._pending_lock:
            gen = self._gen
            self._pending[rid] = fut
        frame = {
            "jsonrpc": "2.0",
            "id": rid,
            "method": method,
            "params": {k: v for k, v in (params or {}).items() if v is not None},
        }
        try:
            self._send(frame, gen=gen)
        except Exception as e:
            with self._pending_lock:
                self._pending.pop(rid, None)
            raise DeribitConnectionError(f"{method} was not sent: {e}") from e

        wait = timeout if timeout is not None else self._call_timeout
        try:
            return fut.result(wait)
        except concurrent.futures.TimeoutError:
            # Before Python 3.11 this is not the builtin TimeoutError.
            with self._pending_lock:
                self._pending.pop(rid, None)
            raise TimeoutError(f"no reply to {method} within {wait}s") from None

    def _rpc(
        self,
        method: str,
        params: dict,
        model_cls: Optional[Type[DeribitModel]] = None,
    ):
        """Bridge for the generated typed methods. :meta private:"""
        payload = self.call(method, params)
        if model_cls is not None:
            return model_cls(payload)
        return payload

    def _next_id(self) -> int:
        with self._id_lock:
            return next(self._ids)

    def _send(self, obj: dict, gen: Optional[int] = None) -> None:
        data = json.dumps(obj)
        with self._send_lock:
            if gen is not None and gen != self._gen:
                raise DeribitConnectionError(
                    "connection was reset before the request was sent"
                )
            if self._ws is None:
                raise DeribitConnectionError("websocket is not connected")
            self._ws.send(data)

    @property
    def _sub_scope(self) -> str:
        # The trading host (authenticated) only allows private/(un)subscribe and
        # serves user.* channels; the streams host (unauthenticated) only allows
        # public/(un)subscribe and serves market data.
        return "private" if self.is_authenticated else "public"

    def subscribe(
        self,
        channels: List[str],
        callback: Optional[Callable[[Any, str], None]] = None,
    ) -> dict:
        """Subscribe to channels and (optionally) register a callback for them.

        ``callback(data, channel)`` runs on the reader thread for each notification.
        Channels are remembered and re-subscribed automatically after a reconnect.

        An authenticated client serves ``user.*`` channels; market-data channels
        (ticker, book, trades, ...) need an unauthenticated client, which connects
        to the streams host. Raises :class:`DeribitSubscriptionError` listing any
        channel the gateway did not subscribe; the others stay subscribed.
        """
        with self._sub_lock:
            for ch in channels:
                self._subscriptions.setdefault(ch, [])
                if callback is not None:
                    self._subscriptions[ch].append(callback)
        scope = self._sub_scope
        try:
            response = self.call(f"{scope}/subscribe", {"channels": list(channels)})
        except Exception:
            self._forget(channels)
            raise
        rejected = self._rejected(channels, response)
        if rejected:
            self._forget(rejected)
            accepted = [c for c in channels if c not in rejected]
            raise DeribitSubscriptionError(
                rejected, accepted, self._subscription_hint()
            )
        return {scope: response}

    def unsubscribe(self, channels: List[str]) -> dict:
        """Unsubscribe from channels and drop every callback registered for them.

        Callbacks are dropped only after the gateway confirms, so a failed call
        leaves the local registry matching the server.
        """
        scope = self._sub_scope
        response = self.call(f"{scope}/unsubscribe", {"channels": list(channels)})
        self._forget(channels)
        return {scope: response}

    def unsubscribe_all(self) -> dict:
        """Unsubscribe from every channel and drop every registered callback.

        Callbacks are dropped only after the gateway confirms.
        """
        scope = self._sub_scope
        response = self.call(f"{scope}/unsubscribe_all", {})
        with self._sub_lock:
            self._subscriptions.clear()
        return {scope: response}

    def _forget(self, channels) -> None:
        with self._sub_lock:
            for ch in channels:
                self._subscriptions.pop(ch, None)

    @staticmethod
    def _rejected(channels: List[str], response: dict) -> List[str]:
        accepted = response.get("result")
        if not isinstance(accepted, list):
            return []  # unexpected shape: don't second-guess the gateway
        accepted = set(accepted)
        return [c for c in channels if c not in accepted]

    def _subscription_hint(self) -> str:
        if self.is_authenticated:
            return (
                "This client is authenticated (trading host), which serves user.* "
                "channels. Subscribe to market data with an unauthenticated "
                "DeribitRetailWSClient() (streams host)."
            )
        return (
            "This client is unauthenticated (streams host), which serves market "
            "data. user.* channels need a DeribitRetailWSClient with API keys."
        )

    def _run(self) -> None:
        while self._running:
            ws = self._ws  # None if re-auth already dropped it; reconnect below
            if ws is not None:
                try:
                    for raw in ws:
                        if not self._running:
                            return
                        self._handle_frame(raw)
                except (ConnectionClosed, OSError) as e:
                    logger.debug("Deribit WS read loop ended: %s", e)
                except Exception:
                    logger.exception("Deribit WS reader failed; reconnecting")
            if not self._running:
                return
            # Unexpected drop: fail in-flight calls (never resent) and reconnect.
            self._fail_pending(DeribitConnectionError("websocket disconnected"))
            self._close_ws(ws)
            if not self._reconnect():
                if self._running:
                    logger.error(
                        "Deribit WS reconnect gave up after %d attempts",
                        DERIBIT_WS_RETRY_MAX,
                    )
                self._running = False
                return

    def _handle_frame(self, raw) -> None:
        """Parse and dispatch one frame; a bad frame is logged, never fatal."""
        for msg in self._parse_frame(raw):
            try:
                self._dispatch(msg)
            except Exception:
                logger.exception("Deribit WS failed to handle a frame")

    @staticmethod
    def _parse_frame(raw) -> list:
        try:
            msg = json.loads(raw)
        except (TypeError, ValueError):
            logger.warning("Deribit WS ignored a non-JSON frame")
            return []
        msgs = msg if isinstance(msg, list) else [msg]
        return [m for m in msgs if isinstance(m, dict)]

    def _reconnect(self) -> bool:
        delay = DERIBIT_WS_RETRY_BASE
        for attempt in range(1, DERIBIT_WS_RETRY_MAX + 1):
            if not self._running:
                return False
            time.sleep(min(delay, DERIBIT_WS_RETRY_CAP))
            delay *= DERIBIT_WS_RETRY_FACTOR
            if not self._running:
                return False
            try:
                self._connect_and_auth()
                self._resubscribe()
                if not self._running:
                    # close() ran while we were reconnecting; don't leak the socket.
                    self._close_ws(self._ws)
                    return False
                logger.debug("Deribit WS reconnected on attempt %d", attempt)
                return True
            except Exception as e:
                self._close_ws(self._ws)
                logger.debug(
                    "Deribit WS reconnect attempt %d failed: %s",
                    attempt,
                    redact_secrets(e),
                )
        return False

    def _resubscribe(self) -> None:
        """Restore subscriptions on a fresh socket.

        Runs on the reader thread before it resumes reading, so it reads replies
        directly (like the auth handshake) instead of blocking in :meth:`call`.
        """
        with self._sub_lock:
            channels = list(self._subscriptions)
        if not channels:
            return
        response = self._handshake_call(
            f"{self._sub_scope}/subscribe", {"channels": channels}
        )
        rejected = self._rejected(channels, response)
        if rejected:
            self._forget(rejected)
            logger.warning(
                "Deribit WS: gateway did not restore subscriptions after reconnect: %s",
                ", ".join(rejected),
            )

    def _dispatch(self, msg: dict) -> None:
        rid = msg.get("id")
        if rid is not None:
            with self._pending_lock:
                fut = self._pending.pop(rid, None)
            if fut is None:
                return  # response to a fire-and-forget (e.g. our heartbeat test)
            try:
                if msg.get("error"):
                    fut.set_exception(rpc_error_from(msg["error"]))
                else:
                    fut.set_result(msg)
            except concurrent.futures.InvalidStateError:
                pass  # already failed by close()/disconnect
            return

        method = msg.get("method")
        if method == "subscription":
            params = msg.get("params", {})
            channel = params.get("channel")
            data = params.get("data")
            with self._sub_lock:
                callbacks = list(self._subscriptions.get(channel, []))
            for cb in callbacks:
                try:
                    cb(data, channel)
                except Exception:
                    logger.exception(
                        "Deribit subscription callback error on %s", channel
                    )
        elif method == "heartbeat":
            # Server liveness check; reply with public/test to keep the session up.
            if msg.get("params", {}).get("type") == "test_request":
                try:
                    self._send(
                        {
                            "jsonrpc": "2.0",
                            "id": self._next_id(),
                            "method": "public/test",
                            "params": {},
                        }
                    )
                except Exception as e:
                    logger.debug("heartbeat reply failed: %s", e)

    def _fail_pending(self, exc: Exception) -> None:
        # Holding _send_lock while bumping the generation means no call registered
        # before this point can still be sent afterwards.
        with self._send_lock:
            with self._pending_lock:
                self._gen += 1
                pending = list(self._pending.values())
                self._pending.clear()
        for fut in pending:
            try:
                fut.set_exception(exc)
            except concurrent.futures.InvalidStateError:
                pass

    def _close_ws(self, ws) -> None:
        """Close ``ws`` and clear it if it is still the current socket."""
        if ws is None:
            return
        with self._send_lock:
            if self._ws is ws:
                self._ws = None
        try:
            ws.close()
        except Exception:
            pass

    def _join_reader(
        self, reader: Optional[threading.Thread], timeout: float = 5.0
    ) -> None:
        if (
            reader is not None
            and reader.is_alive()
            and reader is not threading.current_thread()
        ):
            reader.join(timeout=timeout)

    def _cancel_reauth(self) -> None:
        if self._reauth_timer is not None:
            self._reauth_timer.cancel()

    def _connect_and_auth(self) -> None:
        self._cancel_reauth()
        ws = ws_connect(self.url, open_timeout=DERIBIT_WS_OPEN_TIMEOUT)
        with self._send_lock:
            self._ws = ws
        try:
            if self.is_authenticated:
                self._handshake_auth()
        except Exception:
            self._close_ws(ws)
            raise

    def _handshake_call(self, method: str, params: dict) -> dict:
        """Send one call and read its reply directly off the socket.

        Only valid while the reader loop is not consuming the socket: on open
        (reader not started) or during reconnect (the reader is the caller).
        Other frames that arrive first are dispatched normally.
        """
        rid = self._next_id()
        self._send({"jsonrpc": "2.0", "id": rid, "method": method, "params": params})
        deadline = time.monotonic() + DERIBIT_WS_OPEN_TIMEOUT
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError(f"timed out waiting for {method} response")
            ws = self._ws
            if ws is None:
                raise DeribitConnectionError(f"socket closed during {method}")
            for msg in self._parse_frame(ws.recv(timeout=remaining)):
                if msg.get("id") == rid:
                    if msg.get("error"):
                        raise rpc_error_from(msg["error"])
                    return msg
                try:
                    self._dispatch(msg)
                except Exception:
                    logger.exception("Deribit WS failed to handle a frame")

    def _handshake_auth(self) -> None:
        """Authenticate on a fresh socket, before the reader loop owns it.

        Scheduled in-band re-auth goes through :meth:`call` instead.
        """
        try:
            msg = self._handshake_call(
                DERIBIT_AUTH_METHOD, build_auth_params(self.api_key, self.api_secret)
            )
        except DeribitRPCError as e:
            raise DeribitAuthError(
                f"public/auth rejected: [{e.code}] {redact_secrets(e.message)}"
            ) from None
        except TimeoutError as e:
            raise DeribitAuthError(str(e)) from None
        except (ConnectionClosed, OSError, DeribitConnectionError) as e:
            raise DeribitAuthError(f"socket closed during auth: {e}") from e
        self._schedule_reauth(msg.get("result", {}).get("expires_in"))

    def _schedule_reauth(self, expires_in: Optional[int]) -> None:
        self._cancel_reauth()
        if not expires_in:
            return
        delay = expires_in * DERIBIT_TOKEN_REFRESH_RATIO
        self._reauth_timer = threading.Timer(delay, self._reauth)
        self._reauth_timer.daemon = True
        self._reauth_timer.start()

    def _reauth(self) -> None:
        """In-band re-auth on the live socket (runs on the timer thread)."""
        if not self._running:
            return
        ws = self._ws  # only ever drop the socket this re-auth started on
        try:
            result = self.call(
                DERIBIT_AUTH_METHOD,
                build_auth_params(self.api_key, self.api_secret),
            )
            self._schedule_reauth(result.get("result", {}).get("expires_in"))
        except Exception as e:
            if not self._running or ws is not self._ws:
                return  # closed, or already reconnected; this result is stale
            logger.error(
                "Deribit WS re-auth failed, forcing reconnect: %s", redact_secrets(e)
            )
            # Drop the socket; the reader loop will reconnect + re-auth fresh.
            self._close_ws(ws)
