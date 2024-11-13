from typing import Any, Dict, List, Optional

from coinbase.rest.types.base_response import BaseResponse
from coinbase.rest.types.common_types import (
    Candle,
    HistoricalMarketTrade,
    PriceBook,
    Product,
    ProductType,
    ProductVenue,
)


# Get Server Time Response
class GetServerTimeResponse(BaseResponse):
    def __init__(self, response: dict):
        if "iso" in response:
            self.iso: Optional[str] = response.pop("iso")
        if "epochSeconds" in response:
            self.epoch_seconds: Optional[int] = response.pop("epochSeconds")
        if "epochMillis" in response:
            self.epoch_millis: Optional[int] = response.pop("epochMillis")
        super().__init__(**response)


# Get Public Product Book Response
class GetPublicProductBookResponse(BaseResponse):
    def __init__(self, response: dict):
        if "pricebook" in response:
            self.pricebook: PriceBook = PriceBook(**response.pop("pricebook"))
        super().__init__(**response)


# List Public Products Response
class ListPublicProductsResponse(BaseResponse):
    def __init__(self, response: dict):
        if "products" in response:
            self.products: Optional[List[Product]] = [
                Product(**product) for product in response.pop("products")
            ]
        if "num_products" in response:
            self.num_products: Optional[int] = response.pop("num_products")
        super().__init__(**response)


# Get Public Product Response
class GetPublicProductResponse(BaseResponse):
    def __init__(self, response: dict):
        if "product_id" in response:
            self.product_id: str = response.pop("product_id")
        if "price" in response:
            self.price: str = response.pop("price")
        if "price_percentage_change_24h" in response:
            self.price_percentage_change_24h: str = response.pop(
                "price_percentage_change_24h"
            )
        if "volume_24h" in response:
            self.volume_24h: str = response.pop("volume_24h")
        if "volume_percentage_change_24h" in response:
            self.volume_percentage_change_24h: str = response.pop(
                "volume_percentage_change_24h"
            )
        if "base_increment" in response:
            self.base_increment: str = response.pop("base_increment")
        if "quote_increment" in response:
            self.quote_increment: str = response.pop("quote_increment")
        if "quote_min_size" in response:
            self.quote_min_size: str = response.pop("quote_min_size")
        if "quote_max_size" in response:
            self.quote_max_size: str = response.pop("quote_max_size")
        if "base_min_size" in response:
            self.base_min_size: str = response.pop("base_min_size")
        if "base_max_size" in response:
            self.base_max_size: str = response.pop("base_max_size")
        if "base_name" in response:
            self.base_name: str = response.pop("base_name")
        if "quote_name" in response:
            self.quote_name: str = response.pop("quote_name")
        if "watched" in response:
            self.watched: bool = response.pop("watched")
        if "is_disabled" in response:
            self.is_disabled: bool = response.pop("is_disabled")
        if "new" in response:
            self.new: bool = response.pop("new")
        if "status" in response:
            self.status: str = response.pop("status")
        if "cancel_only" in response:
            self.cancel_only: bool = response.pop("cancel_only")
        if "limit_only" in response:
            self.limit_only: bool = response.pop("limit_only")
        if "post_only" in response:
            self.post_only: bool = response.pop("post_only")
        if "trading_disabled" in response:
            self.trading_disabled: bool = response.pop("trading_disabled")
        if "auction_mode" in response:
            self.auction_mode: bool = response.pop("auction_mode")
        if "product_type" in response:
            self.product_type: Optional[ProductType] = response.pop("product_type")
        if "quote_currency_id" in response:
            self.quote_currency_id: Optional[str] = response.pop("quote_currency_id")
        if "base_currency_id" in response:
            self.base_currency_id: Optional[str] = response.pop("base_currency_id")
        if "fcm_trading_session_details" in response:
            self.fcm_trading_session_details: Optional[Dict[str, Any]] = response.pop(
                "fcm_trading_session_details"
            )
        if "mid_market_price" in response:
            self.mid_market_price: Optional[str] = response.pop("mid_market_price")
        if "alias" in response:
            self.alias: Optional[str] = response.pop("alias")
        if "alias_to" in response:
            self.alias_to: Optional[List[str]] = response.pop("alias_to")
        if "base_display_symbol" in response:
            self.base_display_symbol: str = response.pop("base_display_symbol")
        if "quote_display_symbol" in response:
            self.quote_display_symbol: Optional[str] = response.pop(
                "quote_display_symbol"
            )
        if "view_only" in response:
            self.view_only: Optional[bool] = response.pop("view_only")
        if "price_increment" in response:
            self.price_increment: Optional[str] = response.pop("price_increment")
        if "display_name" in response:
            self.display_name: Optional[str] = response.pop("display_name")
        if "product_venue" in response:
            self.product_venue: Optional[ProductVenue] = response.pop("product_venue")
        if "approximate_quote_24h_volume" in response:
            self.approximate_quote_24h_volume: Optional[str] = response.pop(
                "approximate_quote_24h_volume"
            )
        if "future_product_details" in response:
            self.future_product_details: Optional[Dict[str, Any]] = response.pop(
                "future_product_details"
            )
        super().__init__(**response)


# Get Public Product Candles Response
class GetPublicProductCandlesResponse(BaseResponse):
    def __init__(self, response: dict):
        if "candles" in response:
            self.candles: Optional[List[Candle]] = [
                Candle(**candle) for candle in response.pop("candles")
            ]
        super().__init__(**response)


# Get Public Market Trades Response
class GetPublicMarketTradesResponse(BaseResponse):
    def __init__(self, response: dict):
        if "trades" in response:
            self.trades: Optional[List[HistoricalMarketTrade]] = [
                HistoricalMarketTrade(**trade) for trade in response.pop("trades")
            ]
        if "best_bid" in response:
            self.best_bid: Optional[str] = response.pop("best_bid")
        if "best_ask" in response:
            self.best_ask: Optional[str] = response.pop("best_ask")
        super().__init__(**response)
