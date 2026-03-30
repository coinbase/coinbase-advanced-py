import base64
import json
import unittest
from unittest.mock import patch

import jwt

from coinbase import jwt_generator

from .constants import TEST_API_KEY, TEST_API_SECRET


class JwtGeneratorTest(unittest.TestCase):
    def test_build_rest_jwt(self):
        uri = jwt_generator.format_jwt_uri("GET", "/api/v3/brokerage/accounts")
        result_jwt = jwt_generator.build_rest_jwt(uri, TEST_API_KEY, TEST_API_SECRET)

        decoded_data = jwt.decode(result_jwt, TEST_API_SECRET, algorithms=["ES256"])
        header_bytes = base64.urlsafe_b64decode(str(result_jwt.split(".")[0] + "=="))
        decoded_header = json.loads(header_bytes.decode("utf-8"))

        self.assertEqual(decoded_data["sub"], TEST_API_KEY)
        self.assertEqual(decoded_data["iss"], "cdp")
        self.assertEqual(decoded_data["uri"], uri)
        self.assertEqual(decoded_header["kid"], TEST_API_KEY)

    def test_build_ws_jwt(self):
        result_jwt = jwt_generator.build_ws_jwt(TEST_API_KEY, TEST_API_SECRET)

        decoded_data = jwt.decode(result_jwt, TEST_API_SECRET, algorithms=["ES256"])
        header_bytes = base64.urlsafe_b64decode(str(result_jwt.split(".")[0] + "=="))
        decoded_header = json.loads(header_bytes.decode("utf-8"))

        self.assertEqual(decoded_data["sub"], TEST_API_KEY)
        self.assertEqual(decoded_data["iss"], "cdp")
        self.assertNotIn("uri", decoded_data)
        self.assertEqual(decoded_header["kid"], TEST_API_KEY)

    def test_build_rest_jwt_error(self):
        with self.assertRaises(Exception):
            uri = jwt_generator.format_jwt_uri("GET", "/api/v3/brokerage/accounts")
            jwt_generator.build_rest_jwt(uri, TEST_API_KEY, "bad_secret")

    @patch("coinbase.jwt_generator.jwt.encode", return_value="signed-jwt")
    @patch("coinbase.jwt_generator.serialization.load_pem_private_key")
    def test_build_rest_jwt_with_preparsed_key(
        self, mock_load_private_key, mock_jwt_encode
    ):
        private_key = object()
        uri = jwt_generator.format_jwt_uri("GET", "/api/v3/brokerage/accounts")

        result_jwt = jwt_generator.build_rest_jwt(
            uri, TEST_API_KEY, TEST_API_SECRET, private_key=private_key
        )

        mock_load_private_key.assert_not_called()
        self.assertEqual(result_jwt, "signed-jwt")
        self.assertEqual(mock_jwt_encode.call_args.args[1], private_key)
        self.assertEqual(mock_jwt_encode.call_args.kwargs["algorithm"], "ES256")

    @patch("coinbase.jwt_generator.jwt.encode", return_value="signed-jwt")
    @patch("coinbase.jwt_generator.serialization.load_pem_private_key")
    def test_build_ws_jwt_with_preparsed_key(
        self, mock_load_private_key, mock_jwt_encode
    ):
        private_key = object()

        result_jwt = jwt_generator.build_ws_jwt(
            TEST_API_KEY, TEST_API_SECRET, private_key=private_key
        )

        mock_load_private_key.assert_not_called()
        self.assertEqual(result_jwt, "signed-jwt")
        self.assertEqual(mock_jwt_encode.call_args.args[1], private_key)
        self.assertEqual(mock_jwt_encode.call_args.kwargs["algorithm"], "ES256")
