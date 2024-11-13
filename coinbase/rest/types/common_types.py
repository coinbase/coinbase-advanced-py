from enum import Enum
from typing import Any, Dict, List, Optional

from coinbase.rest.types.base_response import BaseResponse


class ProductVenue(Enum):
    UNKNOWN = "UNKNOWN_VENUE_TYPE"
    CBE = "CBE"
    FCM = "FCM"
    INTX = "INTX"


class StopDirection(Enum):
    UP = "UP"
    DOWN = "DOWN"


class MarginType(Enum):
    CROSS = "CROSS"
    ISOLATED = "ISOLATED"


class OrderPlacementSource(Enum):
    UNKNOWN = "UNKNOWN_PLACEMENT_SOURCE"
    RETAIL_SIMPLE = "RETAIL_SIMPLE"
    RETAIL_ADVANCED = "RETAIL_ADVANCED"


class ProductType(Enum):
    UNKNOWN = "UNKNOWN_PRODUCT_TYPE"
    SPOT = "SPOT"
    FUTURE = "FUTURE"


class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


class PortfolioType(Enum):
    UNDEFINED = "UNDEFINED"
    DEFAULT = "DEFAULT"
    CONSUMER = "CONSUMER"
    INTX = "INTX"


class IntradayMarginSetting(Enum):
    UNSPECIFIED = "INTRADAY_MARGIN_SETTING_UNSPECIFIED"
    STANDARD = "INTRADAY_MARGIN_SETTING_STANDARD"
    INTRADAY = "INTRADAY_MARGIN_SETTING_INTRADAY"


class Account(BaseResponse):
    def __init__(self, **kwargs):
        if "uuid" in kwargs:
            self.uuid: Optional[str] = kwargs.pop("uuid")
        if "name" in kwargs:
            self.name: Optional[str] = kwargs.pop("name")
        if "currency" in kwargs:
            self.currency: Optional[str] = kwargs.pop("currency")
        if "available_balance" in kwargs:
            self.available_balance: Optional[Dict[str, Any]] = kwargs.pop(
                "available_balance"
            )
        if "default" in kwargs:
            self.default: Optional[bool] = kwargs.pop("default")
        if "active" in kwargs:
            self.active: Optional[bool] = kwargs.pop("active")
        if "created_at" in kwargs:
            self.created_at: Optional[str] = kwargs.pop("created_at")
        if "updated_at" in kwargs:
            self.updated_at: Optional[str] = kwargs.pop("updated_at")
        if "deleted_at" in kwargs:
            self.deleted_at: Optional[str] = kwargs.pop("deleted_at")
        if "type" in kwargs:
            self.type: Optional[Dict[str, Any]] = kwargs.pop("type")
        if "ready" in kwargs:
            self.ready: Optional[bool] = kwargs.pop("ready")
        if "hold" in kwargs:
            self.hold: Optional[Dict[str, Any]] = kwargs.pop("hold")
        if "retail_portfolio_id" in kwargs:
            self.retail_portfolio_id: Optional[str] = kwargs.pop("retail_portfolio_id")
        super().__init__(**kwargs)


class RatConvertTrade(BaseResponse):
    def __init__(self, **kwargs):
        if "id" in kwargs:
            self.id: Optional[str] = kwargs.pop("id")
        if "status" in kwargs:
            self.status: Optional[Dict[str, Any]] = kwargs.pop("status")
        if "user_entered_amount" in kwargs:
            self.user_entered_amount: Optional[Dict[str, Any]] = kwargs.pop(
                "user_entered_amount"
            )
        if "amount" in kwargs:
            self.amount: Optional[Dict[str, Any]] = kwargs.pop("amount")
        if "subtotal" in kwargs:
            self.subtotal: Optional[Dict[str, Any]] = kwargs.pop("subtotal")
        if "total" in kwargs:
            self.total: Optional[Dict[str, Any]] = kwargs.pop("total")
        if "fees" in kwargs:
            self.fees: Optional[Dict[str, Any]] = kwargs.pop("fees")
        if "total_fee" in kwargs:
            self.total_fee: Optional[Dict[str, Any]] = kwargs.pop("total_fee")
        if "source" in kwargs:
            self.source: Optional[Dict[str, Any]] = kwargs.pop("source")
        if "target" in kwargs:
            self.target: Optional[Dict[str, Any]] = kwargs.pop("target")
        if "unit_price" in kwargs:
            self.unit_price: Optional[Dict[str, Any]] = kwargs.pop("unit_price")
        if "user_warnings" in kwargs:
            self.user_warnings: Optional[Dict[str, Any]] = kwargs.pop("user_warnings")
        if "user_reference" in kwargs:
            self.user_reference: Optional[str] = kwargs.pop("user_reference")
        if "source_curency" in kwargs:
            self.source_curency: Optional[str] = kwargs.pop("source_curency")
        if "cancellation_reason" in kwargs:
            self.cancellation_reason: Optional[Dict[str, Any]] = kwargs.pop(
                "cancellation_reason"
            )
        if "source_id" in kwargs:
            self.source_id: Optional[str] = kwargs.pop("source_id")
        if "target_id" in kwargs:
            self.target_id: Optional[str] = kwargs.pop("target_id")
        if "subscription_info" in kwargs:
            self.subscription_info: Optional[Dict[str, Any]] = kwargs.pop(
                "subscription_info"
            )
        if "exchange_rate" in kwargs:
            self.exchange_rate: Optional[Dict[str, Any]] = kwargs.pop("exchange_rate")
        if "tax_details" in kwargs:
            self.tax_details: Optional[Dict[str, Any]] = kwargs.pop("tax_details")
        if "trade_incentive_info" in kwargs:
            self.trade_incentive_info: Optional[Dict[str, Any]] = kwargs.pop(
                "trade_incentive_info"
            )
        if "total_fee_without_tax" in kwargs:
            self.total_fee_without_tax: Optional[Dict[str, Any]] = kwargs.pop(
                "total_fee_without_tax"
            )
        if "fiat_denoted_total" in kwargs:
            self.fiat_denoted_total: Optional[Dict[str, Any]] = kwargs.pop(
                "fiat_denoted_total"
            )
        super().__init__(**kwargs)


class FCMBalanceSummary(BaseResponse):
    def __init__(self, **kwargs):
        if "futures_buying_power" in kwargs:
            self.futures_buying_power: Optional[Dict[str, Any]] = kwargs.pop(
                "futures_buying_power"
            )
        if "total_usd_balance" in kwargs:
            self.total_usd_balance: Optional[Dict[str, Any]] = kwargs.pop(
                "total_usd_balance"
            )
        if "cbi_usd_balance" in kwargs:
            self.cbi_usd_balance: Optional[Dict[str, Any]] = kwargs.pop(
                "cbi_usd_balance"
            )
        if "cfm_usd_balance" in kwargs:
            self.cfm_usd_balance: Optional[Dict[str, Any]] = kwargs.pop(
                "cfm_usd_balance"
            )
        if "total_open_orders_hold_amount" in kwargs:
            self.total_open_orders_hold_amount: Optional[Dict[str, Any]] = kwargs.pop(
                "total_open_orders_hold_amount"
            )
        if "unrealized_pnl" in kwargs:
            self.unrealized_pnl: Optional[Dict[str, Any]] = kwargs.pop("unrealized_pnl")
        if "daily_realized_pnl" in kwargs:
            self.daily_realized_pnl: Optional[Dict[str, Any]] = kwargs.pop(
                "daily_realized_pnl"
            )
        if "initial_margin" in kwargs:
            self.initial_margin: Optional[Dict[str, Any]] = kwargs.pop("initial_margin")
        if "available_margin" in kwargs:
            self.available_margin: Optional[Dict[str, Any]] = kwargs.pop(
                "available_margin"
            )
        if "liquidation_threshold" in kwargs:
            self.liquidation_threshold: Optional[Dict[str, Any]] = kwargs.pop(
                "liquidation_threshold"
            )
        if "liquidation_buffer_amount" in kwargs:
            self.liquidation_buffer_amount: Optional[Dict[str, Any]] = kwargs.pop(
                "liquidation_buffer_amount"
            )
        if "liquidation_buffer_percentage" in kwargs:
            self.liquidation_buffer_percentage: Optional[str] = kwargs.pop(
                "liquidation_buffer_percentage"
            )
        if "intraday_margin_window_measure" in kwargs:
            self.intraday_margin_window_measure: Optional[Dict[str, Any]] = kwargs.pop(
                "intraday_margin_window_measure"
            )
        if "overnight_margin_window_measure" in kwargs:
            self.overnight_margin_window_measure: Optional[Dict[str, Any]] = kwargs.pop(
                "overnight_margin_window_measure"
            )
        super().__init__(**kwargs)


class FCMPosition(BaseResponse):
    def __init__(self, **kwargs):
        if "product_id" in kwargs:
            self.product_id: Optional[str] = kwargs.pop("product_id")
        if "expiration_time" in kwargs:
            self.expiration_time: Optional[Dict[str, Any]] = kwargs.pop(
                "expiration_time"
            )
        if "side" in kwargs:
            self.side: Optional[Dict[str, Any]] = kwargs.pop("side")
        if "number_of_contracts" in kwargs:
            self.number_of_contracts: Optional[str] = kwargs.pop("number_of_contracts")
        if "current_price" in kwargs:
            self.current_price: Optional[str] = kwargs.pop("current_price")
        if "avg_entry_price" in kwargs:
            self.avg_entry_price: Optional[str] = kwargs.pop("avg_entry_price")
        if "unrealized_pnl" in kwargs:
            self.unrealized_pnl: Optional[str] = kwargs.pop("unrealized_pnl")
        if "daily_realized_pnl" in kwargs:
            self.daily_realized_pnl: Optional[str] = kwargs.pop("daily_realized_pnl")
        super().__init__(**kwargs)


class FCMSweep(BaseResponse):
    def __init__(self, **kwargs):
        if "id" in kwargs:
            self.id: str = kwargs.pop("id")
        if "requested_amount" in kwargs:
            self.requested_amount: Dict[str, Any] = kwargs.pop("requested_amount")
        if "should_sweep_all" in kwargs:
            self.should_sweep_all: bool = kwargs.pop("should_sweep_all")
        if "status" in kwargs:
            self.status: Dict[str, Any] = kwargs.pop("status")
        if "schedule_time" in kwargs:
            self.schedule_time: Dict[str, Any] = kwargs.pop("schedule_time")

        super().__init__(**kwargs)


class CancelOrderObject(BaseResponse):
    def __init__(self, **kwargs):
        if "success" in kwargs:
            self.success: bool = kwargs.pop("success")
        if "failure_reason" in kwargs:
            self.failure_reason: Dict[str, Any] = kwargs.pop("failure_reason")
        if "order_id" in kwargs:
            self.order_id: str = kwargs.pop("order_id")
        super().__init__(**kwargs)


class MarketMarketIoc(BaseResponse):
    def __init__(self, **kwargs):
        if "quote_size" in kwargs:
            self.quote_size: str = kwargs.pop("quote_size")
        if "base_size" in kwargs:
            self.base_size: str = kwargs.pop("base_size")
        super().__init__(**kwargs)


class SorLimitIoc(BaseResponse):
    def __init__(self, **kwargs):
        if "base_size" in kwargs:
            self.base_size: str = kwargs.pop("base_size")
        if "limit_price" in kwargs:
            self.limit_price: str = kwargs.pop("limit_price")
        super().__init__(**kwargs)


class LimitLimitGtc(BaseResponse):
    def __init__(self, **kwargs):
        if "base_size" in kwargs:
            self.base_size: str = kwargs.pop("base_size")
        if "limit_price" in kwargs:
            self.limit_price: str = kwargs.pop("limit_price")
        if "post_only" in kwargs:
            self.post_only: bool = kwargs.pop("post_only")
        super().__init__(**kwargs)


class LimitLimitGtd(BaseResponse):
    def __init__(self, **kwargs):
        if "base_size" in kwargs:
            self.base_size: str = kwargs.pop("base_size")
        if "limit_price" in kwargs:
            self.limit_price: str = kwargs.pop("limit_price")
        if "end_time" in kwargs:
            self.end_time: str = kwargs.pop("end_time")
        if "post_only" in kwargs:
            self.post_only: bool = kwargs.pop("post_only")
        super().__init__(**kwargs)


class LimitLimitFok(BaseResponse):
    def __init__(self, **kwargs):
        if "base_size" in kwargs:
            self.base_size: str = kwargs.pop("base_size")
        if "limit_price" in kwargs:
            self.limit_price: str = kwargs.pop("limit_price")
        super().__init__(**kwargs)


class StopLimitStopLimitGtc(BaseResponse):
    def __init__(self, **kwargs):
        if "base_size" in kwargs:
            self.base_size: str = kwargs.pop("base_size")
        if "limit_price" in kwargs:
            self.limit_price: str = kwargs.pop("limit_price")
        if "stop_price" in kwargs:
            self.stop_price: str = kwargs.pop("stop_price")
        if "stop_direction" in kwargs:
            self.stop_direction: StopDirection = kwargs.pop("stop_direction")
        super().__init__(**kwargs)


class StopLimitStopLimitGtd(BaseResponse):
    def __init__(self, **kwargs):
        if "base_size" in kwargs:
            self.base_size: str = kwargs.pop("base_size")
        if "limit_price" in kwargs:
            self.limit_price: str = kwargs.pop("limit_price")
        if "stop_price" in kwargs:
            self.stop_price: str = kwargs.pop("stop_price")
        if "end_time" in kwargs:
            self.end_time: str = kwargs.pop("end_time")
        if "stop_direction" in kwargs:
            self.stop_direction: StopDirection = kwargs.pop("stop_direction")

        super().__init__(**kwargs)


class TriggerBracketGtc(BaseResponse):
    def __init__(self, **kwargs):
        if "base_size" in kwargs:
            self.base_size: str = kwargs.pop("base_size")
        if "limit_price" in kwargs:
            self.limit_price: str = kwargs.pop("limit_price")
        if "stop_trigger_price" in kwargs:
            self.stop_trigger_price: str = kwargs.pop("stop_trigger_price")
        super().__init__(**kwargs)


class TriggerBracketGtd(BaseResponse):
    def __init__(self, **kwargs):
        if "base_size" in kwargs:
            self.base_size: str = kwargs.pop("base_size")
        if "limit_price" in kwargs:
            self.limit_price: str = kwargs.pop("limit_price")
        if "stop_trigger_price" in kwargs:
            self.stop_trigger_price: str = kwargs.pop("stop_trigger_price")
        if "end_time" in kwargs:
            self.end_time: str = kwargs.pop("end_time")

        super().__init__(**kwargs)


class OrderConfiguration(BaseResponse):
    def __init__(self, **kwargs):
        if "market_market_ioc" in kwargs:
            self.market_market_ioc: Optional[MarketMarketIoc] = MarketMarketIoc(
                **kwargs.pop("market_market_ioc")
            )
        if "sor_limit_ioc" in kwargs:
            self.sor_limit_ioc: Optional[SorLimitIoc] = SorLimitIoc(
                **kwargs.pop("sor_limit_ioc")
            )
        if "limit_limit_gtc" in kwargs:
            self.limit_limit_gtc: Optional[LimitLimitGtc] = LimitLimitGtc(
                **kwargs.pop("limit_limit_gtc")
            )
        if "limit_limit_gtd" in kwargs:
            self.limit_limit_gtd: Optional[LimitLimitGtd] = LimitLimitGtd(
                **kwargs.pop("limit_limit_gtd")
            )
        if "limit_limit_fok" in kwargs:
            self.limit_limit_fok: Optional[LimitLimitFok] = LimitLimitFok(
                **kwargs.pop("limit_limit_fok")
            )
        if "stop_limit_stop_limit_gtc" in kwargs:
            self.stop_limit_stop_limit_gtc: Optional[StopLimitStopLimitGtc] = (
                StopLimitStopLimitGtc(**kwargs.pop("stop_limit_stop_limit_gtc"))
            )
        if "stop_limit_stop_limit_gtd" in kwargs:
            self.stop_limit_stop_limit_gtd: Optional[StopLimitStopLimitGtd] = (
                StopLimitStopLimitGtd(**kwargs.pop("stop_limit_stop_limit_gtd"))
            )
        if "trigger_bracket_gtc" in kwargs:
            self.trigger_bracket_gtc: Optional[TriggerBracketGtc] = TriggerBracketGtc(
                **kwargs.pop("trigger_bracket_gtc")
            )

        if "trigger_bracket_gtd" in kwargs:
            self.trigger_bracket_gtd: Optional[TriggerBracketGtd] = TriggerBracketGtd(
                **kwargs.pop("trigger_bracket_gtd")
            )
        super().__init__(**kwargs)


class Order(BaseResponse):
    def __init__(self, **kwargs):
        if "order_id" in kwargs:
            self.order_id: str = kwargs.pop("order_id")
        if "product_id" in kwargs:
            self.product_id: str = kwargs.pop("product_id")
        if "user_id" in kwargs:
            self.user_id: str = kwargs.pop("user_id")
        if "order_configuration" in kwargs:
            self.order_configuration: OrderConfiguration = OrderConfiguration(
                **kwargs.pop("order_configuration")
            )
        if "side" in kwargs:
            self.side: OrderSide = kwargs.pop("side")
        if "client_order_id" in kwargs:
            self.client_order_id: str = kwargs.pop("client_order_id")
        if "status" in kwargs:
            self.status: Dict[str, Any] = kwargs.pop("status")
        if "time_in_force" in kwargs:
            self.time_in_force: Optional[Dict[str, Any]] = kwargs.pop("time_in_force")
        if "created_time" in kwargs:
            self.created_time: Dict[str, Any] = kwargs.pop("created_time")
        if "completion_percentage" in kwargs:
            self.completion_percentage: str = kwargs.pop("completion_percentage")
        if "filled_size" in kwargs:
            self.filled_size: Optional[str] = kwargs.pop("filled_size")
        if "average_filled_price" in kwargs:
            self.average_filled_price: str = kwargs.pop("average_filled_price")
        if "fee" in kwargs:
            self.fee: Optional[str] = kwargs.pop("fee")
        if "number_of_fills" in kwargs:
            self.number_of_fills: str = kwargs.pop("number_of_fills")
        if "filled_value" in kwargs:
            self.filled_value: Optional[str] = kwargs.pop("filled_value")
        if "pending_cancel" in kwargs:
            self.pending_cancel: bool = kwargs.pop("pending_cancel")
        if "size_in_quote" in kwargs:
            self.size_in_quote: bool = kwargs.pop("size_in_quote")
        if "total_fees" in kwargs:
            self.total_fees: str = kwargs.pop("total_fees")
        if "size_inclusive_of_fees" in kwargs:
            self.size_inclusive_of_fees: bool = kwargs.pop("size_inclusive_of_fees")
        if "total_value_after_fees" in kwargs:
            self.total_value_after_fees: str = kwargs.pop("total_value_after_fees")
        if "trigger_status" in kwargs:
            self.trigger_status: Optional[Dict[str, Any]] = kwargs.pop("trigger_status")
        if "order_type" in kwargs:
            self.order_type: Optional[Dict[str, Any]] = kwargs.pop("order_type")
        if "reject_reason" in kwargs:
            self.reject_reason: Optional[Dict[str, Any]] = kwargs.pop("reject_reason")
        if "settled" in kwargs:
            self.settled: Optional[bool] = kwargs.pop("settled")
        if "product_type" in kwargs:
            self.product_type: Optional[ProductType] = kwargs.pop("product_type")
        if "reject_message" in kwargs:
            self.reject_message: Optional[str] = kwargs.pop("reject_message")
        if "cancel_message" in kwargs:
            self.cancel_message: Optional[str] = kwargs.pop("cancel_message")
        if "order_placement_source" in kwargs:
            self.order_placement_source: Optional[OrderPlacementSource] = kwargs.pop(
                "order_placement_source"
            )
        if "outstanding_hold_amount" in kwargs:
            self.outstanding_hold_amount: Optional[str] = kwargs.pop(
                "outstanding_hold_amount"
            )
        if "is_liquidation" in kwargs:
            self.is_liquidation: Optional[bool] = kwargs.pop("is_liquidation")
        if "last_fill_time" in kwargs:
            self.last_fill_time: Optional[Dict[str, Any]] = kwargs.pop("last_fill_time")
        if "edit_history" in kwargs:
            self.edit_history: Optional[List[Dict[str, Any]]] = kwargs.pop(
                "edit_history"
            )
        if "leverage" in kwargs:
            self.leverage: Optional[str] = kwargs.pop("leverage")
        if "margin_type" in kwargs:
            self.margin_type: Optional[MarginType] = kwargs.pop("margin_type")
        if "retail_portfolio_id" in kwargs:
            self.retail_portfolio_id: Optional[str] = kwargs.pop("retail_portfolio_id")
        if "originating_order_id" in kwargs:
            self.originating_order_id: Optional[str] = kwargs.pop(
                "originating_order_id"
            )
        if "attached_order_id" in kwargs:
            self.attached_order_id: Optional[str] = kwargs.pop("attached_order_id")
        # NOT LIVE YET
        # if "attached_order_configuration" in kwargs:
        #     self.attached_order_configuration: Optional[
        #         OrderConfiguration
        #     ] = OrderConfiguration(**kwargs.pop("attached_order_configuration"))
        super().__init__(**kwargs)


class PaymentMethod(BaseResponse):
    def __init__(self, **kwargs):
        if "id" in kwargs:
            self.id: Optional[str] = kwargs.pop("id")
        if "type" in kwargs:
            self.type: Optional[str] = kwargs.pop("type")
        if "name" in kwargs:
            self.name: Optional[str] = kwargs.pop("name")
        if "currency" in kwargs:
            self.currency: Optional[str] = kwargs.pop("currency")
        if "verified" in kwargs:
            self.verified: Optional[bool] = kwargs.pop("verified")
        if "allow_buy" in kwargs:
            self.allow_buy: Optional[bool] = kwargs.pop("allow_buy")
        if "allow_sell" in kwargs:
            self.allow_sell: Optional[bool] = kwargs.pop("allow_sell")
        if "allow_deposit" in kwargs:
            self.allow_deposit: Optional[bool] = kwargs.pop("allow_deposit")
        if "allow_withdraw" in kwargs:
            self.allow_withdraw: Optional[bool] = kwargs.pop("allow_withdraw")
        if "created_at" in kwargs:
            self.created_at: Optional[str] = kwargs.pop("created_at")
        if "updated_at" in kwargs:
            self.updated_at: Optional[str] = kwargs.pop("updated_at")
        super().__init__(**kwargs)


class PerpetualPortfolio(BaseResponse):
    def __init__(self, **kwargs):
        if "portfolio_uuid" in kwargs:
            self.portfolio_uuid: Optional[str] = kwargs.pop("portfolio_uuid")
        if "collateral" in kwargs:
            self.collateral: Optional[str] = kwargs.pop("collateral")
        if "position_notional" in kwargs:
            self.position_notional: Optional[str] = kwargs.pop("position_notional")
        if "open_position_notional" in kwargs:
            self.open_position_notional: Optional[str] = kwargs.pop(
                "open_position_notional"
            )
        if "pending_fees" in kwargs:
            self.pending_fees: Optional[str] = kwargs.pop("pending_fees")
        if "borrow" in kwargs:
            self.borrow: Optional[str] = kwargs.pop("borrow")
        if "accrued_interest" in kwargs:
            self.accrued_interest: Optional[str] = kwargs.pop("accrued_interest")
        if "rolling_debt" in kwargs:
            self.rolling_debt: Optional[str] = kwargs.pop("rolling_debt")
        if "portfolio_initial_margin" in kwargs:
            self.portfolio_initial_margin: Optional[str] = kwargs.pop(
                "portfolio_initial_margin"
            )
        if "portfolio_im_notional" in kwargs:
            self.portfolio_im_notional: Optional[Dict[str, Any]] = kwargs.pop(
                "portfolio_im_notional"
            )
        if "liquidation_percentage" in kwargs:
            self.liquidation_percentage: Optional[str] = kwargs.pop(
                "liquidation_percentage"
            )
        if "liquidation_buffer" in kwargs:
            self.liquidation_buffer: Optional[str] = kwargs.pop("liquidation_buffer")
        if "margin_type" in kwargs:
            self.margin_type: Optional[Dict[str, Any]] = kwargs.pop("margin_type")
        if "margin_flags" in kwargs:
            self.margin_flags: Optional[Dict[str, Any]] = kwargs.pop("margin_flags")
        if "liquidation_status" in kwargs:
            self.liquidation_status: Optional[Dict[str, Any]] = kwargs.pop(
                "liquidation_status"
            )
        if "unrealized_pnl" in kwargs:
            self.unrealized_pnl: Optional[Dict[str, Any]] = kwargs.pop("unrealized_pnl")
        if "total_balance" in kwargs:
            self.total_balance: Optional[Dict[str, Any]] = kwargs.pop("total_balance")
        super().__init__(**kwargs)


class PortfolioSummary(BaseResponse):
    def __init__(self, **kwargs):
        if "unrealized_pnl" in kwargs:
            self.unrealized_pnl: Optional[Dict[str, Any]] = kwargs.pop("unrealized_pnl")
        if "buying_power" in kwargs:
            self.buying_power: Optional[Dict[str, Any]] = kwargs.pop("buying_power")
        if "total_balance" in kwargs:
            self.total_balance: Optional[Dict[str, Any]] = kwargs.pop("total_balance")
        if "max_withdrawal_amount" in kwargs:
            self.max_withdrawal_amount: Optional[Dict[str, Any]] = kwargs.pop(
                "max_withdrawal_amount"
            )
        super().__init__(**kwargs)


class Position(BaseResponse):
    def __init__(self, **kwargs):
        if "product_id" in kwargs:
            self.product_id: Optional[str] = kwargs.pop("product_id")
        if "product_uuid" in kwargs:
            self.product_uuid: Optional[str] = kwargs.pop("product_uuid")
        if "portfolio_uuid" in kwargs:
            self.portfolio_uuid: Optional[str] = kwargs.pop("portfolio_uuid")
        if "symbol" in kwargs:
            self.symbol: Optional[str] = kwargs.pop("symbol")
        if "vwap" in kwargs:
            self.vwap: Optional[Dict[str, Any]] = kwargs.pop("vwap")
        if "entry_vwap" in kwargs:
            self.entry_vwap: Optional[Dict[str, Any]] = kwargs.pop("entry_vwap")
        if "position_side" in kwargs:
            self.position_side: Optional[Dict[str, Any]] = kwargs.pop("position_side")
        if "margin_type" in kwargs:
            self.margin_type: Optional[Dict[str, Any]] = kwargs.pop("margin_type")
        if "net_size" in kwargs:
            self.net_size: Optional[str] = kwargs.pop("net_size")
        if "buy_order_size" in kwargs:
            self.buy_order_size: Optional[str] = kwargs.pop("buy_order_size")
        if "sell_order_size" in kwargs:
            self.sell_order_size: Optional[str] = kwargs.pop("sell_order_size")
        if "im_contribution" in kwargs:
            self.im_contribution: Optional[str] = kwargs.pop("im_contribution")
        if "unrealized_pnl" in kwargs:
            self.unrealized_pnl: Optional[Dict[str, Any]] = kwargs.pop("unrealized_pnl")
        if "mark_price" in kwargs:
            self.mark_price: Optional[Dict[str, Any]] = kwargs.pop("mark_price")
        if "liquidation_price" in kwargs:
            self.liquidation_price: Optional[Dict[str, Any]] = kwargs.pop(
                "liquidation_price"
            )
        if "leverage" in kwargs:
            self.leverage: Optional[str] = kwargs.pop("leverage")
        if "im_notional" in kwargs:
            self.im_notional: Optional[Dict[str, Any]] = kwargs.pop("im_notional")
        if "mm_notional" in kwargs:
            self.mm_notional: Optional[Dict[str, Any]] = kwargs.pop("mm_notional")
        if "position_notional" in kwargs:
            self.position_notional: Optional[Dict[str, Any]] = kwargs.pop(
                "position_notional"
            )
        if "aggregated_pnl" in kwargs:
            self.aggregated_pnl: Optional[Dict[str, Any]] = kwargs.pop("aggregated_pnl")

        super().__init__(**kwargs)


class PositionSummary(BaseResponse):
    def __init__(self, **kwargs):
        if "aggregated_pnl" in kwargs:
            self.aggregated_pnl: Optional[Dict[str, Any]] = kwargs.pop("aggregated_pnl")
        super().__init__(**kwargs)


class Balance(BaseResponse):
    def __init__(self, **kwargs):
        if "asset" in kwargs:
            self.asset: Dict[str, Any] = kwargs.pop("asset")
        if "quantity" in kwargs:
            self.quantity: str = kwargs.pop("quantity")
        if "hold" in kwargs:
            self.hold: str = kwargs.pop("hold")
        if "transfer_hold" in kwargs:
            self.transfer_hold: str = kwargs.pop("transfer_hold")
        if "collateral_value" in kwargs:
            self.collateral_value: str = kwargs.pop("collateral_value")
        if "collateral_weight" in kwargs:
            self.collateral_weight: str = kwargs.pop("collateral_weight")
        if "max_withdraw_amount" in kwargs:
            self.max_withdraw_amount: str = kwargs.pop("max_withdraw_amount")
        if "loan" in kwargs:
            self.loan: str = kwargs.pop("loan")
        if "loan_collateral_requirement_usd" in kwargs:
            self.loan_collateral_requirement_usd: str = kwargs.pop(
                "loan_collateral_requirement_usd"
            )
        if "pledged_quantity" in kwargs:
            self.pledged_quantity: str = kwargs.pop("pledged_quantity")
        super().__init__(**kwargs)


class PortfolioBalance(BaseResponse):
    def __init__(self, **kwargs):
        if "portfolio_uuid" in kwargs:
            self.portfolio_uuid: Optional[str] = kwargs.pop("portfolio_uuid")
        if "balances" in kwargs:
            self.balances: Optional[List[Balance]] = [
                Balance(**balance) for balance in kwargs.pop("balances")
            ]
        if "is_margin_limit_reached" in kwargs:
            self.is_margin_limit_reached: Optional[bool] = kwargs.pop(
                "is_margin_limit_reached"
            )
        super().__init__(**kwargs)


class Portfolio(BaseResponse):
    def __init__(self, **kwargs):
        if "name" in kwargs:
            self.name: Optional[str] = kwargs.pop("name")
        if "uuid" in kwargs:
            self.uuid: Optional[str] = kwargs.pop("uuid")
        if "type" in kwargs:
            self.type: Optional[str] = kwargs.pop("type")
        super().__init__(**kwargs)


class PortfolioBreakdown(BaseResponse):
    def __init__(self, **kwargs):
        if "portfolio" in kwargs:
            self.portfolio: Optional[Portfolio] = Portfolio(**kwargs.pop("portfolio"))
        if "portfolio_balances" in kwargs:
            self.portfolio_balances: Optional[Dict[str, Any]] = kwargs.pop(
                "portfolio_balances"
            )
        if "spot_positions" in kwargs:
            self.spot_positions: Optional[List[Dict[str, Any]]] = kwargs.pop(
                "spot_positions"
            )
        if "perp_positions" in kwargs:
            self.perp_positions: Optional[List[Dict[str, Any]]] = kwargs.pop(
                "perp_positions"
            )
        if "futures_positions" in kwargs:
            self.futures_positions: Optional[List[Dict[str, Any]]] = kwargs.pop(
                "futures_positions"
            )
        super().__init__(**kwargs)


class PriceBook(BaseResponse):
    def __init__(self, **kwargs):
        if "product_id" in kwargs:
            self.product_id: str = kwargs.pop("product_id")
        if "bids" in kwargs:
            self.bids: List[Dict[str, Any]] = kwargs.pop("bids")
        if "asks" in kwargs:
            self.asks: List[Dict[str, Any]] = kwargs.pop("asks")
        if "time" in kwargs:
            self.time: Optional[Dict[str, Any]] = kwargs.pop("time")
        super().__init__(**kwargs)


class Product(BaseResponse):
    def __init__(self, **kwargs):
        if "product_id" in kwargs:
            self.product_id: str = kwargs.pop("product_id")
        if "price" in kwargs:
            self.price: str = kwargs.pop("price")
        if "price_percentage_change_24h" in kwargs:
            self.price_percentage_change_24h: str = kwargs.pop(
                "price_percentage_change_24h"
            )
        if "volume_24h" in kwargs:
            self.volume_24h: str = kwargs.pop("volume_24h")
        if "volume_percentage_change_24h" in kwargs:
            self.volume_percentage_change_24h: str = kwargs.pop(
                "volume_percentage_change_24h"
            )
        if "base_increment" in kwargs:
            self.base_increment: str = kwargs.pop("base_increment")
        if "quote_increment" in kwargs:
            self.quote_increment: str = kwargs.pop("quote_increment")
        if "quote_min_size" in kwargs:
            self.quote_min_size: str = kwargs.pop("quote_min_size")
        if "quote_max_size" in kwargs:
            self.quote_max_size: str = kwargs.pop("quote_max_size")
        if "base_min_size" in kwargs:
            self.base_min_size: str = kwargs.pop("base_min_size")
        if "base_max_size" in kwargs:
            self.base_max_size: str = kwargs.pop("base_max_size")
        if "base_name" in kwargs:
            self.base_name: str = kwargs.pop("base_name")
        if "quote_name" in kwargs:
            self.quote_name: str = kwargs.pop("quote_name")
        if "watched" in kwargs:
            self.watched: bool = kwargs.pop("watched")
        if "is_disabled" in kwargs:
            self.is_disabled: bool = kwargs.pop("is_disabled")
        if "new" in kwargs:
            self.new: bool = kwargs.pop("new")
        if "status" in kwargs:
            self.status: str = kwargs.pop("status")
        if "cancel_only" in kwargs:
            self.cancel_only: bool = kwargs.pop("cancel_only")
        if "limit_only" in kwargs:
            self.limit_only: bool = kwargs.pop("limit_only")
        if "post_only" in kwargs:
            self.post_only: bool = kwargs.pop("post_only")
        if "trading_disabled" in kwargs:
            self.trading_disabled: bool = kwargs.pop("trading_disabled")
        if "auction_mode" in kwargs:
            self.auction_mode: bool = kwargs.pop("auction_mode")
        if "product_type" in kwargs:
            self.product_type: Optional[ProductType] = kwargs.pop("product_type")
        if "quote_currency_id" in kwargs:
            self.quote_currency_id: Optional[str] = kwargs.pop("quote_currency_id")
        if "base_currency_id" in kwargs:
            self.base_currency_id: Optional[str] = kwargs.pop("base_currency_id")
        if "fcm_trading_session_details" in kwargs:
            self.fcm_trading_session_details: Optional[Dict[str, Any]] = kwargs.pop(
                "fcm_trading_session_details"
            )
        if "mid_market_price" in kwargs:
            self.mid_market_price: Optional[str] = kwargs.pop("mid_market_price")
        if "alias" in kwargs:
            self.alias: Optional[str] = kwargs.pop("alias")
        if "alias_to" in kwargs:
            self.alias_to: Optional[List[str]] = kwargs.pop("alias_to")
        if "base_display_symbol" in kwargs:
            self.base_display_symbol: str = kwargs.pop("base_display_symbol")
        if "quote_display_symbol" in kwargs:
            self.quote_display_symbol: Optional[str] = kwargs.pop(
                "quote_display_symbol"
            )
        if "view_only" in kwargs:
            self.view_only: Optional[bool] = kwargs.pop("view_only")
        if "price_increment" in kwargs:
            self.price_increment: Optional[str] = kwargs.pop("price_increment")
        if "display_name" in kwargs:
            self.display_name: Optional[str] = kwargs.pop("display_name")
        if "product_venue" in kwargs:
            self.product_venue: Optional[ProductVenue] = kwargs.pop("product_venue")
        if "approximate_quote_24h_volume" in kwargs:
            self.approximate_quote_24h_volume: Optional[str] = kwargs.pop(
                "approximate_quote_24h_volume"
            )
        if "future_product_details" in kwargs:
            self.future_product_details: Optional[Dict[str, Any]] = kwargs.pop(
                "future_product_details"
            )
        super().__init__(**kwargs)


class Products(BaseResponse):
    def __init__(self, **kwargs):
        if "products" in kwargs:
            self.products: Optional[List[Product]] = [
                Product(**product) for product in kwargs.pop("products")
            ]
        if "num_products" in kwargs:
            self.num_products: Optional[int] = kwargs.pop("num_products")
        super().__init__(**kwargs)


class Candle(BaseResponse):
    def __init__(self, **kwargs):
        if "start" in kwargs:
            self.start: Optional[str] = kwargs.pop("start")
        if "low" in kwargs:
            self.low: Optional[str] = kwargs.pop("low")
        if "high" in kwargs:
            self.high: Optional[str] = kwargs.pop("high")
        if "open" in kwargs:
            self.open: Optional[str] = kwargs.pop("open")
        if "close" in kwargs:
            self.close: Optional[str] = kwargs.pop("close")
        if "volume" in kwargs:
            self.volume: Optional[str] = kwargs.pop("volume")
        super().__init__(**kwargs)


class Candles(BaseResponse):
    def __init__(self, **kwargs):
        if "candles" in kwargs:
            self.candles: Optional[List[Candle]] = [
                Candle(**candle) for candle in kwargs.pop("candles")
            ]
        super().__init__(**kwargs)


class HistoricalMarketTrade(BaseResponse):
    def __init__(self, **kwargs):
        if "trade_id" in kwargs:
            self.trade_id: Optional[str] = kwargs.pop("trade_id")
        if "product_id" in kwargs:
            self.product_id: Optional[str] = kwargs.pop("product_id")
        if "price" in kwargs:
            self.price: Optional[str] = kwargs.pop("price")
        if "size" in kwargs:
            self.size: Optional[str] = kwargs.pop("size")
        if "time" in kwargs:
            self.time: Optional[str] = kwargs.pop("time")
        if "side" in kwargs:
            self.side: Optional[OrderSide] = kwargs.pop("side")
        super().__init__(**kwargs)
