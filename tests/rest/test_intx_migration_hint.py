import unittest
from unittest.mock import patch

from requests.exceptions import HTTPError
from requests_mock import Mocker

from coinbase.rest import RESTClient, _intx_cutover

from ..constants import TEST_API_KEY, TEST_API_SECRET

BASE = "https://api.coinbase.com/api/v3/brokerage"
GONE = {"error": "NOT_FOUND", "message": "endpoint unavailable"}
LOGGER = "coinbase.RESTClient"


class IntxMigrationHintTest(unittest.TestCase):
    """INTX calls still go out; on failure the SDK logs a Deribit migration hint."""

    def setUp(self):
        self.client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

    def assert_hint_on_failure(self, method, url, call, method_name, replacement):
        with Mocker() as m:
            m.request(method, url, status_code=404, json=GONE)
            with self.assertLogs(LOGGER, level="ERROR") as logs:
                with self.assertRaises(HTTPError) as ctx:
                    call()
            self.assertEqual(m.call_count, 1)
        self.assertIn("endpoint unavailable", str(ctx.exception))
        hints = [line for line in logs.output if "October 1, 2026" in line]
        self.assertEqual(len(hints), 1)
        self.assertIn(f"{method_name}() failed", hints[0])
        if replacement:
            self.assertIn(replacement, hints[0])
        else:
            self.assertIn("no Deribit Retail replacement", hints[0])

    def test_allocate_portfolio(self):
        self.assert_hint_on_failure(
            "POST",
            f"{BASE}/intx/allocate",
            lambda: self.client.allocate_portfolio("u", "BTC-PERP-INTX", "1", "USD"),
            "allocate_portfolio",
            "private_submit_transfer_between_subaccounts",
        )

    def test_get_perps_portfolio_summary(self):
        self.assert_hint_on_failure(
            "GET",
            f"{BASE}/intx/portfolio/u",
            lambda: self.client.get_perps_portfolio_summary("u"),
            "get_perps_portfolio_summary",
            "private_get_account_summary",
        )

    def test_list_perps_positions(self):
        self.assert_hint_on_failure(
            "GET",
            f"{BASE}/intx/positions/u",
            lambda: self.client.list_perps_positions("u"),
            "list_perps_positions",
            "private_get_positions",
        )

    def test_get_perps_position(self):
        self.assert_hint_on_failure(
            "GET",
            f"{BASE}/intx/positions/u/BTC-PERP-INTX",
            lambda: self.client.get_perps_position("u", "BTC-PERP-INTX"),
            "get_perps_position",
            "private_get_position",
        )

    def test_get_perps_portfolio_balances(self):
        self.assert_hint_on_failure(
            "GET",
            f"{BASE}/intx/balances/u",
            lambda: self.client.get_perps_portfolio_balances("u"),
            "get_perps_portfolio_balances",
            "private_get_account_summaries",
        )

    def test_opt_in_or_out_multi_asset_collateral(self):
        self.assert_hint_on_failure(
            "POST",
            f"{BASE}/intx/multi_asset_collateral",
            lambda: self.client.opt_in_or_out_multi_asset_collateral("u", True),
            "opt_in_or_out_multi_asset_collateral",
            "private_change_margin_model",
        )

    def test_create_order_perp_product(self):
        self.assert_hint_on_failure(
            "POST",
            f"{BASE}/orders",
            lambda: self.client.market_order_buy(
                "id", "btc-perp-intx", quote_size="10"
            ),
            "create_order",
            "private_buy or private_sell",
        )

    def test_preview_order_perp_product(self):
        self.assert_hint_on_failure(
            "POST",
            f"{BASE}/orders/preview",
            lambda: self.client.preview_market_order_buy(
                "BTC-PERP-INTX", quote_size="10"
            ),
            "preview_order",
            None,
        )

    def test_close_position_perp_product(self):
        self.assert_hint_on_failure(
            "POST",
            f"{BASE}/orders/close_position",
            lambda: self.client.close_position("id", "BTC-PERP-INTX"),
            "close_position",
            "private_close_position",
        )

    def test_no_hint_for_spot_order_failure(self):
        with Mocker() as m:
            m.request("POST", f"{BASE}/orders", status_code=400, json=GONE)
            with self.assertLogs(LOGGER, level="ERROR") as logs:
                with self.assertRaises(HTTPError):
                    self.client.market_order_buy("id", "BTC-USD", quote_size="10")
        self.assertFalse(any("October 1, 2026" in line for line in logs.output))

    def test_no_hint_on_success(self):
        with Mocker() as m:
            m.request("GET", f"{BASE}/intx/positions/u", json={"positions": []})
            with patch.object(_intx_cutover.logger, "error") as log_error:
                self.client.list_perps_positions("u")
            log_error.assert_not_called()


if __name__ == "__main__":
    unittest.main()
