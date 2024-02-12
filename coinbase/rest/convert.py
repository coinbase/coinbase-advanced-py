from typing import Optional

from coinbase.constants import API_PREFIX


def create_convert_quote(
    self,
    from_account: str,
    to_account: str,
    amount: str,
    user_incentive_id: Optional[str] = None,
    code_val: Optional[str] = None,
    **kwargs,
):
    """
    **Create Convert Quote**
    ________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/convert/quote

    __________

    **Description:**

    Create a convert quote with a specified source currency, target currency, and amount.

    __________

    **Read more on the official documentation:** `Create Convert Quote <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_createconvertquote>`_
    """
    endpoint = f"{API_PREFIX}/convert/quote"

    data = {
        "from_account": from_account,
        "to_account": to_account,
        "amount": amount,
    }

    trade_incentive_metadata = {
        "user_incentive_id": user_incentive_id,
        "code_val": code_val,
    }
    filtered_trade_incentive_metadata = {
        key: value
        for key, value in trade_incentive_metadata.items()
        if value is not None
    }

    if filtered_trade_incentive_metadata:
        data["trade_incentive_metadata"] = filtered_trade_incentive_metadata

    return self.post(endpoint, data=data, **kwargs)


def get_convert_trade(
    self, trade_id: str, from_account: str, to_account: str, **kwargs
):
    """
    **Get Convert Trade**
    _____________________

    [GET] https://api.coinbase.com/api/v3/brokerage/convert/trade/{trade_id}

    __________

    **Description:**

    Gets a list of information about a convert trade with a specified trade ID, source currency, and target currency.

    __________

    **Read more on the official documentation:** `Get Convert Trade <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getconverttrade>`_
    """
    endpoint = f"{API_PREFIX}/convert/trade/{trade_id}"

    params = {
        "from_account": from_account,
        "to_account": to_account,
    }

    return self.get(endpoint, params=params, **kwargs)


def commit_convert_trade(
    self, trade_id: str, from_account: str, to_account: str, **kwargs
):
    """
    **Commit Convert Trade**
    ________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/convert/trade/{trade_id}

    __________

    **Description:**

    Commits a convert trade with a specified trade ID, source currency, and target currency.

    __________

    **Read more on the official documentation:** `Commit Convert Trade <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_commitconverttrade>`_
    """
    endpoint = f"{API_PREFIX}/convert/trade/{trade_id}"

    data = {
        "from_account": from_account,
        "to_account": to_account,
    }

    return self.post(endpoint, data=data, **kwargs)
