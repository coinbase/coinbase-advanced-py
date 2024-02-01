import secrets
import time

import jwt
from cryptography.hazmat.primitives import serialization

from coinbase.constants import BASE_URL, REST_SERVICE, WS_SERVICE


def build_jwt(key_var, secret_var, service, uri=None):
    try:
        private_key_bytes = secret_var.encode("utf-8")
        private_key = serialization.load_pem_private_key(
            private_key_bytes, password=None
        )
    except ValueError as e:
        # This handles errors like incorrect key format
        raise Exception(
            f"{e}\n"
            "Are you sure you generated your key at https://cloud.coinbase.com/access/api ?"
        )

    jwt_data = {
        "sub": key_var,
        "iss": "coinbase-cloud",
        "nbf": int(time.time()),
        "exp": int(time.time()) + 120,
        "aud": [service],
    }

    if uri:
        jwt_data["uri"] = uri

    jwt_token = jwt.encode(
        jwt_data,
        private_key,
        algorithm="ES256",
        headers={"kid": key_var, "nonce": secrets.token_hex()},
    )

    return jwt_token


def build_rest_jwt(uri, key_var, secret_var):
    return build_jwt(key_var, secret_var, REST_SERVICE, uri=uri)


def build_ws_jwt(key_var, secret_var):
    return build_jwt(key_var, secret_var, WS_SERVICE)


def format_jwt_uri(method, path):
    return f"{method} {BASE_URL}{path}"
