import unittest
from io import StringIO

from coinbase.api_base import APIBase

from .constants import TEST_API_KEY, TEST_API_SECRET


class RestBaseTest(unittest.TestCase):
    def test_no_api_key(self):
        with self.assertRaises(Exception):
            APIBase("test_key", None)

    def test_key_api_key_vars(self):
        try:
            APIBase(api_key=TEST_API_KEY, api_secret=TEST_API_SECRET)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    def test_key_file_string(self):
        try:
            APIBase(key_file="tests/test_api_key.json")
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    def test_key_file_object(self):
        try:
            key_file_object = StringIO(
                '{"name": "test-api-key-name","privateKey": "test-api-key-private-key"}'
            )
            APIBase(key_file=key_file_object)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    def test_key_file_no_key(self):
        with self.assertRaises(Exception):
            key_file_object = StringIO('{"field_1": "value_1","field_2": "value_2"}')
            APIBase(key_file=key_file_object)

    def test_key_file_multiple_key_inputs(self):
        with self.assertRaises(Exception):
            key_file_object = StringIO('{"field_1": "value_1","field_2": "value_2"}')
            APIBase(
                api_key=TEST_API_KEY,
                api_secret=TEST_API_SECRET,
                key_file=key_file_object,
            )

    def test_key_file_invalid_json(self):
        with self.assertRaises(Exception):
            key_file_object = StringIO(
                '"name": "test-api-key-name","privateKey": "test-api-key-private-key"'
            )
            APIBase(key_file=key_file_object)
