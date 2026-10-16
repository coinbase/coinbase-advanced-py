import threading
import time
from typing import Optional

import requests

from coinbase.api_base import get_logger
from coinbase.constants import USER_AGENT
from coinbase.deribit.auth.cdp_jwt import build_cdp_jwt
from coinbase.deribit.constants import (
    DERIBIT_AUTH_METHOD,
    DERIBIT_REST_API_PREFIX,
    DERIBIT_REST_BASE_URL,
    DERIBIT_REST_TIMEOUT,
    DERIBIT_TOKEN_REFRESH_RATIO,
    GRANT_TYPE_CDP,
)
from coinbase.deribit.errors import DeribitAuthError, redact_secrets

logger = get_logger("coinbase.deribit.auth")


def build_auth_params(api_key: str, api_secret: str) -> dict:
    """JSON-RPC ``params`` for a public/auth coinbase_cdp exchange.

    Shared by the HTTP token cache and the WS in-band re-auth, which sign a fresh
    CDP JWT each time rather than reusing a cached token.

    :meta private:
    """
    return {"grant_type": GRANT_TYPE_CDP, "token": build_cdp_jwt(api_key, api_secret)}


class DeribitAuth:
    """Manages the HTTP access_token: exchanges a CDP JWT at public/auth and keeps
    the returned token fresh.

    The CDP JWT is sent in the JSON-RPC body (not the query string) so the
    credential never lands in a URL or access log. The returned access_token is
    held in memory only — never persisted, never logged — and refreshed proactively
    once it passes ``refresh_ratio`` of its lifetime.
    """

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        base_url: str = DERIBIT_REST_BASE_URL,
        api_prefix: str = DERIBIT_REST_API_PREFIX,
        session: Optional[requests.Session] = None,
        timeout: Optional[int] = DERIBIT_REST_TIMEOUT,
        refresh_ratio: float = DERIBIT_TOKEN_REFRESH_RATIO,
    ) -> None:
        self._api_key = api_key
        self._api_secret = api_secret
        self._auth_url = f"https://{base_url}{api_prefix}/{DERIBIT_AUTH_METHOD}"
        self._session = session or requests.Session()
        self._timeout = timeout
        self._refresh_ratio = refresh_ratio

        self._lock = threading.Lock()
        self._access_token: Optional[str] = None
        self._refresh_at = 0.0  # monotonic deadline; 0 forces a first exchange

    def get_access_token(self, force_refresh: bool = False) -> str:
        """Return a valid access_token, exchanging or refreshing if needed."""
        with self._lock:
            if force_refresh or self._needs_refresh():
                self._exchange()
            return self._access_token

    def _needs_refresh(self) -> bool:
        return self._access_token is None or time.monotonic() >= self._refresh_at

    def _exchange(self) -> None:
        body = {
            "jsonrpc": "2.0",
            "method": DERIBIT_AUTH_METHOD,
            "params": build_auth_params(self._api_key, self._api_secret),
        }
        try:
            resp = self._session.post(
                self._auth_url,
                json=body,
                headers={
                    "User-Agent": USER_AGENT,
                    "Content-Type": "application/json",
                },
                timeout=self._timeout,
            )
        except requests.RequestException as e:
            raise DeribitAuthError(
                f"public/auth request failed: {redact_secrets(e)}"
            ) from None

        try:
            payload = resp.json()
        except ValueError:
            payload = None
        err = payload.get("error") if isinstance(payload, dict) else None
        if err:
            raise DeribitAuthError(
                f"public/auth rejected (HTTP {resp.status_code}): "
                f"[{err.get('code')}] {redact_secrets(err.get('message'))}"
            )
        if resp.status_code != 200:
            raise DeribitAuthError(f"public/auth returned status {resp.status_code}")
        if not isinstance(payload, dict):
            raise DeribitAuthError("public/auth returned an unexpected response")

        result = payload.get("result") or {}
        token = result.get("access_token")
        expires_in = result.get("expires_in")
        if not token or not expires_in:
            raise DeribitAuthError("public/auth response missing access_token")

        self._access_token = token
        self._refresh_at = time.monotonic() + expires_in * self._refresh_ratio
        logger.debug("Deribit access_token refreshed (expires_in=%ss)", expires_in)
