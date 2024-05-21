from typing import Any, Dict, Optional

from coinbase.constants import API_PREFIX


def get_accounts(
    self,
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **List Accounts**
    _________________
    [GET] https://api.coinbase.com/api/v3/brokerage/accounts

    __________

    **Description:**

    Get a list of authenticated accounts for the current user.

    __________

    **Read more on the official documentation:** `List Accounts <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getaccounts>`_

    """
    endpoint = f"{API_PREFIX}/accounts"
    params = {
        "limit": limit,
        "cursor": cursor,
        "retail_portfolio_id": retail_portfolio_id,
    }

    return self.get(endpoint, params=params, **kwargs)


def get_account(self, account_uuid: str, **kwargs) -> Dict[str, Any]:
    """

    **Get Account**
    _______________
    [GET] https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid}

    __________

    **Description:**

    Get a list of information about an account, given an account UUID.

    __________

    **Read more on the official documentation:** `Get Account <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getaccount>`_
    """
    endpoint = f"{API_PREFIX}/accounts/{account_uuid}"

    return self.get(endpoint, **kwargs)
