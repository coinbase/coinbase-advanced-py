import unittest

from requests_mock import ANY, Mocker

from coinbase.deribit.errors import DeribitRateLimitError, DeribitRPCError
from coinbase.deribit.rest_client import DeribitRetailClient

from ..constants import TEST_API_KEY, TEST_API_SECRET

BASE = "https://drb.coinbase.com/api/v2"


def _test_client():
    return DeribitRetailClient(TEST_API_KEY, TEST_API_SECRET)


class DeribitRESTClientTest(unittest.TestCase):
    def setUp(self):
        self.client = _test_client()

    def test_public_method_skips_auth(self):
        with Mocker() as m:
            m.post(
                f"{BASE}/public/get_time",
                json={"id": 1, "jsonrpc": "2.0", "result": 1700000000000},
            )
            result = self.client.public_get_time()
            self.assertEqual(result["result"], 1700000000000)
            # Only the one call; no public/auth exchange for a public method.
            self.assertEqual(len(m.request_history), 1)

    def test_private_method_authenticates_and_wraps(self):
        with Mocker() as m:
            m.post(
                f"{BASE}/public/auth",
                json={"result": {"access_token": "TOK", "expires_in": 900}},
            )
            m.post(
                f"{BASE}/private/buy",
                json={
                    "id": 2,
                    "jsonrpc": "2.0",
                    "result": {"order": {"order_id": "E1"}},
                },
            )
            buy = self.client.private_buy(
                instrument_name="ETH-PERPETUAL", amount=1, type="market"
            )
            self.assertEqual(buy.result.order.order_id, "E1")
            buy_req = [r for r in m.request_history if r.path.endswith("/private/buy")][
                0
            ]
            self.assertEqual(buy_req.headers["Authorization"], "Bearer TOK")

    def test_rpc_error_maps_to_typed_exception(self):
        with Mocker() as m:
            m.post(
                f"{BASE}/public/auth",
                json={"result": {"access_token": "TOK", "expires_in": 900}},
            )
            m.post(
                f"{BASE}/private/cancel",
                json={
                    "error": {
                        "code": 10028,
                        "message": "too_many_requests",
                        "data": {"retry_after": 2},
                    }
                },
            )
            with self.assertRaises(DeribitRateLimitError):
                self.client.private_cancel(order_id="x")

    def test_production_is_the_default(self):
        client = DeribitRetailClient(TEST_API_KEY, TEST_API_SECRET)
        self.assertEqual(client._endpoint, "https://drb.coinbase.com/api/v2")

    def test_test_environment_is_not_available(self):
        # The pre-launch test gateway was retired; only production exists.
        with self.assertRaises(ValueError):
            DeribitRetailClient(TEST_API_KEY, TEST_API_SECRET, environment="test")

    def test_explicit_base_url_overrides_environment(self):
        client = DeribitRetailClient(
            TEST_API_KEY, TEST_API_SECRET, base_url="custom.example.com"
        )
        self.assertEqual(client._endpoint, "https://custom.example.com/api/v2")

    def test_unknown_environment_raises(self):
        with self.assertRaises(ValueError):
            DeribitRetailClient(TEST_API_KEY, TEST_API_SECRET, environment="bogus")

    def test_call_escape_hatch(self):
        with Mocker() as m:
            m.post(
                f"{BASE}/public/get_status",
                json={"id": 3, "jsonrpc": "2.0", "result": {"locked": False}},
            )
            result = self.client.call("public/get_status")
            self.assertEqual(result["result"]["locked"], False)

    def test_default_timeout_is_finite(self):
        self.assertEqual(self.client.timeout, 30)
        self.assertEqual(self.client._auth._timeout, 30)

    def test_rejected_token_is_refreshed_and_retried_once(self):
        with Mocker() as m:
            m.post(
                f"{BASE}/public/auth",
                [
                    {"json": {"result": {"access_token": "OLD", "expires_in": 900}}},
                    {"json": {"result": {"access_token": "NEW", "expires_in": 900}}},
                ],
            )
            m.post(
                f"{BASE}/private/get_positions",
                [
                    {"json": {"error": {"code": 13009, "message": "unauthorized"}}},
                    {"json": {"jsonrpc": "2.0", "result": []}},
                ],
            )
            self.client.call("private/get_positions", {"currency": "USDC"})
            calls = [
                r.headers["Authorization"]
                for r in m.request_history
                if r.path.endswith("/private/get_positions")
            ]
            self.assertEqual(calls, ["Bearer OLD", "Bearer NEW"])

    def test_non_token_error_is_not_retried(self):
        with Mocker() as m:
            m.post(
                f"{BASE}/public/auth",
                json={"result": {"access_token": "TOK", "expires_in": 900}},
            )
            m.post(
                f"{BASE}/private/buy",
                json={"error": {"code": 10009, "message": "not_enough_funds"}},
            )
            with self.assertRaises(Exception):
                self.client.call("private/buy", {"instrument_name": "X"})
            buys = [r for r in m.request_history if r.path.endswith("/private/buy")]
            self.assertEqual(len(buys), 1)

    def test_non_json_auth_response_raises_auth_error(self):
        from coinbase.deribit.errors import DeribitAuthError

        with Mocker() as m:
            m.post(f"{BASE}/public/auth", text="<html>bad gateway</html>")
            with self.assertRaises(DeribitAuthError):
                self.client.call("private/get_positions", {})

    def test_auth_rejection_reports_gateway_error(self):
        from coinbase.deribit.errors import DeribitAuthError

        with Mocker() as m:
            m.post(
                f"{BASE}/public/auth",
                status_code=401,
                json={"error": {"code": 13004, "message": "invalid_credentials"}},
            )
            with self.assertRaises(DeribitAuthError) as ctx:
                self.client.call("private/get_positions", {})
        self.assertIn("13004", str(ctx.exception))
        self.assertIn("HTTP 401", str(ctx.exception))

    def test_private_method_without_keys_raises_locally(self):
        anon = DeribitRetailClient(api_key=None, api_secret=None)
        with Mocker() as m:
            m.post(ANY, json={"result": {}})
            with self.assertRaises(DeribitRPCError) as ctx:
                anon.private_get_positions(currency="USDC")
            self.assertEqual(m.call_count, 0)
        self.assertEqual(ctx.exception.code, 13009)


if __name__ == "__main__":
    unittest.main()
