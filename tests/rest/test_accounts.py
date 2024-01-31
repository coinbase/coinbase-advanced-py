import unittest

from requests_mock import Mocker

from coinbase.rest import RESTClient

from ..constants import TEST_API_KEY, TEST_API_SECRET


class AccountsTest(unittest.TestCase):
    def test_get_accounts(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"accounts": [{"uuid": "account1"}, {"name": "account2"}]}

        with Mocker() as m:
            m.request(
                "GET",
                "https://api.coinbase.com/api/v3/brokerage/accounts",
                json=expected_response,
            )
            accounts = client.get_accounts(limit=2, cursor="abcd")

            captured_request = m.request_history[0]

            self.assertEqual(captured_request.query, "limit=2&cursor=abcd")
            self.assertEqual(accounts, expected_response)

    def test_get_account(self):
        client = RESTClient(TEST_API_KEY, TEST_API_SECRET)

        expected_response = {"uuid": "account1"}

        with Mocker() as m:
            m.request(
                "GET",
                "https://api.coinbase.com/api/v3/brokerage/accounts/account1",
                json=expected_response,
            )
            account = client.get_account("account1")

            captured_request = m.request_history[0]

            self.assertEqual(captured_request.query, "")
            self.assertEqual(account, expected_response)
