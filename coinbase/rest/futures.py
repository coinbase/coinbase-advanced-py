from coinbase.constants import API_PREFIX


def get_futures_balance_summary(self, **kwargs):
    """
    Get information on your balances related to Coinbase Financial Markets (CFM) futures trading.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getfcmbalancesummary
    """
    endpoint = f"{API_PREFIX}/cfm/balance_summary"

    return self.get(endpoint, **kwargs)


def list_futures_positions(self, **kwargs):
    """
    Get a list of all open positions in CFM futures products.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getfcmpositions
    """
    endpoint = f"{API_PREFIX}/cfm/positions"

    return self.get(endpoint, **kwargs)


def get_futures_position(self, product_id: str, **kwargs):
    """
    Get the position of a specific CFM futures product.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getfcmposition
    """
    endpoint = f"{API_PREFIX}/cfm/positions/{product_id}"

    return self.get(endpoint, **kwargs)


def schedule_futures_sweep(self, usd_amount: str, **kwargs):
    """
    Schedule a sweep of funds from your CFTC-regulated futures account to your Coinbase Inc. USD Spot wallet.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_schedulefcmsweep
    """
    endpoint = f"{API_PREFIX}/cfm/sweeps/schedule"

    data = {"usd_amount": usd_amount}

    return self.post(endpoint, data=data, **kwargs)


def list_futures_sweeps(self, **kwargs):
    """
    Get information on your pending and/or processing requests to sweep funds from your CFTC-regulated futures account to your Coinbase Inc. USD Spot wallet.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getfcmsweeps
    """
    endpoint = f"{API_PREFIX}/cfm/sweeps"

    return self.get(endpoint, **kwargs)


def cancel_pending_futures_sweep(self, **kwargs):
    """
    Cancel your pending sweep of funds from your CFTC-regulated futures account to your Coinbase Inc. USD Spot wallet.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_cancelfcmsweep
    """
    endpoint = f"{API_PREFIX}/cfm/sweeps"

    return self.delete(endpoint, **kwargs)
