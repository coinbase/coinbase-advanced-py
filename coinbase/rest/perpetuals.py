from typing import Optional

from coinbase.constants import API_PREFIX


def allocate_portfolio(
    self, portfolio_uuid: str, symbol: str, amount: str, currency: str, **kwargs
):
    """
    Allocate more funds to an isolated position in your Perpetuals portfolio.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_allocateportfolio
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
    Get a summary of your Perpetuals portfolio.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getintxportfoliosummary
    """
    endpoint = f"{API_PREFIX}/intx/portfolio/{portfolio_uuid}"

    return self.get(endpoint, **kwargs)


def list_perps_positions(self, portfolio_uuid: str, **kwargs):
    """
    Get a list of open positions in your Perpetuals portfolio.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getintxpositions
    """
    endpoint = f"{API_PREFIX}/intx/positions/{portfolio_uuid}"

    return self.get(endpoint, **kwargs)


def get_perps_position(self, portfolio_uuid: str, symbol: str, **kwargs):
    """
    Get a specific open position in your Perpetuals portfolio

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getintxposition
    """
    endpoint = f"{API_PREFIX}/intx/positions/{portfolio_uuid}/{symbol}"

    return self.get(endpoint, **kwargs)
