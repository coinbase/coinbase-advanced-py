from typing import Any, Dict, Optional

from coinbase.constants import API_PREFIX


def get_api_key_permissions(
    self,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Get Api Key Permissions**
    _____________________________

    [GET] https://api.coinbase.com/api/v3/brokerage/key_permissions

    __________

    **Description:**

    Get information about your CDP API key permissions

    __________

    **Read more on the official documentation:** `Create Convert Quote <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getapikeypermissions>`_
    """
    endpoint = f"{API_PREFIX}/key_permissions"

    return self.get(endpoint, **kwargs)
