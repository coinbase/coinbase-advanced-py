from coinbase.constants import API_PREFIX


def get_unix_time(self, **kwargs):
    """
    Get the current time from the Coinbase Advanced API.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getunixtime
    """
    endpoint = f"{API_PREFIX}/time"

    params = {}
    if kwargs:
        params.update(kwargs)

    return self.get(endpoint, params=params)
