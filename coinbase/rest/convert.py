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
    Create a convert quote with a specified source currency, target currency, and amount.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_createconvertquote
    """
    endpoint = f"{API_PREFIX}/convert/quote"

    data = {
        "from_account": from_account,
        "to_account": to_account,
        "amount": amount,
        "trade_incentive_metadata": {
            "user_incentive_id": user_incentive_id,
            "code_val": code_val,
        },
    }

    if kwargs:
        data.update(kwargs)

    return self.post(endpoint, data=data)


def get_convert_trade(
    self, trade_id: str, from_account: str, to_account: str, **kwargs
):
    """
    Gets a list of information about a convert trade with a specified trade ID, source currency, and target currency.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getconverttrade
    """
    endpoint = f"{API_PREFIX}/convert/trade/{trade_id}"

    params = {
        "from_account": from_account,
        "to_account": to_account,
    }

    if kwargs:
        params.update(kwargs)

    return self.get(endpoint, params=params)


def commit_convert_trade(
    self, trade_id: str, from_account: str, to_account: str, **kwargs
):
    """
    Commits a convert trade with a specified trade ID, source currency, and target currency.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_commitconverttrade
    """
    endpoint = f"{API_PREFIX}/convert/trade/{trade_id}"

    data = {
        "from_account": from_account,
        "to_account": to_account,
    }

    if kwargs:
        data.update(kwargs)

    return self.post(endpoint, data=data)
