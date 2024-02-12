import unittest

from requests_mock import Mocker

from coinbase.rest import RESTClient

from ..constants import TEST_API_KEY, TEST_API_SECRET


class OrdersTest(unittest.TestCase):
    def test_create_order(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order_configuration = {"market_market_ioc": {"quote_size": "1"}}

            order = client.create_order(
                "client_order_id_1",
                "product_id_1",
                "BUY",
                order_configuration,
                self_trade_prevention_id="self_trade_prevention_id_1",
                margin_type="CROSS",
                leverage="5",
                retail_portfolio_id="portfolio_id_1",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {"market_market_ioc": {"quote_size": "1"}},
                    "self_trade_prevention_id": "self_trade_prevention_id_1",
                    "margin_type": "CROSS",
                    "leverage": "5",
                    "retail_portfolio_id": "portfolio_id_1",
                },
            )
            self.assertEqual(order, expected_response)

    def test_market_order(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )

            order = client.market_order(
                "client_order_id_1", "product_id_1", "BUY", quote_size="1"
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {"market_market_ioc": {"quote_size": "1"}},
                },
            )
            self.assertEqual(order, expected_response)

    def test_market_order_buy(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )

            order = client.market_order_buy("client_order_id_1", "product_id_1", "1")

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {"market_market_ioc": {"quote_size": "1"}},
                },
            )
            self.assertEqual(order, expected_response)

    def test_market_order_sell(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )

            order = client.market_order_sell("client_order_id_1", "product_id_1", "1")

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "SELL",
                    "order_configuration": {"market_market_ioc": {"base_size": "1"}},
                },
            )
            self.assertEqual(order, expected_response)

    def test_limit_order_gtc(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.limit_order_gtc(
                "client_order_id_1",
                "product_id_1",
                "BUY",
                "1",
                "100",
                True,
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "limit_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "post_only": True,
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_limit_order_gtc_buy(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.limit_order_gtc_buy(
                "client_order_id_1",
                "product_id_1",
                "1",
                "100",
                True,
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "limit_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "post_only": True,
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_limit_order_gtc_sell(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.limit_order_gtc_sell(
                "client_order_id_1",
                "product_id_1",
                "1",
                "100",
                True,
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "SELL",
                    "order_configuration": {
                        "limit_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "post_only": True,
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_limit_order_gtd(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.limit_order_gtd(
                "client_order_id_1",
                "product_id_1",
                "BUY",
                "1",
                "100",
                "2022-01-01T00:00:00Z",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "limit_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "end_time": "2022-01-01T00:00:00Z",
                            "post_only": False,
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_limit_order_gtd_buy(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.limit_order_gtd_buy(
                "client_order_id_1", "product_id_1", "1", "100", "2022-01-01T00:00:00Z"
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "limit_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "end_time": "2022-01-01T00:00:00Z",
                            "post_only": False,
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_limit_order_gtd_sell(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.limit_order_gtd_sell(
                "client_order_id_1", "product_id_1", "1", "100", "2022-01-01T00:00:00Z"
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "SELL",
                    "order_configuration": {
                        "limit_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "end_time": "2022-01-01T00:00:00Z",
                            "post_only": False,
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_stop_limit_order_gtc(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.stop_limit_order_gtc(
                "client_order_id_1",
                "product_id_1",
                "BUY",
                "1",
                "100",
                "90",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_stop_limit_order_gtc_buy(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.stop_limit_order_gtc_buy(
                "client_order_id_1",
                "product_id_1",
                "1",
                "100",
                "90",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_stop_limit_order_gtc_sell(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.stop_limit_order_gtc_sell(
                "client_order_id_1",
                "product_id_1",
                "1",
                "100",
                "90",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "SELL",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_stop_limit_order_gtd(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.stop_limit_order_gtd(
                "client_order_id_1",
                "product_id_1",
                "BUY",
                "1",
                "100",
                "90",
                "2022-01-01T00:00:00Z",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "end_time": "2022-01-01T00:00:00Z",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_stop_limit_order_gtd_buy(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.stop_limit_order_gtd_buy(
                "client_order_id_1",
                "product_id_1",
                "1",
                "100",
                "90",
                "2022-01-01T00:00:00Z",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "end_time": "2022-01-01T00:00:00Z",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_stop_limit_order_gtd_sell(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders",
                json=expected_response,
            )
            order = client.stop_limit_order_gtd_sell(
                "client_order_id_1",
                "product_id_1",
                "1",
                "100",
                "90",
                "2022-01-01T00:00:00Z",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "client_order_id": "client_order_id_1",
                    "product_id": "product_id_1",
                    "side": "SELL",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "end_time": "2022-01-01T00:00:00Z",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                },
            )
            self.assertEqual(order, expected_response)

    def test_get_order(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "GET",
                "https://api.coinbase.com/api/v3/brokerage/orders/historical/order_id_1",
                json=expected_response,
            )
            order = client.get_order("order_id_1")

            captured_request = m.request_history[0]

            self.assertEqual(captured_request.query, "")
            self.assertEqual(order, expected_response)

    def test_list_orders(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"orders": [{"order_id": "1234"}, {"order_id": "5678"}]}

        with Mocker() as m:
            m.request(
                "GET",
                "https://api.coinbase.com/api/v3/brokerage/orders/historical/batch",
                json=expected_response,
            )
            orders = client.list_orders(
                product_id="product_id_1",
                order_status="OPEN",
                limit=2,
                product_type="SPOT",
            )

            captured_request = m.request_history[0]

            self.assertEqual(
                captured_request.query,
                "product_id=product_id_1&order_status=open&limit=2&product_type=spot",
            )
            self.assertEqual(orders, expected_response)

    def test_get_fills(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"orders": [{"order_id": "1234"}]}

        with Mocker() as m:
            m.request(
                "GET",
                "https://api.coinbase.com/api/v3/brokerage/orders/historical/fills",
                json=expected_response,
            )
            orders = client.get_fills(
                order_id="1234", product_id="product_id_1", limit=2, cursor="abc"
            )

            captured_request = m.request_history[0]

            self.assertEqual(
                captured_request.query,
                "order_id=1234&product_id=product_id_1&limit=2&cursor=abc",
            )
            self.assertEqual(orders, expected_response)

    def test_edit_order(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "order_id_1"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/edit",
                json=expected_response,
            )
            order = client.edit_order("order_id_1", "100", "50")

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json, {"order_id": "order_id_1", "size": "100", "price": "50"}
            )
            self.assertEqual(order, expected_response)

    def test_preview_edit_order(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "order_id_1"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/edit_preview",
                json=expected_response,
            )
            order = client.preview_edit_order("order_id_1", "100", "50")

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json, {"order_id": "order_id_1", "size": "100", "price": "50"}
            )
            self.assertEqual(order, expected_response)

    def test_cancel_orders(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "order_id_1"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel",
                json=expected_response,
            )
            order = client.cancel_orders(["order_id_1", "order_id_2"])

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(captured_json, {"order_ids": ["order_id_1", "order_id_2"]})
            self.assertEqual(order, expected_response)

    def test_preview_order(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "order_id_1"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )

            order_configuration = {"market_market_ioc": {"quote_size": "1"}}

            preview = client.preview_order(
                "product_id_1",
                "BUY",
                order_configuration,
                commission_rate="0.005",
                is_max=False,
                tradable_balance="100",
                skip_fcm_risk_check=False,
                leverage="5",
                margin_type="CROSS",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {"market_market_ioc": {"quote_size": "1"}},
                    "commission_rate": {"value": "0.005"},
                    "is_max": False,
                    "tradable_balance": "100",
                    "skip_fcm_risk_check": False,
                    "leverage": "5",
                    "margin_type": "CROSS",
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_market_order(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )

            preview = client.preview_market_order("product_id_1", "BUY", quote_size="1")

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {"market_market_ioc": {"quote_size": "1"}},
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_market_order_buy(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )

            preview = client.preview_market_order_buy("product_id_1", "1")

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {"market_market_ioc": {"quote_size": "1"}},
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_market_order_sell(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )

            preview = client.preview_market_order_sell("product_id_1", "1")

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "SELL",
                    "order_configuration": {"market_market_ioc": {"base_size": "1"}},
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_limit_order_gtc(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_limit_order_gtc(
                "product_id_1",
                "BUY",
                "1",
                "100",
                True,
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "limit_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "post_only": True,
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_limit_order_gtc_buy(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_limit_order_gtc_buy(
                "product_id_1",
                "1",
                "100",
                True,
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "limit_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "post_only": True,
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_limit_order_gtc_sell(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_limit_order_gtc_sell(
                "product_id_1",
                "1",
                "100",
                True,
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "SELL",
                    "order_configuration": {
                        "limit_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "post_only": True,
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_limit_order_gtd(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_limit_order_gtd(
                "product_id_1",
                "BUY",
                "1",
                "100",
                "2022-01-01T00:00:00Z",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "limit_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "end_time": "2022-01-01T00:00:00Z",
                            "post_only": False,
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_limit_order_gtd_buy(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_limit_order_gtd_buy(
                "product_id_1", "1", "100", "2022-01-01T00:00:00Z"
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "limit_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "end_time": "2022-01-01T00:00:00Z",
                            "post_only": False,
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_limit_order_gtd_sell(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_limit_order_gtd_sell(
                "product_id_1", "1", "100", "2022-01-01T00:00:00Z"
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "SELL",
                    "order_configuration": {
                        "limit_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "end_time": "2022-01-01T00:00:00Z",
                            "post_only": False,
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_stop_limit_order_gtc(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_stop_limit_order_gtc(
                "product_id_1",
                "BUY",
                "1",
                "100",
                "90",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_stop_limit_order_gtc_buy(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_stop_limit_order_gtc_buy(
                "product_id_1",
                "1",
                "100",
                "90",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_stop_limit_order_gtc_sell(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_stop_limit_order_gtc_sell(
                "product_id_1",
                "1",
                "100",
                "90",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "SELL",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtc": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_stop_limit_order_gtd(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_stop_limit_order_gtd(
                "product_id_1",
                "BUY",
                "1",
                "100",
                "90",
                "2022-01-01T00:00:00Z",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "end_time": "2022-01-01T00:00:00Z",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_stop_limit_order_gtd_buy(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_stop_limit_order_gtd_buy(
                "product_id_1",
                "1",
                "100",
                "90",
                "2022-01-01T00:00:00Z",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "BUY",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "end_time": "2022-01-01T00:00:00Z",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)

    def test_preview_stop_limit_order_gtd_sell(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"order_id": "1234"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/orders/preview",
                json=expected_response,
            )
            preview = client.preview_stop_limit_order_gtd_sell(
                "product_id_1",
                "1",
                "100",
                "90",
                "2022-01-01T00:00:00Z",
                "STOP_DIRECTION_STOP_UP",
            )

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(
                captured_json,
                {
                    "product_id": "product_id_1",
                    "side": "SELL",
                    "order_configuration": {
                        "stop_limit_stop_limit_gtd": {
                            "base_size": "1",
                            "limit_price": "100",
                            "stop_price": "90",
                            "end_time": "2022-01-01T00:00:00Z",
                            "stop_direction": "STOP_DIRECTION_STOP_UP",
                        }
                    },
                    "is_max": False,
                    "skip_fcm_risk_check": False,
                },
            )
            self.assertEqual(preview, expected_response)
