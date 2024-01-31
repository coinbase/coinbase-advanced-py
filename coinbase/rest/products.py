from typing import List, Optional

from coinbase.constants import API_PREFIX


def get_products(
    self,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    product_type: Optional[str] = None,
    product_ids: Optional[List[str]] = None,
    contract_expiry_type: Optional[str] = None,
    expiring_contract_status: Optional[str] = None,
    **kwargs,
):
    """
    Get a list of the available currency pairs for trading.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getproducts
    """
    endpoint = f"{API_PREFIX}/products"

    params = {
        "limit": limit,
        "offset": offset,
        "product_type": product_type,
        "product_ids": product_ids,
        "contract_expiry_type": contract_expiry_type,
        "expiring_contract_status": expiring_contract_status,
    }

    return self.get(endpoint, params=params, **kwargs)


def get_product(self, product_id: str, **kwargs):
    """
    Get information on a single product by product ID.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getproduct
    """
    endpoint = f"{API_PREFIX}/products/{product_id}"

    return self.get(endpoint, **kwargs)


def get_product_book(self, product_id: str, limit: Optional[int] = None, **kwargs):
    """
    Get a list of bids/asks for a single product. The amount of detail shown can be customized with the limit parameter.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getproductbook
    """
    endpoint = f"{API_PREFIX}/product_book"

    params = {"product_id": product_id, "limit": limit}

    return self.get(endpoint, params=params, **kwargs)


def get_best_bid_ask(self, product_ids: Optional[List[str]] = None, **kwargs):
    """
    Get the best bid/ask for all products. A subset of all products can be returned instead by using the product_ids
    input.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getbestbidask
    """
    endpoint = f"{API_PREFIX}/best_bid_ask"

    params = {
        "product_ids": product_ids,
    }

    return self.get(endpoint, params=params, **kwargs)
