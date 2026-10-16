import logging
import os
from typing import Any, Optional, Type

import requests

from coinbase.api_base import APIBase, get_logger
from coinbase.constants import API_ENV_KEY, API_SECRET_ENV_KEY, USER_AGENT
from coinbase.deribit._generated.rest_methods import GeneratedRESTMixin
from coinbase.deribit._model import DeribitModel
from coinbase.deribit.auth.token_cache import DeribitAuth
from coinbase.deribit.constants import (
    DERIBIT_REST_API_PREFIX,
    DERIBIT_REST_TIMEOUT,
    select_environment,
)
from coinbase.deribit.errors import (
    TOKEN_REJECTED_CODES,
    DeribitRPCError,
    rpc_error_from,
)

logger = get_logger("coinbase.deribit.RESTClient")


class DeribitRetailClient(APIBase, GeneratedRESTMixin):
    """Synchronous REST client for the Deribit Retail gateway (drb.coinbase.com).

    A convenience surface over HTTP; ``DeribitRetailWSClient`` is the primary
    transport. Every Deribit RPC method is a typed method on this class (mixed in
    from the generated layer); each forwards to :meth:`_rpc`, which handles the
    JSON-RPC envelope, bearer auth for private methods, and error mapping.

    Authenticates with the same CDP keys as the spot RESTClient (Ed25519 or ECDSA),
    exchanging a CDP JWT at public/auth for a short-lived access_token that is
    refreshed automatically.
    """

    def __init__(
        self,
        api_key: Optional[str] = os.getenv(API_ENV_KEY),
        api_secret: Optional[str] = os.getenv(API_SECRET_ENV_KEY),
        key_file: Optional[Any] = None,
        environment: str = "production",
        base_url: Optional[str] = None,
        api_prefix: str = DERIBIT_REST_API_PREFIX,
        timeout: Optional[int] = DERIBIT_REST_TIMEOUT,
        verbose: bool = False,
    ) -> None:
        # environment picks the gateway host; an explicit base_url overrides it.
        if base_url is None:
            base_url = select_environment(environment)["rest_base_url"]
        super().__init__(
            api_key=api_key,
            api_secret=api_secret,
            key_file=key_file,
            base_url=base_url,
            timeout=timeout,
            verbose=verbose,
        )
        if verbose:
            logger.setLevel(logging.DEBUG)

        self._api_prefix = api_prefix
        self._endpoint = f"https://{base_url}{api_prefix}"
        self._session = requests.Session()
        self._auth: Optional[DeribitAuth] = None
        if self.is_authenticated:
            self._auth = DeribitAuth(
                self.api_key,
                self.api_secret,
                base_url=base_url,
                api_prefix=api_prefix,
                session=self._session,
                timeout=timeout,
            )

    def _rpc(
        self,
        method: str,
        params: dict,
        model_cls: Optional[Type[DeribitModel]] = None,
    ):
        """Send one JSON-RPC call and return the parsed response.

        Returns ``model_cls(envelope)`` when the method has a typed response (access
        the payload via ``.result``), otherwise the raw response dict. Raises a
        :class:`DeribitRPCError` subclass on a JSON-RPC error.

        If the gateway rejects the access token of a private call (it did not run),
        the token is refreshed and the call is retried once.

        :meta private:
        """
        params = {k: v for k, v in params.items() if v is not None}
        is_private = method.startswith("private/")
        if is_private and self._auth is None:
            raise DeribitRPCError(
                13009,
                f"{method} is a private method but the client is unauthenticated. "
                "Provide api_key/api_secret or key_file.",
            )
        try:
            payload = self._post(method, params, is_private, force_refresh=False)
        except DeribitRPCError as e:
            if not (is_private and e.code in TOKEN_REJECTED_CODES):
                raise
            logger.debug("Deribit %s: token rejected, refreshing and retrying", method)
            payload = self._post(method, params, is_private, force_refresh=True)

        if model_cls is not None:
            return model_cls(payload)
        return payload

    def _post(
        self, method: str, params: dict, is_private: bool, force_refresh: bool
    ) -> dict:
        headers = {
            "User-Agent": USER_AGENT,
            "Content-Type": "application/json",
        }
        if is_private:
            # Bearer header (not params.access_token) so the token never lands in a
            # logged request body.
            token = self._auth.get_access_token(force_refresh=force_refresh)
            headers["Authorization"] = f"Bearer {token}"

        url = f"{self._endpoint}/{method}"
        body = {"jsonrpc": "2.0", "method": method, "params": params}
        logger.debug("Deribit RPC %s", method)

        response = self._session.post(
            url, json=body, headers=headers, timeout=self.timeout
        )
        try:
            payload = response.json()
        except ValueError:
            response.raise_for_status()
            raise DeribitRPCError(response.status_code, response.text)
        if not isinstance(payload, dict):
            response.raise_for_status()
            raise DeribitRPCError(
                response.status_code, "unexpected non-object JSON-RPC response"
            )

        if payload.get("error"):
            raise rpc_error_from(payload["error"])
        response.raise_for_status()
        return payload

    def call(self, method: str, params: Optional[dict] = None):
        """Escape hatch: invoke any Deribit method by name with a raw params dict.

        Returns the raw response dict. Use the typed methods for the documented
        surface; this covers anything not yet wrapped.
        """
        return self._rpc(method, params or {}, None)
