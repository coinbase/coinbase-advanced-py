import unittest

from requests_mock import Mocker

from coinbase.rest import RESTClient

from ..constants import TEST_API_KEY, TEST_API_SECRET


class TimeTest(unittest.TestCase):
    def test_get_time(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"iso": "2022-01-01T00:00:00Z", "epoch": 1640995200}

        with Mocker() as m:
            m.request(
                "GET",
                "https://api.coinbase.com/api/v3/brokerage/time",
                json=expected_response,
            )
            time = client.get_unix_time()

            captured_request = m.request_history[0]

            self.assertEqual(captured_request.query, "")
            self.assertEqual(time, expected_response)
