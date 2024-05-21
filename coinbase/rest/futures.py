from typing import Any, Dict, Optional

from coinbase.constants import API_PREFIX


def close_position(
    self, client_order_id: str, product_id: str, size: Optional[str] = None, **kwargs
) -> Dict[str, Any]:
    """
    **Close Position**
    _________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/close_position

    __________

    **Description:**

    Places an order to close any open positions for a specified ``product_id``.

    __________

    **Read more on the official documentation:** `Close Position
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_closeposition>`_
    """
    endpoint = f"{API_PREFIX}/orders/close_position"
    data = {"client_order_id": client_order_id, "product_id": product_id, "size": size}

    return self.post(endpoint, data=data, **kwargs)


def get_futures_balance_summary(self, **kwargs) -> Dict[str, Any]:
    """
    **Get Futures Balance Summary**
    _______________________________

    [GET] https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary

    __________

    **Description:**

    Get information on your balances related to `Coinbase Financial Markets <https://www.coinbase.com/fcm>`_ (CFM) futures trading.

    __________

    **Read more on the official documentation:** `Get Futures Balance Summary
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getfcmbalancesummary>`_
    """
    endpoint = f"{API_PREFIX}/cfm/balance_summary"

    return self.get(endpoint, **kwargs)


def list_futures_positions(self, **kwargs) -> Dict[str, Any]:
    """
    **List Futures Positions**
    __________________________

    [GET] https://api.coinbase.com/api/v3/brokerage/cfm/positions

    __________

    **Description:**

    Get a list of all open positions in CFM futures products.

    __________

    **Read more on the official documentation:** `List Futures Positions
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getfcmpositions>`_
    """
    endpoint = f"{API_PREFIX}/cfm/positions"

    return self.get(endpoint, **kwargs)


def get_futures_position(self, product_id: str, **kwargs) -> Dict[str, Any]:
    """
    **Get Futures Position**
    _________________________

    [GET] https://api.coinbase.com/api/v3/brokerage/cfm/positions/{product_id}

    __________

    **Description:**

    Get the position of a specific CFM futures product.

    __________

    **Read more on the official documentation:** `Get Futures Position
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getfcmposition>`_
    """
    endpoint = f"{API_PREFIX}/cfm/positions/{product_id}"

    return self.get(endpoint, **kwargs)


def schedule_futures_sweep(self, usd_amount: str, **kwargs) -> Dict[str, Any]:
    """
    **Schedule Futures Sweep**
    __________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/cfm/sweeps/schedule

    __________

    **Description:**

    Schedule a sweep of funds from your CFTC-regulated futures account to your Coinbase Inc. USD Spot wallet.

    __________

    **Read more on the official documentation:** `Schedule Futures Sweep
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_schedulefcmsweep>`_
    """
    endpoint = f"{API_PREFIX}/cfm/sweeps/schedule"

    data = {"usd_amount": usd_amount}

    return self.post(endpoint, data=data, **kwargs)


def list_futures_sweeps(self, **kwargs) -> Dict[str, Any]:
    """
    **List Futures Sweeps**
    _______________________

    [GET] https://api.coinbase.com/api/v3/brokerage/cfm/sweeps

    __________

    **Description:**

    Get information on your pending and/or processing requests to sweep funds from your CFTC-regulated futures account to your Coinbase Inc. USD Spot wallet.

    __________

    **Read more on the official documentation:** `List Futures Sweeps
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getfcmsweeps>`_
    """
    endpoint = f"{API_PREFIX}/cfm/sweeps"

    return self.get(endpoint, **kwargs)


def cancel_pending_futures_sweep(self, **kwargs) -> Dict[str, Any]:
    """
    **Cancel Pending Futures Sweep**
    ________________________________

    [DELETE] https://api.coinbase.com/api/v3/brokerage/cfm/sweeps

    __________

    **Description:**

    Cancel your pending sweep of funds from your CFTC-regulated futures account to your Coinbase Inc. USD Spot wallet.

    __________

    **Read more on the official documentation:** `Cancel Pending Futures Sweep
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_cancelfcmsweep>`_
    """
    endpoint = f"{API_PREFIX}/cfm/sweeps"

    return self.delete(endpoint, **kwargs)


def get_intraday_margin_setting(self, **kwargs) -> Dict[str, Any]:
    """
    **Get Intraday Margin Setting**
    _______________________________

    [GET] https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting

    __________

    **Description:**

    Get the status of whether your account is opted in to receive increased leverage on futures trades on weekdays from 8am-4pm ET.

    __________

    **Read more on the official documentation:** `Get Intraday Margin Setting
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getintradaymarginsetting>`_
    """
    endpoint = f"{API_PREFIX}/cfm/intraday/margin_setting"

    return self.get(endpoint, **kwargs)


def get_current_margin_window(
    self, margin_profile_type: str, **kwargs
) -> Dict[str, Any]:
    """
    **Get Current Margin Window**
    ________________________________

    [GET] https://api.coinbase.com/api/v3/brokerage/cfm/intraday/current_margin_window

    __________

    **Description:**

    Get the current margin window to determine whether intraday or overnight margin rates are in effect.

    __________

    **Read more on the official documentation:** `Get Current Margin Window
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getcurrentmarginwindow>`_
    """

    endpoint = f"{API_PREFIX}/cfm/intraday/current_margin_window"

    params = {"margin_profile_type": margin_profile_type}

    return self.get(endpoint, params=params, **kwargs)


def set_intraday_margin_setting(self, setting: str, **kwargs) -> Dict[str, Any]:
    """
    **Set Intraday Margin Setting**
    ________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting

    __________

    **Description:**

    Opt in to receive increased leverage on futures trades on weekdays from 8am-4pm ET.

    __________

    **Read more on the official documentation:** `Set Intraday Margin Setting
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_setintradaymarginsetting>`_
    """

    endpoint = f"{API_PREFIX}/cfm/intraday/margin_setting"

    data = {"setting": setting}

    return self.post(endpoint, data=data, **kwargs)
