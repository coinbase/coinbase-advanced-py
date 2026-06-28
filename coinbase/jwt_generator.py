import base64
import binascii
import secrets
import time

import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519

from coinbase.constants import BASE_URL


def _load_private_key(secret_var):
    if secret_var.lstrip().startswith("-----BEGIN"):
        return serialization.load_pem_private_key(
            secret_var.encode("utf-8"), password=None
        )

    # join+split strips whitespace so trailing newlines from .env loaders don't break valid keys
    try:
        raw = base64.b64decode("".join(secret_var.split()), validate=True)
    except (binascii.Error, ValueError):
        raise ValueError("private key is neither PEM nor valid base64")
    if len(raw) not in (32, 64):
        raise ValueError(
            f"Ed25519 raw key must decode to 32 or 64 bytes, got {len(raw)}"
        )
    return ed25519.Ed25519PrivateKey.from_private_bytes(raw[:32])


def _algorithm_for(private_key) -> str:
    if isinstance(private_key, ed25519.Ed25519PrivateKey):
        return "EdDSA"
    if isinstance(private_key, ec.EllipticCurvePrivateKey):
        return "ES256"
    raise ValueError(
        f"Unsupported private key type: {type(private_key).__name__}. "
        "Expected ECDSA (P-256) or Ed25519."
    )


def _load_private_key_for_jwt(secret_var):
    try:
        return _load_private_key(secret_var)
    except (ValueError, TypeError) as e:
        raise Exception(
            f"{e}\n"
            "Are you sure you generated your key at https://cloud.coinbase.com/access/api ?"
        )


def build_jwt(key_var, secret_var, uri=None, private_key=None) -> str:
    """
    :meta private:
    """
    private_key = private_key or _load_private_key_for_jwt(secret_var)

    jwt_data = {
        "sub": key_var,
        "iss": "cdp",
        "nbf": int(time.time()),
        "exp": int(time.time()) + 120,
    }

    if uri:
        jwt_data["uri"] = uri

    jwt_token = jwt.encode(
        jwt_data,
        private_key,
        algorithm=_algorithm_for(private_key),
        headers={"kid": key_var, "nonce": secrets.token_hex()},
    )

    return jwt_token


def build_rest_jwt(uri, key_var, secret_var, private_key=None) -> str:
    """
    **Build REST JWT**
    __________

    **Description:**

    Builds and returns a JWT token for connecting to the REST API.

    __________

    Parameters:

    - **uri (str)** - Formatted URI for the endpoint (e.g. "GET api.coinbase.com/api/v3/brokerage/accounts") Can be generated using ``format_jwt_uri``
    - **key_var (str)** - The API key
    - **secret_var (str)** - The API key secret
    """
    return build_jwt(key_var, secret_var, uri=uri, private_key=private_key)


def build_ws_jwt(key_var, secret_var) -> str:
    """
    **Build WebSocket JWT**
    __________

    **Description:**

    Builds and returns a JWT token for connecting to the WebSocket API.

    __________

    Parameters:

    - **key_var (str)** - The API key
    - **secret_var (str)** - The API key secret
    """
    return build_jwt(key_var, secret_var)


def format_jwt_uri(method, path) -> str:
    """
    **Format JWT URI**
    __________

    **Description:**

    Formats method and path into valid URI for JWT generation.

    __________

    Parameters:

    - **method (str)** - The REST request method. E.g. GET, POST, PUT, DELETE
    - **path (str)** - The path of the endpoint. E.g. "/api/v3/brokerage/accounts"

    """
    return f"{method} {BASE_URL}{path}"
