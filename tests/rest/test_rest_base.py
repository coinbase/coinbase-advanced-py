import unittest

from requests_mock import Mocker

from coinbase.__version__ import __version__
from coinbase.rest import RESTClient
from tests.constants import TEST_API_KEY, TEST_API_SECRET


class RestBaseTest(unittest.TestCase):
    def test_get(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"key_1": "value_1", "key_2": "value_2"}

        with Mocker() as m:
            m.request(
                "GET",
                "https://api.coinbase.com/api/v3/brokerage/accounts",
                json=expected_response,
            )

            params = {"limit": 2}
            accounts = client.get("/api/v3/brokerage/accounts", params)

            captured_request = m.request_history[0]
            captured_query = captured_request.query
            captured_headers = captured_request.headers

            self.assertEqual(captured_request.method, "GET")

            self.assertEqual(captured_query, "limit=2")

            self.assertTrue("User-Agent" in captured_headers)
            self.assertEqual(
                captured_headers["User-Agent"], "coinbase-advanced-py/" + __version__
            )
            self.assertTrue("Authorization" in captured_headers)
            self.assertTrue(captured_headers["Authorization"].startswith("Bearer "))

            self.assertEqual(accounts, expected_response)

    def test_post(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"key_1": "value_1", "key_2": "value_2"}

        with Mocker() as m:
            m.request(
                "POST",
                "https://api.coinbase.com/api/v3/brokerage/portfolios",
                json=expected_response,
            )

            data = {"name": "TestName"}
            portfolio = client.post("/api/v3/brokerage/portfolios", data=data)

            captured_request = m.request_history[0]
            captured_json = captured_request.json()
            captured_headers = captured_request.headers

            self.assertEqual(captured_request.method, "POST")

            self.assertEqual(captured_json, data)

            self.assertTrue("User-Agent" in captured_headers)
            self.assertEqual(
                captured_headers["User-Agent"], "coinbase-advanced-py/" + __version__
            )
            self.assertTrue("Authorization" in captured_headers)
            self.assertTrue(captured_headers["Authorization"].startswith("Bearer "))

            self.assertEqual(portfolio, expected_response)
