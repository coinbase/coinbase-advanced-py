import inspect
import unittest

from coinbase.deribit._generated import channels, models
from coinbase.deribit._generated.rest_methods import GeneratedRESTMixin


class GeneratedLayerTest(unittest.TestCase):
    def test_channel_builder_fills_segments(self):
        self.assertEqual(
            channels.ticker_instrument_name_interval("BTC-PERPETUAL", "100ms"),
            "ticker.BTC-PERPETUAL.100ms",
        )
        self.assertEqual(
            channels.book_instrument_name_group_depth_interval(
                "BTC-PERPETUAL", "none", "10", "100ms"
            ),
            "book.BTC-PERPETUAL.none.10.100ms",
        )

    def test_model_nests_objects_and_lists(self):
        buy = models.PrivateBuyAndSellResponse(
            {
                "id": 1,
                "jsonrpc": "2.0",
                "result": {
                    "order": {"order_id": "E1", "direction": "buy"},
                    "trades": [{"trade_id": "t1"}, {"trade_id": "t2"}],
                },
            }
        )
        self.assertEqual(type(buy.result).__name__, "PrivateBuyAndSellResponseResult")
        self.assertEqual(buy.result.order.order_id, "E1")
        self.assertEqual([t.trade_id for t in buy.result.trades], ["t1", "t2"])

    def test_to_dict_round_trips(self):
        buy = models.PrivateBuyAndSellResponse(
            {"id": 1, "jsonrpc": "2.0", "result": {"order": {"order_id": "E1"}}}
        )
        self.assertEqual(buy.to_dict()["result"]["order"]["order_id"], "E1")

    def test_optional_rpc_params_are_keyword_only(self):
        params = inspect.signature(GeneratedRESTMixin.private_buy).parameters
        self.assertEqual(
            params["instrument_name"].kind, inspect.Parameter.POSITIONAL_OR_KEYWORD
        )
        for name in ("amount", "type", "price", "label"):
            self.assertEqual(params[name].kind, inspect.Parameter.KEYWORD_ONLY, name)

    def test_rest_client_exposes_only_rest_served_methods(self):
        from coinbase.deribit import DeribitRetailClient, DeribitRetailWSClient

        ws_only = [
            "public_hello",
            "public_set_heartbeat",
            "public_disable_heartbeat",
            "private_enable_cancel_on_disconnect",
            "private_get_cancel_on_disconnect",
            "private_disable_cancel_on_disconnect",
            "private_logout",
            "public_get_tradingview_chart_data",
            "private_get_access_log",
        ]
        raw_subscription = [
            f"{scope}_{op}"
            for scope in ("public", "private")
            for op in ("subscribe", "unsubscribe", "unsubscribe_all")
        ]
        for name in ws_only:
            self.assertFalse(hasattr(DeribitRetailClient, name), name)
            self.assertTrue(hasattr(DeribitRetailWSClient, name), name)
        for name in raw_subscription:
            self.assertFalse(hasattr(DeribitRetailClient, name), name)
            self.assertFalse(hasattr(DeribitRetailWSClient, name), name)
        for name in ("subscribe", "unsubscribe", "unsubscribe_all"):
            self.assertTrue(hasattr(DeribitRetailWSClient, name), name)

    def test_block_trade_and_rfq_methods_are_not_generated(self):
        from coinbase.deribit import DeribitRetailWSClient

        leftovers = [
            n for n in dir(DeribitRetailWSClient) if "block" in n or "rfq" in n
        ]
        self.assertEqual(leftovers, [])

    def test_generated_code_only_embeds_expected_identifiers(self):
        # Guards against spec values breaking out of string literals in the
        # committed generated code.
        import re
        from pathlib import Path

        import coinbase.deribit._generated as gen

        source = (Path(gen.__file__).parent / "rest_methods.py").read_text()
        methods = re.findall(r'self\._rpc\(\s*"([^"]*)"', source)
        self.assertTrue(methods)
        for method in methods:
            self.assertRegex(method, r"^(public|private)(/[a-z0-9_]+)+$")
        for key in re.findall(r"params = \{([^}]*)\}", source):
            for name in re.findall(r'"([^"]*)":', key):
                self.assertRegex(name, r"^[A-Za-z_][A-Za-z0-9_]*$")
        for name, fn in inspect.getmembers(channels, inspect.isfunction):
            args = ["x"] * len(inspect.signature(fn).parameters)
            self.assertRegex(fn(*args), r"^[A-Za-z0-9_.\-]+$", name)

    def test_model_keeps_data_when_gateway_shape_differs_from_spec(self):
        # Spec says result is a list; the gateway returns an object keyed by currency.
        raw = {"result": {"btc": {"future": ["PERPETUAL"]}}}
        resp = models.PublicGetExpirationsResponse(raw)
        self.assertEqual(resp.to_dict(), raw)
        self.assertEqual(resp.result.btc, {"future": ["PERPETUAL"]})

    def test_model_accepts_list_where_spec_says_object(self):
        cls = type(
            "Tmp",
            (models.DeribitModel,),
            {"_NESTED": {"item": (models.DeribitModel, False)}},
        )
        raw = {"item": [{"a": 1}, {"a": 2}]}
        self.assertEqual(cls(raw).to_dict(), raw)


if __name__ == "__main__":
    unittest.main()
