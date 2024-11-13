from typing import Any, Dict, List, Optional

from coinbase.rest.types.base_response import BaseResponse
from coinbase.rest.types.common_types import (
    CancelOrderObject,
    Order,
    OrderConfiguration,
)


# Create Order
class CreateOrderResponse(BaseResponse):
    def __init__(self, response: dict):
        if "success" in response:
            self.success: bool = response.pop("success")
        if "failure_reason" in response:
            self.failure_reason: Optional[Dict[str, Any]] = response.pop(
                "failure_reason"
            )
        if "order_id" in response:
            self.order_id: Optional[str] = response.pop("order_id")

        if "success_response" in response:
            self.response: Optional[Dict[str, Any]] = response.pop("success_response")
        elif "error_response" in response:
            self.response: Optional[Dict[str, Any]] = response.pop("error_response")

        if "order_configuration" in response:
            self.order_configuration: Optional[OrderConfiguration] = OrderConfiguration(
                **response.pop("order_configuration")
            )
        super().__init__(**response)


# Cancel Orders
class CancelOrdersResponse(BaseResponse):
    def __init__(self, response: dict):
        if "results" in response:
            self.results: Optional[List[CancelOrderObject]] = [
                CancelOrderObject(**result) for result in response.pop("results")
            ]
        super().__init__(**response)


# Edit Order
class EditOrderResponse(BaseResponse):
    def __init__(self, response: dict):
        if "success" in response:
            self.success: bool = response.pop("success")

        if "success_response" in response:
            self.response: Optional[Dict[str, Any]] = response.pop("success_response")
        elif "error_response" in response:
            self.response: Optional[Dict[str, Any]] = response.pop("error_response")

        if "errors" in response:
            self.errors: Optional[List[Dict[str, Any]]] = response.pop("errors")
        super().__init__(**response)


# Edit Order Preview
class EditOrderPreviewResponse(BaseResponse):
    def __init__(self, response: dict):
        if "errors" in response:
            self.errors: List[Dict[str, Any]] = response.pop("errors")
        if "slippage" in response:
            self.slippage: Optional[str] = response.pop("slippage")
        if "order_total" in response:
            self.order_total: Optional[str] = response.pop("order_total")
        if "commission_total" in response:
            self.commission_total: Optional[str] = response.pop("commission_total")
        if "quote_size" in response:
            self.quote_size: Optional[str] = response.pop("quote_size")
        if "base_size" in response:
            self.base_size: Optional[str] = response.pop("base_size")
        if "best_bid" in response:
            self.best_bid: Optional[str] = response.pop("best_bid")
        if "average_filled_price" in response:
            self.average_filled_price: Optional[str] = response.pop(
                "average_filled_price"
            )
        super().__init__(**response)


# List Orders
class ListOrdersResponse(BaseResponse):
    def __init__(self, response: dict):
        if "orders" in response:
            self.orders: List[Order] = [
                Order(**order) for order in response.pop("orders")
            ]
        if "sequence" in response:
            self.sequence: Optional[int] = response.pop("sequence")
        if "has_next" in response:
            self.has_next: bool = response.pop("has_next")
        if "cursor" in response:
            self.cursor: Optional[str] = response.pop("cursor")
        super().__init__(**response)


# List Fills
class ListFillsResponse(BaseResponse):
    def __init__(self, response: dict):
        if "fills" in response:
            self.fills: Optional[List[Dict[str, Any]]] = response.pop("fills")
        if "cursor" in response:
            self.cursor: Optional[str] = response.pop("cursor")
        super().__init__(**response)


# Get Order
class GetOrderResponse(BaseResponse):
    def __init__(self, response: dict):
        if "order" in response:
            self.order: Optional[Order] = Order(**response.pop("order"))
        super().__init__(**response)


# Preview Order
class PreviewOrderResponse(BaseResponse):
    def __init__(self, response: dict):
        if "order_total" in response:
            self.order_total: str = response.pop("order_total")
        if "commission_total" in response:
            self.commission_total: str = response.pop("commission_total")
        if "errs" in response:
            self.errs: List[Dict[str, Any]] = response.pop("errs")
        if "warning" in response:
            self.warning: List[Dict[str, Any]] = response.pop("warning")
        if "quote_size" in response:
            self.quote_size: str = response.pop("quote_size")
        if "base_size" in response:
            self.base_size: str = response.pop("base_size")
        if "best_bid" in response:
            self.best_bid: str = response.pop("best_bid")
        if "best_ask" in response:
            self.best_ask: str = response.pop("best_ask")
        if "is_max" in response:
            self.is_max: bool = response.pop("is_max")
        if "order_margin_total" in response:
            self.order_margin_total: Optional[str] = response.pop("order_margin_total")
        if "leverage" in response:
            self.leverage: Optional[str] = response.pop("leverage")
        if "long_leverage" in response:
            self.long_leverage: Optional[str] = response.pop("long_leverage")
        if "short_leverage" in response:
            self.short_leverage: Optional[str] = response.pop("short_leverage")
        if "slippage" in response:
            self.slippage: Optional[str] = response.pop("slippage")
        if "preview_id" in response:
            self.preview_id: Optional[str] = response.pop("preview_id")
        if "current_liquidation_buffer" in response:
            self.current_liquidation_buffer: Optional[str] = response.pop(
                "current_liquidation_buffer"
            )
        if "projected_liquidation_buffer" in response:
            self.projected_liquidation_buffer: Optional[str] = response.pop(
                "projected_liquidation_buffer"
            )
        if "max_leverage" in response:
            self.max_leverage: Optional[str] = response.pop("max_leverage")
        if "pnl_configuration" in response:
            self.pnl_configuration: Optional[Dict[str, Any]] = response.pop(
                "pnl_configuration"
            )
        super().__init__(**response)


# Close Position
class ClosePositionResponse(BaseResponse):
    def __init__(self, response: dict):
        if "success" in response:
            self.success: bool = response.pop("success")

        if "success_response" in response:
            self.response: Optional[Dict[str, Any]] = response.pop("success_response")
        elif "error_response" in response:
            self.response: Optional[Dict[str, Any]] = response.pop("error_response")

        if "order_configuration" in response:
            self.order_configuration: Optional[OrderConfiguration] = OrderConfiguration(
                **response.pop("order_configuration")
            )
        super().__init__(**response)
