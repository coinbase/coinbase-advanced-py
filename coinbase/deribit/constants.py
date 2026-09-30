# Deribit Retail gateway — derivatives surface.
# Spot stays on api.coinbase.com via the existing RESTClient; these point at the
# Coinbase-operated Deribit gateway (drb.coinbase.com), not Deribit directly.
DERIBIT_REST_BASE_URL = "drb.coinbase.com"
DERIBIT_REST_API_PREFIX = "/api/v2"
DERIBIT_WS_URL = "wss://drb.coinbase.com/ws/api/v2"
DERIBIT_STREAM_WS_URL = "wss://streams.drb.coinbase.com/ws/api/v2"

# Named environments the clients accept via environment=. Only "production" exists
# today; the parameter stays so a sandbox can be added without an API change.
DERIBIT_ENVIRONMENTS = {
    "production": {
        "rest_base_url": DERIBIT_REST_BASE_URL,
        "ws_url": DERIBIT_WS_URL,
        "stream_ws_url": DERIBIT_STREAM_WS_URL,
    },
}


def resolve_environment(environment: str) -> dict:
    try:
        return DERIBIT_ENVIRONMENTS[environment]
    except KeyError:
        raise ValueError(
            f"unknown environment {environment!r}; "
            f"expected one of {sorted(DERIBIT_ENVIRONMENTS)}"
        )


def select_environment(environment: str) -> dict:
    """Resolve an environment name to its gateway hosts.

    :meta private:
    """
    return resolve_environment(environment)


# WebSocket
DERIBIT_WS_CALL_TIMEOUT = 30  # default seconds to block on a JSON-RPC reply
DERIBIT_REST_TIMEOUT = 30  # default seconds for REST and public/auth HTTP requests
DERIBIT_WS_OPEN_TIMEOUT = 10
DERIBIT_WS_RETRY_MAX = 5  # reconnect attempts before giving up
DERIBIT_WS_RETRY_BASE = 1.0  # initial backoff seconds
DERIBIT_WS_RETRY_FACTOR = 2.0
DERIBIT_WS_RETRY_CAP = 30.0

# Auth — CDP JWT exchanged once at public/auth for a short-lived access_token.
DERIBIT_AUTH_METHOD = "public/auth"
GRANT_TYPE_CDP = "coinbase_cdp"
# Re-auth proactively at this fraction of expires_in (15-min token -> ~12 min).
DERIBIT_TOKEN_REFRESH_RATIO = 0.8
