from coinbase.constants import API_PREFIX


def get_futures_balance_summary(self, **kwargs):
    """
    **Get Futures Balance Summary**
    _______________________________

    [GET] https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary

    __________

    **Description:**

    Get information on your balances related to `Coinbase Financial Markets <https://www.coinbase.com/fcm>`_ (CFM) futures trading.

    __________

    **Read more on the official documentation:** `Get Futures Balance Summary
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getfcmbalancesummary>`_
    """
    endpoint = f"{API_PREFIX}/cfm/balance_summary"

    return self.get(endpoint, **kwargs)


def list_futures_positions(self, **kwargs):
    """
    **List Futures Positions**
    __________________________

    [GET] https://api.coinbase.com/api/v3/brokerage/cfm/positions

    __________

    **Description:**

    Get a list of all open positions in CFM futures products.

    __________

    **Read more on the official documentation:** `List Futures Positions
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getfcmpositions>`_
    """
    endpoint = f"{API_PREFIX}/cfm/positions"

    return self.get(endpoint, **kwargs)


def get_futures_position(self, product_id: str, **kwargs):
    """
    **Get Futures Position**
    _________________________

    [GET] https://api.coinbase.com/api/v3/brokerage/cfm/positions/{product_id}

    __________

    **Description:**

    Get the position of a specific CFM futures product.

    __________

    **Read more on the official documentation:** `Get Futures Position
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getfcmposition>`_
    """
    endpoint = f"{API_PREFIX}/cfm/positions/{product_id}"

    return self.get(endpoint, **kwargs)


def schedule_futures_sweep(self, usd_amount: str, **kwargs):
    """
    **Schedule Futures Sweep**
    __________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/cfm/sweeps/schedule

    __________

    **Description:**

    Schedule a sweep of funds from your CFTC-regulated futures account to your Coinbase Inc. USD Spot wallet.

    __________

    **Read more on the official documentation:** `Schedule Futures Sweep
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_schedulefcmsweep>`_
    """
    endpoint = f"{API_PREFIX}/cfm/sweeps/schedule"

    data = {"usd_amount": usd_amount}

    return self.post(endpoint, data=data, **kwargs)


def list_futures_sweeps(self, **kwargs):
    """
    **List Futures Sweeps**
    _______________________

    [GET] https://api.coinbase.com/api/v3/brokerage/cfm/sweeps

    __________

    **Description:**

    Get information on your pending and/or processing requests to sweep funds from your CFTC-regulated futures account to your Coinbase Inc. USD Spot wallet.

    __________

    **Read more on the official documentation:** `List Futures Sweeps
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getfcmsweeps>`_
    """
    endpoint = f"{API_PREFIX}/cfm/sweeps"

    return self.get(endpoint, **kwargs)


def cancel_pending_futures_sweep(self, **kwargs):
    """
    **Cancel Pending Futures Sweep**
    ________________________________

    [DELETE] https://api.coinbase.com/api/v3/brokerage/cfm/sweeps

    __________

    **Description:**

    Cancel your pending sweep of funds from your CFTC-regulated futures account to your Coinbase Inc. USD Spot wallet.

    __________

    **Read more on the official documentation:** `Cancel Pending Futures Sweep
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_cancelfcmsweep>`_
    """
    endpoint = f"{API_PREFIX}/cfm/sweeps"

    return self.delete(endpoint, **kwargs)
