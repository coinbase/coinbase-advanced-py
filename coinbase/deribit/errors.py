import re
from typing import Optional

# Deribit JSON-RPC error codes we special-case. Everything else falls back to the
# base DeribitRPCError carrying the raw code + message. The SDK never retries an
# RPC error on the caller's behalf; retry policy belongs to the caller.
RATE_LIMIT_CODE = 10028
MATCHING_QUEUE_FULL_CODE = 10047
INSUFFICIENT_FUNDS_CODE = 10009
INVALID_PARAMS_CODE = 11030
JSONRPC_INVALID_PARAMS_CODE = -32602  # what the gateway returns for bad params

# Codes the gateway returns when an access token is rejected before the request
# runs. The REST client refreshes the token and retries once on these.
TOKEN_REJECTED_CODES = frozenset({13004, 13009})  # invalid_credentials, unauthorized

# JWT-shaped strings (three base64url segments). Gateway error text is copied into
# exceptions and logs; if it ever echoes a credential, this keeps it out.
_JWT_LIKE = re.compile(r"[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}")


def redact_secrets(text) -> str:
    """Replace JWT-like substrings with ``<redacted>``.

    :meta private:
    """
    return _JWT_LIKE.sub("<redacted>", str(text))


class DeribitRPCError(Exception):
    """A JSON-RPC ``error`` object returned by the Deribit gateway."""

    def __init__(self, code: int, message: str, data: Optional[dict] = None) -> None:
        self.code = code
        self.message = message
        self.data = data
        super().__init__(f"[{code}] {message}")


class DeribitRateLimitError(DeribitRPCError):
    """Code 10028 — too many requests."""

    def __init__(self, code: int, message: str, data: Optional[dict] = None) -> None:
        super().__init__(code, message, data)
        retry_after = None
        if isinstance(data, dict):
            # Deribit surfaces a cool-down hint here when present.
            retry_after = data.get("retry_after") or data.get("retry_after_ms")
        self.retry_after = retry_after


class DeribitMatchingQueueFullError(DeribitRPCError):
    """Code 10047 — matching engine queue is full; safe to retry with backoff."""


class DeribitInsufficientFundsError(DeribitRPCError):
    """Code 10009 (and variants) — not enough funds."""


class DeribitInvalidParamsError(DeribitRPCError):
    """Code 11030 or JSON-RPC -32602 — invalid arguments."""


_CODE_TO_CLASS = {
    RATE_LIMIT_CODE: DeribitRateLimitError,
    MATCHING_QUEUE_FULL_CODE: DeribitMatchingQueueFullError,
    INSUFFICIENT_FUNDS_CODE: DeribitInsufficientFundsError,
    INVALID_PARAMS_CODE: DeribitInvalidParamsError,
    JSONRPC_INVALID_PARAMS_CODE: DeribitInvalidParamsError,
}


def rpc_error_from(error: dict) -> DeribitRPCError:
    """Build the most specific DeribitRPCError subclass for a JSON-RPC error object.

    :meta private:
    """
    code = error.get("code", 0)
    message = error.get("message", "")
    data = error.get("data")
    cls = _CODE_TO_CLASS.get(code, DeribitRPCError)
    return cls(code, message, data)


class DeribitAuthError(Exception):
    """Auth pipeline failure (token exchange/refresh) — not a Deribit RPC error."""


class DeribitConnectionError(Exception):
    """WS disconnect while a call was pending. Writes are never auto-resent."""


class DeribitSubscriptionError(Exception):
    """The gateway did not subscribe some of the requested channels.

    The gateway answers a subscribe with the channels it accepted and silently
    drops the rest. Market-data channels are only served on the streams host
    (an unauthenticated :class:`DeribitRetailWSClient`); ``user.*`` channels only
    on the trading host (an authenticated one). Accepted channels stay subscribed.

    - **rejected** - channels that were not subscribed.
    - **accepted** - channels that were subscribed.
    """

    def __init__(self, rejected, accepted, hint: str = "") -> None:
        self.rejected = list(rejected)
        self.accepted = list(accepted)
        message = f"gateway did not subscribe: {', '.join(self.rejected)}"
        super().__init__(f"{message}. {hint}".strip() if hint else message)
