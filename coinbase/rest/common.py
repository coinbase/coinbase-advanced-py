from coinbase.constants import API_PREFIX


def get_unix_time(self, **kwargs):
    """
    **Get UNIX Time**
    _________________
    [GET] https://api.coinbase.com/api/v3/brokerage/time

    __________

    **Description:**

    Get the current time from the Coinbase Advanced API.

    __________

    **Read more on the official documentation:** `Get UNIX Time <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getunixtime>`_
    """
    endpoint = f"{API_PREFIX}/time"

    return self.get(endpoint, **kwargs)
