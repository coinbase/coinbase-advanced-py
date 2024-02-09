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
    **List Products**
    _________________

    [GET] https://api.coinbase.com/api/v3/brokerage/products

    __________

    **Description:**

    Get a list of the available currency pairs for trading.

    __________

    **Read more on the official documentation:** `List Products
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getproducts>`_
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
    **Get Product**
    _______________

    [GET] https://api.coinbase.com/api/v3/brokerage/products/{product_id}

    __________

    **Description:**

    Get information on a single product by product ID.

    __________

    **Read more on the official documentation:** `Get Product
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getproduct>`_
    """
    endpoint = f"{API_PREFIX}/products/{product_id}"

    return self.get(endpoint, **kwargs)


def get_product_book(self, product_id: str, limit: Optional[int] = None, **kwargs):
    """
    **Get Product Book**
    ____________________

    [GET] https://api.coinbase.com/api/v3/brokerage/product_book

    __________

    **Description:**

    Get a list of bids/asks for a single product. The amount of detail shown can be customized with the limit parameter.

    __________

    **Read more on the official documentation:** `Get Product Book
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getproductbook>`_
    """
    endpoint = f"{API_PREFIX}/product_book"

    params = {"product_id": product_id, "limit": limit}

    return self.get(endpoint, params=params, **kwargs)


def get_best_bid_ask(self, product_ids: Optional[List[str]] = None, **kwargs):
    """
    **Get Best Bid/Ask**
    ____________________

    [GET] https://api.coinbase.com/api/v3/brokerage/best_bid_ask

    __________

    **Description:**

    Get the best bid/ask for all products. A subset of all products can be returned instead by using the product_ids input.

    __________

    **Read more on the official documentation:** `Get Best Bid/Ask
    <https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getproductbook>`_
    """
    endpoint = f"{API_PREFIX}/best_bid_ask"

    params = {
        "product_ids": product_ids,
    }

    return self.get(endpoint, params=params, **kwargs)
