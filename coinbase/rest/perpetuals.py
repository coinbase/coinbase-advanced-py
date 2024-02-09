from typing import Optional

from coinbase.constants import API_PREFIX


def allocate_portfolio(
    self, portfolio_uuid: str, symbol: str, amount: str, currency: str, **kwargs
):
    """
    **Allocate Portfolio**
    ________________

    [POST] https://api.coinbase.com/api/v3/brokerage/intx/allocate

    __________

    **Description:**

    Allocate more funds to an isolated position in your Perpetuals portfolio.

    __________

    **Read more on the official documentation:** `Allocate Portfolio
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_allocateportfolio>`_
    """

    endpoint = f"{API_PREFIX}/intx/allocate"

    data = {
        "portfolio_uuid": portfolio_uuid,
        "symbol": symbol,
        "amount": amount,
        "currency": currency,
    }

    return self.post(endpoint, data=data, **kwargs)


def get_perps_portfolio_summary(self, portfolio_uuid: str, **kwargs):
    """
    **Get Perpetuals Portfolio Summary**
    ________________

    [GET] https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid}

    __________

    **Description:**

    Get a summary of your Perpetuals portfolio.

    __________

    **Read more on the official documentation:** `Get Perpetuals Portfolio Summary
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getintxportfoliosummary>`_
    """
    endpoint = f"{API_PREFIX}/intx/portfolio/{portfolio_uuid}"

    return self.get(endpoint, **kwargs)


def list_perps_positions(self, portfolio_uuid: str, **kwargs):
    """
    **List Perpetuals Positions**
    ________________

    [GET] https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}

    __________

    **Description:**

    Get a list of open positions in your Perpetuals portfolio.

    __________

    **Read more on the official documentation:** `List Perpetuals Positions
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getintxpositions>`_
    """
    endpoint = f"{API_PREFIX}/intx/positions/{portfolio_uuid}"

    return self.get(endpoint, **kwargs)


def get_perps_position(self, portfolio_uuid: str, symbol: str, **kwargs):
    """
    **Get Perpetuals Position**
    ________________

    [GET] https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}/{symbol}

    __________

    **Description:**

    Get a specific open position in your Perpetuals portfolio

    __________

    **Read more on the official documentation:** `Get Perpetuals Positions
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getintxposition>`_
    """
    endpoint = f"{API_PREFIX}/intx/positions/{portfolio_uuid}/{symbol}"

    return self.get(endpoint, **kwargs)
