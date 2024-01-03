from typing import Optional

from coinbase.constants import API_PREFIX


def get_accounts(
    self, limit: Optional[int] = None, cursor: Optional[str] = None, **kwargs
):
    """
    Get a list of authenticated accounts for the current user.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getaccounts
    """
    endpoint = f"{API_PREFIX}/accounts"
    params = {"limit": limit, "cursor": cursor}

    return self.get(endpoint, params=params, **kwargs)


def get_account(self, account_uuid: str, **kwargs):
    """
    Get a list of information about an account, given an account UUID.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getaccount
    """
    endpoint = f"{API_PREFIX}/accounts/{account_uuid}"

    return self.get(endpoint, **kwargs)
