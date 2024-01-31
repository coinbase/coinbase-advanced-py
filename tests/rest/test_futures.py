import unittest

from requests_mock import Mocker

from coinbase.rest import RESTClient

from ..constants import TEST_API_KEY, TEST_API_SECRET


class FuturesTest(unittest.TestCase):
    def test_get_futures_balance_summary(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"key_1": "value_1", "key_2": "value_2"}

        with Mocker() as m:
            m.request(
                "GET",
                "https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary",
                json=expected_response,
            )
            balance_summary = client.get_futures_balance_summary()

            captured_request = m.request_history[0]

            self.assertEqual(captured_request.query, "")
            self.assertEqual(balance_summary, expected_response)

    def test_list_futures_positions(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"key_1": "value_1", "key_2": "value_2"}

        with Mocker() as m:
            m.request(
                "GET",
                "https://api.coinbase.com/api/v3/brokerage/cfm/positions",
                json=expected_response,
            )
            positions = client.list_futures_positions()

            captured_request = m.request_history[0]

            self.assertEqual(captured_request.query, "")
            self.assertEqual(positions, expected_response)

    def test_get_futures_position(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"key_1": "value_1", "key_2": "value_2"}

        with Mocker() as m:
            m.request(
                "GET",
                "https://api.coinbase.com/api/v3/brokerage/cfm/positions/PRODUCT_ID_1",
                json=expected_response,
            )
            position = client.get_futures_position("PRODUCT_ID_1")

            captured_request = m.request_history[0]

            self.assertEqual(captured_request.query, "")
            self.assertEqual(position, expected_response)

    def test_schedule_futures_sweep(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"key_1": "value_1", "key_2": "value_2"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/cfm/sweeps/schedule",
                json=expected_response,
            )
            response = client.schedule_futures_sweep("5")

            captured_request = m.request_history[0]
            captured_json = captured_request.json()

            self.assertEqual(captured_request.query, "")
            self.assertEqual(captured_json, {"usd_amount": "5"})
            self.assertEqual(response, expected_response)

    def test_list_futures_sweeps(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"key_1": "value_1", "key_2": "value_2"}

        with Mocker() as m:
            m.request(
                "GET",
                "https://api.coinbase.com/api/v3/brokerage/cfm/sweeps",
                json=expected_response,
            )
            sweeps = client.list_futures_sweeps()

            captured_request = m.request_history[0]

            self.assertEqual(captured_request.query, "")
            self.assertEqual(sweeps, expected_response)

    def test_cancel_pending_futures_sweep(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"key_1": "value_1", "key_2": "value_2"}

        with Mocker() as m:
            m.request(
                "DELETE",
                "https://api.coinbase.com/api/v3/brokerage/cfm/sweeps",
                json=expected_response,
            )
            delete = client.cancel_pending_futures_sweep()

            captured_request = m.request_history[0]

            self.assertEqual(captured_request.query, "")
            self.assertEqual(delete, expected_response)
