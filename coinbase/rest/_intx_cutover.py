import logging
from contextlib import contextmanager
from typing import Iterator, Optional

from requests.exceptions import HTTPError

PERP_PRODUCT_SUFFIX = "-PERP-INTX"

# Same logger (and handler) that rest_base configures for HTTP errors.
logger = logging.getLogger("coinbase.RESTClient")


def is_intx_perp_product(product_id) -> bool:
    """
    :meta private:
    """
    return isinstance(product_id, str) and product_id.upper().endswith(
        PERP_PRODUCT_SUFFIX
    )


def intx_migration_hint_message(method: str, replacement: Optional[str]) -> str:
    """
    :meta private:
    """
    if replacement:
        hint = (
            f"Use {replacement} on coinbase.deribit.DeribitRetailClient "
            f"or DeribitRetailWSClient instead."
        )
    else:
        hint = "There is no Deribit Retail replacement for this call yet."
    return (
        f"{method}() failed. From October 1, 2026, Global Derivatives run on the "
        f"Deribit-powered gateway at drb.coinbase.com instead of INTX. {hint}"
    )


@contextmanager
def intx_migration_hint(
    method: str, replacement: Optional[str] = None, enabled: bool = True
) -> Iterator[None]:
    """
    Send the request unchanged. If the server rejects it, log a migration hint
    and re-raise the original :class:`HTTPError`.

    :meta private:
    """
    try:
        yield
    except HTTPError:
        if enabled:
            logger.error(intx_migration_hint_message(method, replacement))
        raise
