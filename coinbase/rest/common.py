from typing import Any, Dict

from coinbase.constants import API_PREFIX


def get_unix_time(self, **kwargs) -> Dict[str, Any]:
    """
    **Get Server Time**
    _________________
    [GET] https://api.coinbase.com/api/v3/brokerage/time

    __________

    **Description:**

    Get the current time from the Coinbase Advanced API. This is a public endpoint.

    __________

    **Read more on the official documentation:** `Get Server Time <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getservertime>`_
    """

    endpoint = f"{API_PREFIX}/time"

    return self.get(endpoint, public=True, **kwargs)
