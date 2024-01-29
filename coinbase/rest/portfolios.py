from typing import Optional

from coinbase.constants import API_PREFIX


def get_portfolios(self, portfolio_type: Optional[str] = None, **kwargs):
    """
    Get a list of all portfolios of a user.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getportfolios
    """
    endpoint = f"{API_PREFIX}/portfolios"

    params = {"portfolio_type": portfolio_type}

    return self.get(endpoint, params=params, **kwargs)


def create_portfolio(self, name: str, **kwargs):
    """
    Create a portfolio.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_createportfolio
    """
    endpoint = f"{API_PREFIX}/portfolios"

    data = {
        "name": name,
    }

    return self.post(endpoint, data=data, **kwargs)


def get_portfolio_breakdown(self, portfolio_uuid: str, **kwargs):
    """
    Get the breakdown of a portfolio by portfolio ID.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getportfoliobreakdown
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
    Transfer funds between portfolios.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_moveportfoliofunds
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
    Modify a portfolio by portfolio ID.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_editportfolio
    """
    endpoint = f"{API_PREFIX}/portfolios/{portfolio_uuid}"

    data = {
        "name": name,
    }

    return self.put(endpoint, data=data, **kwargs)


def delete_portfolio(self, portfolio_uuid: str, **kwargs):
    """
    Delete a portfolio by portfolio ID.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_deleteportfolio
    """
    endpoint = f"{API_PREFIX}/portfolios/{portfolio_uuid}"

    return self.delete(endpoint, **kwargs)
