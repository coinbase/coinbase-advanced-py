import base64
import json
import unittest

import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from coinbase import jwt_generator

from .constants import (
    TEST_API_KEY,
    TEST_API_SECRET,
    TEST_ED25519_API_SECRET,
    TEST_ED25519_PKCS8_API_SECRET,
    TEST_ED25519_SEED_API_SECRET,
)


def _decode_header(token):
    header_bytes = base64.urlsafe_b64decode(str(token.split(".")[0] + "=="))
    return json.loads(header_bytes.decode("utf-8"))


def _ed25519_public_key(secret):
    # independent of _load_private_key to avoid circular test coverage
    if secret.lstrip().startswith("-----BEGIN"):
        return serialization.load_pem_private_key(
            secret.encode(), password=None
        ).public_key()
    raw = base64.b64decode("".join(secret.split()))
    return Ed25519PrivateKey.from_private_bytes(raw[:32]).public_key()


class JwtGeneratorTest(unittest.TestCase):
    def test_build_rest_jwt(self):
        uri = jwt_generator.format_jwt_uri("GET", "/api/v3/brokerage/accounts")
        result_jwt = jwt_generator.build_rest_jwt(uri, TEST_API_KEY, TEST_API_SECRET)

        decoded_data = jwt.decode(result_jwt, TEST_API_SECRET, algorithms=["ES256"])
        decoded_header = _decode_header(result_jwt)

        self.assertEqual(decoded_data["sub"], TEST_API_KEY)
        self.assertEqual(decoded_data["iss"], "cdp")
        self.assertEqual(decoded_data["uri"], uri)
        self.assertEqual(decoded_header["kid"], TEST_API_KEY)
        self.assertEqual(decoded_header["alg"], "ES256")

    def test_build_ws_jwt(self):
        result_jwt = jwt_generator.build_ws_jwt(TEST_API_KEY, TEST_API_SECRET)

        decoded_data = jwt.decode(result_jwt, TEST_API_SECRET, algorithms=["ES256"])
        decoded_header = _decode_header(result_jwt)

        self.assertEqual(decoded_data["sub"], TEST_API_KEY)
        self.assertEqual(decoded_data["iss"], "cdp")
        self.assertNotIn("uri", decoded_data)
        self.assertEqual(decoded_header["kid"], TEST_API_KEY)
        self.assertEqual(decoded_header["alg"], "ES256")

    def test_build_rest_jwt_error(self):
        with self.assertRaises(Exception):
            uri = jwt_generator.format_jwt_uri("GET", "/api/v3/brokerage/accounts")
            jwt_generator.build_rest_jwt(uri, TEST_API_KEY, "bad_secret")

    def test_malformed_pem_raises_clearly(self):
        bad_pem = "-----BEGIN EC PRIVATE KEY-----\nNOTVALIDDATA\n-----END EC PRIVATE KEY-----\n"
        with self.assertRaises(Exception) as ctx:
            jwt_generator._load_private_key(bad_pem)
        self.assertNotIn("neither PEM nor valid base64", str(ctx.exception))

    def test_wrong_length_base64_raises(self):
        import base64 as b64

        for n in (31, 33, 65):
            bad = b64.b64encode(bytes(n)).decode()
            with self.assertRaises(ValueError, msg=f"{n} bytes should raise"):
                jwt_generator._load_private_key(bad)

    def test_invalid_base64_raises(self):
        with self.assertRaises(Exception):
            jwt_generator._load_private_key("not-valid-base64!!!")

    def test_whitespace_padded_ed25519_accepted(self):
        padded = TEST_ED25519_SEED_API_SECRET + "\n"
        key = jwt_generator._load_private_key(padded)
        self.assertIsInstance(key, Ed25519PrivateKey)

    def test_build_rest_jwt_ed25519(self):
        uri = jwt_generator.format_jwt_uri("GET", "/api/v3/brokerage/accounts")
        result_jwt = jwt_generator.build_rest_jwt(
            uri, TEST_API_KEY, TEST_ED25519_API_SECRET
        )

        public_key = _ed25519_public_key(TEST_ED25519_API_SECRET)
        decoded_data = jwt.decode(result_jwt, public_key, algorithms=["EdDSA"])
        decoded_header = _decode_header(result_jwt)

        self.assertEqual(decoded_data["sub"], TEST_API_KEY)
        self.assertEqual(decoded_data["iss"], "cdp")
        self.assertEqual(decoded_data["uri"], uri)
        self.assertEqual(decoded_header["kid"], TEST_API_KEY)
        self.assertEqual(decoded_header["alg"], "EdDSA")

    def test_build_ws_jwt_ed25519(self):
        result_jwt = jwt_generator.build_ws_jwt(TEST_API_KEY, TEST_ED25519_API_SECRET)

        public_key = _ed25519_public_key(TEST_ED25519_API_SECRET)
        decoded_data = jwt.decode(result_jwt, public_key, algorithms=["EdDSA"])
        decoded_header = _decode_header(result_jwt)

        self.assertEqual(decoded_data["sub"], TEST_API_KEY)
        self.assertEqual(decoded_data["iss"], "cdp")
        self.assertNotIn("uri", decoded_data)
        self.assertEqual(decoded_header["kid"], TEST_API_KEY)
        self.assertEqual(decoded_header["alg"], "EdDSA")

    def test_build_rest_jwt_ed25519_pkcs8(self):
        uri = jwt_generator.format_jwt_uri("GET", "/api/v3/brokerage/accounts")
        result_jwt = jwt_generator.build_rest_jwt(
            uri, TEST_API_KEY, TEST_ED25519_PKCS8_API_SECRET
        )

        public_key = _ed25519_public_key(TEST_ED25519_PKCS8_API_SECRET)
        decoded_data = jwt.decode(result_jwt, public_key, algorithms=["EdDSA"])
        decoded_header = _decode_header(result_jwt)

        self.assertEqual(decoded_data["sub"], TEST_API_KEY)
        self.assertEqual(decoded_data["iss"], "cdp")
        self.assertEqual(decoded_data["uri"], uri)
        self.assertEqual(decoded_header["kid"], TEST_API_KEY)
        self.assertEqual(decoded_header["alg"], "EdDSA")

    def test_build_ws_jwt_ed25519_pkcs8(self):
        result_jwt = jwt_generator.build_ws_jwt(
            TEST_API_KEY, TEST_ED25519_PKCS8_API_SECRET
        )

        public_key = _ed25519_public_key(TEST_ED25519_PKCS8_API_SECRET)
        decoded_data = jwt.decode(result_jwt, public_key, algorithms=["EdDSA"])
        decoded_header = _decode_header(result_jwt)

        self.assertEqual(decoded_data["sub"], TEST_API_KEY)
        self.assertEqual(decoded_data["iss"], "cdp")
        self.assertNotIn("uri", decoded_data)
        self.assertEqual(decoded_header["kid"], TEST_API_KEY)
        self.assertEqual(decoded_header["alg"], "EdDSA")

    def test_build_rest_jwt_ed25519_seed(self):
        uri = jwt_generator.format_jwt_uri("GET", "/api/v3/brokerage/accounts")
        result_jwt = jwt_generator.build_rest_jwt(
            uri, TEST_API_KEY, TEST_ED25519_SEED_API_SECRET
        )

        public_key = _ed25519_public_key(TEST_ED25519_SEED_API_SECRET)
        decoded_data = jwt.decode(result_jwt, public_key, algorithms=["EdDSA"])
        decoded_header = _decode_header(result_jwt)

        self.assertEqual(decoded_data["sub"], TEST_API_KEY)
        self.assertEqual(decoded_data["iss"], "cdp")
        self.assertEqual(decoded_data["uri"], uri)
        self.assertEqual(decoded_header["kid"], TEST_API_KEY)
        self.assertEqual(decoded_header["alg"], "EdDSA")

    def test_build_ws_jwt_ed25519_seed(self):
        result_jwt = jwt_generator.build_ws_jwt(
            TEST_API_KEY, TEST_ED25519_SEED_API_SECRET
        )

        public_key = _ed25519_public_key(TEST_ED25519_SEED_API_SECRET)
        decoded_data = jwt.decode(result_jwt, public_key, algorithms=["EdDSA"])
        decoded_header = _decode_header(result_jwt)

        self.assertEqual(decoded_data["sub"], TEST_API_KEY)
        self.assertEqual(decoded_data["iss"], "cdp")
        self.assertNotIn("uri", decoded_data)
        self.assertEqual(decoded_header["kid"], TEST_API_KEY)
        self.assertEqual(decoded_header["alg"], "EdDSA")
