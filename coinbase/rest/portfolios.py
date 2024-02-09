from typing import Optional

from coinbase.constants import API_PREFIX


def get_portfolios(self, portfolio_type: Optional[str] = None, **kwargs):
    """
    **List Portfolios**
    ___________________

    [GET] https://api.coinbase.com/api/v3/brokerage/portfolios

    __________

    **Description:**

    Get a list of all portfolios of a user.

    __________

    **Read more on the official documentation:** `List Portfolios
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getportfolios>`_
    """
    endpoint = f"{API_PREFIX}/portfolios"

    params = {"portfolio_type": portfolio_type}

    return self.get(endpoint, params=params, **kwargs)


def create_portfolio(self, name: str, **kwargs):
    """
    **Create Portfolio**
    ____________________

    [POST] https://api.coinbase.com/api/v3/brokerage/portfolios

    __________

    **Description:**

    Create a portfolio.

    __________

    **Read more on the official documentation:** `Create Portfolio
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_createportfolio>`_
    """
    endpoint = f"{API_PREFIX}/portfolios"

    data = {
        "name": name,
    }

    return self.post(endpoint, data=data, **kwargs)


def get_portfolio_breakdown(self, portfolio_uuid: str, **kwargs):
    """
    **Get Portfolio Breakdown**
    ___________________________

    [GET] https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}

    __________

    **Description:**

    Get the breakdown of a portfolio by portfolio ID.

    __________

    **Read more on the official documentation:** `Get Portfolio Breakdown
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getportfoliobreakdown>`_
    """
    endpoint = f"{API_PREFIX}/portfolios/{portfolio_uuid}"

    return self.get(endpoint, **kwargs)


def move_portfolio_funds(
    self,
    value: str,
    currency: str,
    source_portfolio_uuid: str,
    target_portfolio_uuid: str,
    **kwargs,
):
    """
    **Move Portfolio Funds**
    ________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/portfolios/move_funds

    __________

    **Description:**

    Transfer funds between portfolios.

    __________

    **Read more on the official documentation:** `Move Portfolio Funds
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_moveportfoliofunds>`_
    """
    endpoint = f"{API_PREFIX}/portfolios/move_funds"

    data = {
        "funds": {
            "value": value,
            "currency": currency,
        },
        "source_portfolio_uuid": source_portfolio_uuid,
        "target_portfolio_uuid": target_portfolio_uuid,
    }

    return self.post(endpoint, data=data, **kwargs)


def edit_portfolio(self, portfolio_uuid: str, name: str, **kwargs):
    """
    **Edit Portfolio**
    __________________

    [PUT] https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}

    __________

    **Description:**

    Modify a portfolio by portfolio ID.

    __________

    **Read more on the official documentation:** `Edit Portfolio
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_editportfolio>`_
    """
    endpoint = f"{API_PREFIX}/portfolios/{portfolio_uuid}"

    data = {
        "name": name,
    }

    return self.put(endpoint, data=data, **kwargs)


def delete_portfolio(self, portfolio_uuid: str, **kwargs):
    """
    **Delete Portfolio**
    ____________________

    [DELETE] https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}

    __________

    **Description:**

    Delete a portfolio by portfolio ID.

    __________

    **Read more on the official documentation:** `Delete Portfolio
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_deleteportfolio>`_
    """
    endpoint = f"{API_PREFIX}/portfolios/{portfolio_uuid}"

    return self.delete(endpoint, **kwargs)
