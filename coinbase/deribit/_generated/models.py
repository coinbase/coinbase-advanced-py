"""GENERATED from the Deribit Retail OpenAPI spec — do not edit."""

from coinbase.deribit._model import DeribitModel


# --- enums ---
class Advanced:
    """advanced type: `"usd"` or `"implv"` (Only for options; field is omitted if not applicable)."""

    USD = "usd"
    IMPLV = "implv"
    VALUES = frozenset({"usd", "implv"})


class BookState:
    """The state of the order book. Represents the current lifecycle stage of the instrument."""

    OPEN = "open"
    SETTLEMENT = "settlement"
    DELIVERED = "delivered"
    INACTIVE = "inactive"
    LOCKED = "locked"
    HALTED = "halted"
    ARCHIVIZED = "archivized"
    VALUES = frozenset(
        {
            "open",
            "settlement",
            "delivered",
            "inactive",
            "locked",
            "halted",
            "archivized",
        }
    )


class CancelReason:
    """Enumerated reason behind cancel `"user_request"`, `"autoliquidation"`, `"cancel_on_disconnect"`, `"risk_mitigation"`, `"pme_risk_reduction"` (portfolio margining risk reduction), `"pme_account_locked"` (portfolio margining account locked per currency), `"position_locked"`, `"mmp_trigger"` (market maker protection), `"mmp_config_curtailment"` (market maker configured quantity decreased), `"edit_post_only_reject"` (cancelled on edit because of `reject_post_only` setting), `"oco_other_closed"` (the oco order linked to this order was closed), `"oto_primary_closed"` (the oto primary order that was going to trigger this order was cancelled), `"settlement"` (closed because of a settlement event, e.g. good-til-day orders are cancelled when an instrument enters the daily settlement). Note: orders cancelled because an instrument expired (delivery) currently do not include a `cancel_reason` field."""

    USER_REQUEST = "user_request"
    AUTOLIQUIDATION = "autoliquidation"
    CANCEL_ON_DISCONNECT = "cancel_on_disconnect"
    RISK_MITIGATION = "risk_mitigation"
    PME_RISK_REDUCTION = "pme_risk_reduction"
    PME_ACCOUNT_LOCKED = "pme_account_locked"
    POSITION_LOCKED = "position_locked"
    MMP_TRIGGER = "mmp_trigger"
    MMP_CONFIG_CURTAILMENT = "mmp_config_curtailment"
    EDIT_POST_ONLY_REJECT = "edit_post_only_reject"
    OCO_OTHER_CLOSED = "oco_other_closed"
    OTO_PRIMARY_CLOSED = "oto_primary_closed"
    SETTLEMENT = "settlement"
    VALUES = frozenset(
        {
            "user_request",
            "autoliquidation",
            "cancel_on_disconnect",
            "risk_mitigation",
            "pme_risk_reduction",
            "pme_account_locked",
            "position_locked",
            "mmp_trigger",
            "mmp_config_curtailment",
            "edit_post_only_reject",
            "oco_other_closed",
            "oto_primary_closed",
            "settlement",
        }
    )


class CodScope:
    """Informs if Cancel on Disconnect was checked for the current connection or the account"""

    CONNECTION = "connection"
    ACCOUNT = "account"
    VALUES = frozenset({"connection", "account"})


class ComboState:
    """Combo state: `"active"`, "`inactive`" """

    ACTIVE = "active"
    INACTIVE = "inactive"
    VALUES = frozenset({"active", "inactive"})


class Currency:
    """Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`"""

    BTC = "BTC"
    ETH = "ETH"
    USDC = "USDC"
    USDT = "USDT"
    EURR = "EURR"
    VALUES = frozenset({"BTC", "ETH", "USDC", "USDT", "EURR"})


class CurrencyWithAny:
    """Currency name or `"any"` if don't care"""

    BTC = "BTC"
    ETH = "ETH"
    USDC = "USDC"
    USDT = "USDT"
    EURR = "EURR"
    ANY = "any"
    VALUES = frozenset({"BTC", "ETH", "USDC", "USDT", "EURR", "any"})


class CurrencyWithAnyAndGrouped:
    """Currency name or `"any"` if don't care or `"grouped"` if grouped by currencies"""

    BTC = "BTC"
    ETH = "ETH"
    USDC = "USDC"
    SOL = "SOL"
    USDT = "USDT"
    EURR = "EURR"
    XRP = "XRP"
    STETH = "STETH"
    USYC = "USYC"
    PAXG = "PAXG"
    BNB = "BNB"
    USDE = "USDE"
    ANY = "any"
    GROUPED = "grouped"
    VALUES = frozenset(
        {
            "BTC",
            "ETH",
            "USDC",
            "SOL",
            "USDT",
            "EURR",
            "XRP",
            "STETH",
            "USYC",
            "PAXG",
            "BNB",
            "USDE",
            "any",
            "grouped",
        }
    )


class Direction:
    """Direction: `buy`, or `sell`"""

    BUY = "buy"
    SELL = "sell"
    VALUES = frozenset({"buy", "sell"})


class FeeRole:
    """Fee role of the user: `maker` or `taker`. Can be different from trade role of the user when iceberg order was involved in matching."""

    MAKER = "maker"
    TAKER = "taker"
    VALUES = frozenset({"maker", "taker"})


class IndexName:
    """Index identifier, matches (base) cryptocurrency with quote currency"""

    BTC_USD = "btc_usd"
    ETH_USD = "eth_usd"
    ADA_USDC = "ada_usdc"
    ALGO_USDC = "algo_usdc"
    AVAX_USDC = "avax_usdc"
    BCH_USDC = "bch_usdc"
    BNB_USDC = "bnb_usdc"
    BTC_USDC = "btc_usdc"
    BTCDVOL_USDC = "btcdvol_usdc"
    BUIDL_USDC = "buidl_usdc"
    DOGE_USDC = "doge_usdc"
    DOT_USDC = "dot_usdc"
    EURR_USDC = "eurr_usdc"
    ETH_USDC = "eth_usdc"
    ETHDVOL_USDC = "ethdvol_usdc"
    HYPE_USDC = "hype_usdc"
    LINK_USDC = "link_usdc"
    LTC_USDC = "ltc_usdc"
    NEAR_USDC = "near_usdc"
    PAXG_USDC = "paxg_usdc"
    SHIB_USDC = "shib_usdc"
    SOL_USDC = "sol_usdc"
    STETH_USDC = "steth_usdc"
    TON_USDC = "ton_usdc"
    TRUMP_USDC = "trump_usdc"
    TRX_USDC = "trx_usdc"
    UNI_USDC = "uni_usdc"
    USDE_USDC = "usde_usdc"
    USYC_USDC = "usyc_usdc"
    XRP_USDC = "xrp_usdc"
    BTC_USDT = "btc_usdt"
    ETH_USDT = "eth_usdt"
    EURR_USDT = "eurr_usdt"
    SOL_USDT = "sol_usdt"
    STETH_USDT = "steth_usdt"
    USDC_USDT = "usdc_usdt"
    USDE_USDT = "usde_usdt"
    BTC_EURR = "btc_eurr"
    BTC_USDE = "btc_usde"
    BTC_USYC = "btc_usyc"
    ETH_BTC = "eth_btc"
    ETH_EURR = "eth_eurr"
    ETH_USDE = "eth_usde"
    ETH_USYC = "eth_usyc"
    STETH_ETH = "steth_eth"
    PAXG_BTC = "paxg_btc"
    DRBFIX_BTC_USDC = "drbfix-btc_usdc"
    DRBFIX_ETH_USDC = "drbfix-eth_usdc"
    VALUES = frozenset(
        {
            "btc_usd",
            "eth_usd",
            "ada_usdc",
            "algo_usdc",
            "avax_usdc",
            "bch_usdc",
            "bnb_usdc",
            "btc_usdc",
            "btcdvol_usdc",
            "buidl_usdc",
            "doge_usdc",
            "dot_usdc",
            "eurr_usdc",
            "eth_usdc",
            "ethdvol_usdc",
            "hype_usdc",
            "link_usdc",
            "ltc_usdc",
            "near_usdc",
            "paxg_usdc",
            "shib_usdc",
            "sol_usdc",
            "steth_usdc",
            "ton_usdc",
            "trump_usdc",
            "trx_usdc",
            "uni_usdc",
            "usde_usdc",
            "usyc_usdc",
            "xrp_usdc",
            "btc_usdt",
            "eth_usdt",
            "eurr_usdt",
            "sol_usdt",
            "steth_usdt",
            "usdc_usdt",
            "usde_usdt",
            "btc_eurr",
            "btc_usde",
            "btc_usyc",
            "eth_btc",
            "eth_eurr",
            "eth_usde",
            "eth_usyc",
            "steth_eth",
            "paxg_btc",
            "drbfix-btc_usdc",
            "drbfix-eth_usdc",
        }
    )


class Kind:
    """Instrument kind: `"future"`, `"option"`, `"spot"`, `"future_combo"`, `"option_combo"`"""

    FUTURE = "future"
    OPTION = "option"
    SPOT = "spot"
    FUTURE_COMBO = "future_combo"
    OPTION_COMBO = "option_combo"
    VALUES = frozenset({"future", "option", "spot", "future_combo", "option_combo"})


class KindFutureOrOptionWithAny:
    """Instrument kind: `"future"`, `"option"` or `"any"` for all"""

    FUTURE = "future"
    OPTION = "option"
    ANY = "any"
    VALUES = frozenset({"future", "option", "any"})


class KindWithComboAll:
    """Instrument kind: `"future"`, `"option"`, `"spot"`, `"future_combo"`, `"option_combo"`, `"combo"` for any combo or `"any"` for all"""

    FUTURE = "future"
    OPTION = "option"
    SPOT = "spot"
    FUTURE_COMBO = "future_combo"
    OPTION_COMBO = "option_combo"
    COMBO = "combo"
    ANY = "any"
    VALUES = frozenset(
        {"future", "option", "spot", "future_combo", "option_combo", "combo", "any"}
    )


class KindWithoutSpot:
    """Instrument kind: `"future"`, `"option"`, `"future_combo"`, `"option_combo"` (spot is excluded as spot trades are settled immediately and have no open positions)"""

    FUTURE = "future"
    OPTION = "option"
    FUTURE_COMBO = "future_combo"
    OPTION_COMBO = "option_combo"
    VALUES = frozenset({"future", "option", "future_combo", "option_combo"})


class OrderState:
    """Order state: `"open"`, `"filled"`, `"rejected"`, `"cancelled"`, `"untriggered"`"""

    OPEN = "open"
    FILLED = "filled"
    REJECTED = "rejected"
    CANCELLED = "cancelled"
    UNTRIGGERED = "untriggered"
    TRIGGERED = "triggered"
    VALUES = frozenset(
        {"open", "filled", "rejected", "cancelled", "untriggered", "triggered"}
    )


class OrderStateInUserTrade:
    """Order state: `"open"`, `"filled"`, `"rejected"`, `"cancelled"`, `"untriggered"` or `"archive"` (if order was archived)"""

    OPEN = "open"
    FILLED = "filled"
    REJECTED = "rejected"
    CANCELLED = "cancelled"
    UNTRIGGERED = "untriggered"
    ARCHIVE = "archive"
    VALUES = frozenset(
        {"open", "filled", "rejected", "cancelled", "untriggered", "archive"}
    )


class OrderType:
    """Order type: `"limit"`, `"market"`, `"stop_limit"`, `"stop_market"`, `"take_limit"`, `"take_market"`, `"trailing_stop"`"""

    MARKET = "market"
    LIMIT = "limit"
    STOP_MARKET = "stop_market"
    STOP_LIMIT = "stop_limit"
    TAKE_MARKET = "take_market"
    TAKE_LIMIT = "take_limit"
    TRAILING_STOP = "trailing_stop"
    VALUES = frozenset(
        {
            "market",
            "limit",
            "stop_market",
            "stop_limit",
            "take_market",
            "take_limit",
            "trailing_stop",
        }
    )


class OrderType2:
    """Order type: `"all"`, `"limit"`, `"trigger_all"`, `"stop_all"`, `"stop_limit"`, `"stop_market"`, `"take_all"`, `"take_limit"`, `"take_market"`, `"trailing_all"`, `"trailing_stop"`"""

    ALL = "all"
    LIMIT = "limit"
    TRIGGER_ALL = "trigger_all"
    STOP_ALL = "stop_all"
    STOP_LIMIT = "stop_limit"
    STOP_MARKET = "stop_market"
    TAKE_ALL = "take_all"
    TAKE_LIMIT = "take_limit"
    TAKE_MARKET = "take_market"
    TRAILING_ALL = "trailing_all"
    TRAILING_STOP = "trailing_stop"
    VALUES = frozenset(
        {
            "all",
            "limit",
            "trigger_all",
            "stop_all",
            "stop_limit",
            "stop_market",
            "take_all",
            "take_limit",
            "take_market",
            "trailing_all",
            "trailing_stop",
        }
    )


class OriginalOrderType:
    """Original API order type when an order is represented internally as a limit order. For example, Starbase market orders use `"limit"` as `order_type` with `"market"` in this optional field."""

    MARKET = "market"
    MARKET_LIMIT = "market_limit"
    VALUES = frozenset({"market", "market_limit"})


class PmeCurrency:
    """The currency for which the Extended Risk Matrix will be calculated. Use `CROSS` for Cross Collateral simulation."""

    BTC = "BTC"
    ETH = "ETH"
    USDC = "USDC"
    USDT = "USDT"
    CROSS = "CROSS"
    VALUES = frozenset({"BTC", "ETH", "USDC", "USDT", "CROSS"})


class PositionDirection:
    """Direction: `buy`, `sell` or `zero`"""

    BUY = "buy"
    SELL = "sell"
    ZERO = "zero"
    VALUES = frozenset({"buy", "sell", "zero"})


class Role:
    """Trade role of the user: `maker` or `taker`"""

    MAKER = "maker"
    TAKER = "taker"
    VALUES = frozenset({"maker", "taker"})


class SettlementCurrencyWithAnyAndGrouped:
    """Currency name or `"any"` if don't care or `"grouped"` if grouped by currencies"""

    BTC = "BTC"
    ETH = "ETH"
    USDC = "USDC"
    USDT = "USDT"
    ANY = "any"
    GROUPED = "grouped"
    VALUES = frozenset({"BTC", "ETH", "USDC", "USDT", "any", "grouped"})


class SettlementType:
    """The type of settlement event. `settlement`: daily settlement of futures and perpetual positions at 08:00 UTC, converting unrealized profit and loss into realized profit and loss (option positions do not settle). `delivery`: one-time expiration of a futures or options contract at 08:00 UTC, closing any remaining open position at the delivery price (does not apply to perpetual or spot instruments). `bankruptcy`."""

    SETTLEMENT = "settlement"
    DELIVERY = "delivery"
    BANKRUPTCY = "bankruptcy"
    VALUES = frozenset({"settlement", "delivery", "bankruptcy"})


class SimpleOrderType:
    """Order type: `"all"`, `"limit"`, `"stop"`, `"take"`, `"trailing_stop"`, `"trailing_take"`"""

    ALL = "all"
    LIMIT = "limit"
    TRIGGER_ALL = "trigger_all"
    STOP = "stop"
    TAKE = "take"
    TRAILING_STOP = "trailing_stop"
    VALUES = frozenset({"all", "limit", "trigger_all", "stop", "take", "trailing_stop"})


class Sorting:
    """Sorting"""

    ASC = "asc"
    DESC = "desc"
    DEFAULT = "default"
    VALUES = frozenset({"asc", "desc", "default"})


class TickDirection:
    """Direction of the "tick" (`0` = Plus Tick, `1` = Zero-Plus Tick, `2` = Minus Tick, `3` = Zero-Minus Tick)."""

    VALUES = frozenset({})


class TimeInForce:
    """Order time in force: `"good_til_cancelled"`, `"good_til_day"`, `"fill_or_kill"` or `"immediate_or_cancel"`"""

    GOOD_TIL_CANCELLED = "good_til_cancelled"
    GOOD_TIL_DAY = "good_til_day"
    FILL_OR_KILL = "fill_or_kill"
    IMMEDIATE_OR_CANCEL = "immediate_or_cancel"
    VALUES = frozenset(
        {"good_til_cancelled", "good_til_day", "fill_or_kill", "immediate_or_cancel"}
    )


class TransferDirection:
    """Transfer direction"""

    PAYMENT = "payment"
    INCOME = "income"
    VALUES = frozenset({"payment", "income"})


class TransferType:
    """Type of transfer: `user` - sent to user, `subaccount` - sent to subaccount"""

    USER = "user"
    SUBACCOUNT = "subaccount"
    VALUES = frozenset({"user", "subaccount"})


class Trigger:
    """Trigger type (only for trigger orders). Allowed values: `"index_price"`, `"mark_price"`, `"last_price"`."""

    INDEX_PRICE = "index_price"
    MARK_PRICE = "mark_price"
    LAST_PRICE = "last_price"
    VALUES = frozenset({"index_price", "mark_price", "last_price"})


class TriggerFillCondition:
    """<p>The fill condition of the linked order (Only for linked order types), default: `first_hit`.</p> <ul> <li>`"first_hit"` - any execution of the primary order will fully cancel/place all secondary orders.</li> <li>`"complete_fill"` - a complete execution (meaning the primary order no longer exists) will cancel/place the secondary orders.</li> <li>`"incremental"` - any fill of the primary order will cause proportional partial cancellation/placement of the secondary order. The amount that will be subtracted/added to the secondary order will be rounded down to the contract size.</li> </ul>"""

    FIRST_HIT = "first_hit"
    COMPLETE_FILL = "complete_fill"
    INCREMENTAL = "incremental"
    VALUES = frozenset({"first_hit", "complete_fill", "incremental"})


class WalletCurrency:
    """Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`"""

    BTC = "BTC"
    ETH = "ETH"
    STETH = "STETH"
    ETHW = "ETHW"
    USDC = "USDC"
    USDT = "USDT"
    EURR = "EURR"
    SOL = "SOL"
    XRP = "XRP"
    USYC = "USYC"
    PAXG = "PAXG"
    BNB = "BNB"
    USDE = "USDE"
    VALUES = frozenset(
        {
            "BTC",
            "ETH",
            "STETH",
            "ETHW",
            "USDC",
            "USDT",
            "EURR",
            "SOL",
            "XRP",
            "USYC",
            "PAXG",
            "BNB",
            "USDE",
        }
    )


# --- models ---
class AccessLog(DeribitModel):
    """AccessLog"""


class ApiLimits(DeribitModel):
    """Account API rate limits."""


class BlockTrade(DeribitModel):
    """BlockTrade"""


class BookSummary(DeribitModel):
    """BookSummary"""


class Combo(DeribitModel):
    """Combo"""


class ComboLeg(DeribitModel):
    """ComboLeg"""


class CurrencyPortfolio(DeribitModel):
    """CurrencyPortfolio"""


class CurrencyWithApr(DeribitModel):
    """CurrencyWithApr"""


class DeltaTotalMap(DeribitModel):
    """Map of position delta sums by price index (e.g. `btc_usd`), covering both futures and options positions."""


class ErrorMessageResponse(DeribitModel):
    """ErrorMessageResponse"""


class Expirations(DeribitModel):
    """A map where each key is valid currency (e.g. btc, eth, usdc), and the value is a list of expirations or a map where each key is a valid kind (future or options) and value is a list of expirations from every instrument"""


class Getunsubscribe200response(DeribitModel):
    """Getunsubscribe200response"""


class Greeks(DeribitModel):
    """Only for options. Greeks are risk measures that describe how the option's price changes with respect to various factors."""


class Instrument(DeribitModel):
    """Instrument"""


class KeyNumberPair(DeribitModel):
    """KeyNumberPair"""


class OkResponse(DeribitModel):
    """OkResponse"""


class Order(DeribitModel):
    """Order"""


class OrderIdInitialMarginPair(DeribitModel):
    """OrderIdInitialMarginPair"""


class Portfolio(DeribitModel):
    """Portfolio"""


class Position(DeribitModel):
    """Position"""


class PositionWithOpenOrdersMargin(DeribitModel):
    """PositionWithOpenOrdersMargin"""


class PrivateAccountResponse(DeribitModel):
    """PrivateAccountResponse"""


class PrivateAccountResponseResult(DeribitModel):
    """PrivateAccountResponseResult"""


class PrivateAccountResponseResultFees(DeribitModel):
    """Fee structure for all currency pairs and instrument types related to the currency (available when parameter `extended` = `true` and user has any discounts). Keys are index names (e.g., "btc_usd"), values are objects with instrument types as keys (option, perpetual, future)."""


class PrivateAccountResponseResultOptionsGammaMap(DeribitModel):
    """Map of options' gammas per index"""


class PrivateAccountResponseResultOptionsThetaMap(DeribitModel):
    """Map of options' thetas per index"""


class PrivateAccountResponseResultOptionsVegaMap(DeribitModel):
    """Map of options' vegas per index"""


class PrivateAccountResponseResultTradingProductsDetails(DeribitModel):
    """Which trading products are enabled or can be overwritten for the account"""


class PrivateAccountSummariesResponse(DeribitModel):
    """PrivateAccountSummariesResponse"""


class PrivateAccountSummariesResponseResult(DeribitModel):
    """PrivateAccountSummariesResponseResult"""


class PrivateAccountSummariesResponseResultIsolatedAccountSummaries(DeribitModel):
    """PrivateAccountSummariesResponseResultIsolatedAccountSummaries"""


class PrivateAccountSummariesResponseResultSummaries(DeribitModel):
    """PrivateAccountSummariesResponseResultSummaries"""


class PrivateAccountSummariesResponseResultSummariesFees(DeribitModel):
    """Fee structure for all currency pairs and instrument types related to the currency (available when parameter `extended` = `true` and user has any discounts). Keys are index names (e.g., "btc_usd"), values are objects with instrument types as keys (option, perpetual, future)."""


class PrivateAccountSummariesResponseResultSummariesOptionsGammaMap(DeribitModel):
    """Map of options' gammas per index"""


class PrivateAccountSummariesResponseResultSummariesOptionsThetaMap(DeribitModel):
    """Map of options' thetas per index"""


class PrivateAccountSummariesResponseResultSummariesOptionsVegaMap(DeribitModel):
    """Map of options' vegas per index"""


class PrivateAccountSummariesResponseResultSummariesTradingProductsDetails(
    DeribitModel
):
    """Which trading products are enabled or can be overwritten for the account"""


class PrivateAccountSummariesResponseResultTradingProductsDetails(DeribitModel):
    """Which trading products are enabled or can be overwritten for the account"""


class PrivateBuyAndSellResponse(DeribitModel):
    """PrivateBuyAndSellResponse"""


class PrivateBuyAndSellResponseResult(DeribitModel):
    """PrivateBuyAndSellResponseResult"""


class PrivateCancelAllResponse(DeribitModel):
    """PrivateCancelAllResponse"""


class PrivateCancelResponse(DeribitModel):
    """PrivateCancelResponse"""


class PrivateChangeMarginModelResponse(DeribitModel):
    """PrivateChangeMarginModelResponse"""


class PrivateChangeMarginModelResponseResult(DeribitModel):
    """PrivateChangeMarginModelResponseResult"""


class PrivateChangeMarginModelResponseResultNewState(DeribitModel):
    """Represents portfolio state after change"""


class PrivateChangeMarginModelResponseResultOldState(DeribitModel):
    """Represents portfolio state before change"""


class PrivateCreateComboResponse(DeribitModel):
    """PrivateCreateComboResponse"""


class PrivateEditResponse(DeribitModel):
    """PrivateEditResponse"""


class PrivateEditResponseResult(DeribitModel):
    """PrivateEditResponseResult"""


class PrivateGetAccessLogResponse(DeribitModel):
    """PrivateGetAccessLogResponse"""


class PrivateGetBrokerTradeRequestsResponse(DeribitModel):
    """PrivateGetBrokerTradeRequestsResponse"""


class PrivateGetBrokerTradeRequestsResponseResult(DeribitModel):
    """PrivateGetBrokerTradeRequestsResponseResult"""


class PrivateGetBrokerTradeRequestsResponseResultMaker(DeribitModel):
    """PrivateGetBrokerTradeRequestsResponseResultMaker"""


class PrivateGetBrokerTradeRequestsResponseResultTaker(DeribitModel):
    """PrivateGetBrokerTradeRequestsResponseResultTaker"""


class PrivateGetBrokerTradeRequestsResponseResultTrades(DeribitModel):
    """PrivateGetBrokerTradeRequestsResponseResultTrades"""


class PrivateGetBrokerTradesResponse(DeribitModel):
    """PrivateGetBrokerTradesResponse"""


class PrivateGetBrokerTradesResponseResult(DeribitModel):
    """PrivateGetBrokerTradesResponseResult"""


class PrivateGetBrokerTradesResponseResultHistory(DeribitModel):
    """PrivateGetBrokerTradesResponseResultHistory"""


class PrivateGetBrokerTradesResponseResultHistoryMaker(DeribitModel):
    """PrivateGetBrokerTradesResponseResultHistoryMaker"""


class PrivateGetBrokerTradesResponseResultHistoryTaker(DeribitModel):
    """PrivateGetBrokerTradesResponseResultHistoryTaker"""


class PrivateGetCancelOnDisconnectResponse(DeribitModel):
    """PrivateGetCancelOnDisconnectResponse"""


class PrivateGetCancelOnDisconnectResponseResult(DeribitModel):
    """PrivateGetCancelOnDisconnectResponseResult"""


class PrivateGetLegPricesResponse(DeribitModel):
    """PrivateGetLegPricesResponse"""


class PrivateGetLegPricesResponseResult(DeribitModel):
    """PrivateGetLegPricesResponseResult"""


class PrivateGetLeverageResponse(DeribitModel):
    """PrivateGetLeverageResponse"""


class PrivateGetMarginsResponse(DeribitModel):
    """PrivateGetMarginsResponse"""


class PrivateGetMarginsResponseResult(DeribitModel):
    """PrivateGetMarginsResponseResult"""


class PrivateGetMaxOrderSizeResponse(DeribitModel):
    """PrivateGetMaxOrderSizeResponse"""


class PrivateGetMaxOrderSizeResponseResult(DeribitModel):
    """PrivateGetMaxOrderSizeResponseResult"""


class PrivateGetMaxOrderSizeResponseResultMaxTradableAmount(DeribitModel):
    """PrivateGetMaxOrderSizeResponseResultMaxTradableAmount"""


class PrivateGetMaxOrderSizeResponseResultMaxTradableAmountReduceOnly(DeribitModel):
    """PrivateGetMaxOrderSizeResponseResultMaxTradableAmountReduceOnly"""


class PrivateGetOpenOrdersResponse(DeribitModel):
    """PrivateGetOpenOrdersResponse"""


class PrivateGetOrderHistoryResponse(DeribitModel):
    """PrivateGetOrderHistoryResponse"""


class PrivateGetOrderMarginByIdsResponse(DeribitModel):
    """PrivateGetOrderMarginByIdsResponse"""


class PrivateGetOrderStateByLabelResponse(DeribitModel):
    """PrivateGetOrderStateByLabelResponse"""


class PrivateGetOrderStateResponse(DeribitModel):
    """PrivateGetOrderStateResponse"""


class PrivateGetPositionResponse(DeribitModel):
    """PrivateGetPositionResponse"""


class PrivateGetPositionsResponse(DeribitModel):
    """PrivateGetPositionsResponse"""


class PrivateGetRiskProfileResponse(DeribitModel):
    """PrivateGetRiskProfileResponse"""


class PrivateGetRiskProfileResponseResult(DeribitModel):
    """PrivateGetRiskProfileResponseResult"""


class PrivateGetSubaccountsDetailsResponse(DeribitModel):
    """PrivateGetSubaccountsDetailsResponse"""


class PrivateGetSubaccountsDetailsResponseResult(DeribitModel):
    """PrivateGetSubaccountsDetailsResponseResult"""


class PrivateGetSubaccountsResponse(DeribitModel):
    """PrivateGetSubaccountsResponse"""


class PrivateGetSubaccountsResponseResult(DeribitModel):
    """PrivateGetSubaccountsResponseResult"""


class PrivateGetTradingLimitsResponse(DeribitModel):
    """PrivateGetTradingLimitsResponse"""


class PrivateGetTradingLimitsResponseResult(DeribitModel):
    """PrivateGetTradingLimitsResponseResult"""


class PrivateGetTransactionLogResponse(DeribitModel):
    """PrivateGetTransactionLogResponse"""


class PrivateGetTransactionLogResponseResult(DeribitModel):
    """PrivateGetTransactionLogResponseResult"""


class PrivateGetTriggerOrderHistoryResponse(DeribitModel):
    """PrivateGetTriggerOrderHistoryResponse"""


class PrivateGetTriggerOrderHistoryResponseResult(DeribitModel):
    """PrivateGetTriggerOrderHistoryResponseResult"""


class PrivateGetUserLocksResponse(DeribitModel):
    """PrivateGetUserLocksResponse"""


class PrivateGetUserLocksResponseResult(DeribitModel):
    """PrivateGetUserLocksResponseResult"""


class PrivateGetUserTradesByOrderResponse(DeribitModel):
    """PrivateGetUserTradesByOrderResponse"""


class PrivateGetUserTradesHistoryResponse(DeribitModel):
    """PrivateGetUserTradesHistoryResponse"""


class PrivateGetUserTradesHistoryResponseResult(DeribitModel):
    """PrivateGetUserTradesHistoryResponseResult"""


class PrivatePmeParamsResponse(DeribitModel):
    """PrivatePmeParamsResponse"""


class PrivatePmeParamsResponseResult(DeribitModel):
    """Portfolio Margin order restrictions, or `enabled: false` when Portfolio Margin is disabled."""


class PrivatePmeSimulateResponse(DeribitModel):
    """PrivatePmeSimulateResponse"""


class PrivatePmeSimulateResponseResult(DeribitModel):
    """Simulation details"""


class PrivateSetLeverageResponse(DeribitModel):
    """PrivateSetLeverageResponse"""


class PrivateSettlementResponse(DeribitModel):
    """PrivateSettlementResponse"""


class PrivateSettlementResponseResult(DeribitModel):
    """PrivateSettlementResponseResult"""


class PrivateSimulatePortfolioResponse(DeribitModel):
    """PrivateSimulatePortfolioResponse"""


class PrivateSimulatePortfolioResponseResult(DeribitModel):
    """Portfolio margin simulation result"""


class PrivateSimulatePortfolioResponseResultDeltaTotalMap(DeribitModel):
    """Map of total deltas per index"""


class PrivateSimulatePortfolioResponseResultOptionsGammaMap(DeribitModel):
    """Map of options' gammas per index"""


class PrivateSimulatePortfolioResponseResultOptionsThetaMap(DeribitModel):
    """Map of options' thetas per index"""


class PrivateSimulatePortfolioResponseResultOptionsVegaMap(DeribitModel):
    """Map of options' vegas per index"""


class PrivateSubmitTransferResponse(DeribitModel):
    """PrivateSubmitTransferResponse"""


class PrivateSubscribeResponse(DeribitModel):
    """PrivateSubscribeResponse"""


class PublicAuthResponse(DeribitModel):
    """PublicAuthResponse"""


class PublicAuthResponseResult(DeribitModel):
    """PublicAuthResponseResult"""


class PublicGetAnnouncementsResponse(DeribitModel):
    """PublicGetAnnouncementsResponse"""


class PublicGetAnnouncementsResponseResult(DeribitModel):
    """PublicGetAnnouncementsResponseResult"""


class PublicGetBookSummaryResponse(DeribitModel):
    """PublicGetBookSummaryResponse"""


class PublicGetComboDetailsResponse(DeribitModel):
    """PublicGetComboDetailsResponse"""


class PublicGetComboIdsResponse(DeribitModel):
    """PublicGetComboIdsResponse"""


class PublicGetCombosResponse(DeribitModel):
    """PublicGetCombosResponse"""


class PublicGetContractSizeResponse(DeribitModel):
    """PublicGetContractSizeResponse"""


class PublicGetContractSizeResponseResult(DeribitModel):
    """PublicGetContractSizeResponseResult"""


class PublicGetCurrenciesResponse(DeribitModel):
    """PublicGetCurrenciesResponse"""


class PublicGetDeliveryPricesResponse(DeribitModel):
    """PublicGetDeliveryPricesResponse"""


class PublicGetDeliveryPricesResponseResult(DeribitModel):
    """PublicGetDeliveryPricesResponseResult"""


class PublicGetDeliveryPricesResponseResultData(DeribitModel):
    """PublicGetDeliveryPricesResponseResultData"""


class PublicGetExpirationsResponse(DeribitModel):
    """PublicGetExpirationsResponse"""


class PublicGetFundingChartDataResponse(DeribitModel):
    """PublicGetFundingChartDataResponse"""


class PublicGetFundingChartDataResponseResult(DeribitModel):
    """PublicGetFundingChartDataResponseResult"""


class PublicGetFundingChartDataResponseResultData(DeribitModel):
    """PublicGetFundingChartDataResponseResultData"""


class PublicGetFundingRateHistoryResponse(DeribitModel):
    """PublicGetFundingRateHistoryResponse"""


class PublicGetFundingRateHistoryResponseResult(DeribitModel):
    """PublicGetFundingRateHistoryResponseResult"""


class PublicGetFundingRateValueResponse(DeribitModel):
    """PublicGetFundingRateValueResponse"""


class PublicGetHistoricalVolatilityResponse(DeribitModel):
    """PublicGetHistoricalVolatilityResponse"""


class PublicGetHistoricalVolatilityResponseResult(DeribitModel):
    """PublicGetHistoricalVolatilityResponseResult"""


class PublicGetIndexChartDataResponse(DeribitModel):
    """PublicGetIndexChartDataResponse"""


class PublicGetIndexPriceNamesResponse(DeribitModel):
    """PublicGetIndexPriceNamesResponse"""


class PublicGetIndexPriceNamesResponseResult(DeribitModel):
    """PublicGetIndexPriceNamesResponseResult"""


class PublicGetIndexPriceResponse(DeribitModel):
    """PublicGetIndexPriceResponse"""


class PublicGetIndexPriceResponseResult(DeribitModel):
    """PublicGetIndexPriceResponseResult"""


class PublicGetInstrumentResponse(DeribitModel):
    """PublicGetInstrumentResponse"""


class PublicGetInstrumentsResponse(DeribitModel):
    """PublicGetInstrumentsResponse"""


class PublicGetMarkPriceHistoryResponse(DeribitModel):
    """PublicGetMarkPriceHistoryResponse"""


class PublicGetOrderBookResponse(DeribitModel):
    """PublicGetOrderBookResponse"""


class PublicGetTimeResponse(DeribitModel):
    """PublicGetTimeResponse"""


class PublicGetTradesVolumesResponse(DeribitModel):
    """PublicGetTradesVolumesResponse"""


class PublicGetTradingviewChartDataResponse(DeribitModel):
    """PublicGetTradingviewChartDataResponse"""


class PublicGetTradingviewChartDataResponseResult(DeribitModel):
    """PublicGetTradingviewChartDataResponseResult"""


class PublicGetVolatilityIndexDataResponse(DeribitModel):
    """PublicGetVolatilityIndexDataResponse"""


class PublicGetVolatilityIndexDataResponseResult(DeribitModel):
    """Volatility index candles."""


class PublicSettlementResponse(DeribitModel):
    """PublicSettlementResponse"""


class PublicSettlementResponseResult(DeribitModel):
    """PublicSettlementResponseResult"""


class PublicStatusResponse(DeribitModel):
    """PublicStatusResponse"""


class PublicStatusResponseResult(DeribitModel):
    """PublicStatusResponseResult"""


class PublicTestResponse(DeribitModel):
    """PublicTestResponse"""


class PublicTestResponseResult(DeribitModel):
    """PublicTestResponseResult"""


class PublicTickerResponse(DeribitModel):
    """PublicTickerResponse"""


class PublicTickersByCurrencyResponse(DeribitModel):
    """PublicTickersByCurrencyResponse"""


class PublicTrade(DeribitModel):
    """PublicTrade"""


class PublicTradesHistoryResponse(DeribitModel):
    """PublicTradesHistoryResponse"""


class PublicTradesHistoryResponseResult(DeribitModel):
    """PublicTradesHistoryResponseResult"""


class Settlement(DeribitModel):
    """Settlement"""


class Stats(DeribitModel):
    """Stats"""


class TickSizeStep(DeribitModel):
    """TickSizeStep"""


class TickerNotification(DeribitModel):
    """TickerNotification"""


class TickerNotificationWithBidsAndAsks(DeribitModel):
    """TickerNotificationWithBidsAndAsks"""


class TradesVolumes(DeribitModel):
    """TradesVolumes"""


class TransactionLog(DeribitModel):
    """TransactionLog"""


class TransactionLogInfo(DeribitModel):
    """Additional information regarding transaction. Strongly dependent on the log entry type"""


class TransferItem(DeribitModel):
    """TransferItem"""


class TriggerOrderHistoryRecord(DeribitModel):
    """TriggerOrderHistoryRecord"""


class UserTrade(DeribitModel):
    """UserTrade"""


class UserTradeTradeAllocations(DeribitModel):
    """UserTradeTradeAllocations"""


class UserTradeTradeAllocationsClientInfo(DeribitModel):
    """Optional client allocation info for brokers."""


# --- nested-field wiring (forward refs resolved here) ---
BlockTrade._NESTED = {"trades": (UserTrade, True)}
Combo._NESTED = {"legs": (ComboLeg, True)}
CurrencyWithApr._NESTED = {"withdrawal_priorities": (KeyNumberPair, True)}
Instrument._NESTED = {"tick_size_steps": (TickSizeStep, False)}
Portfolio._NESTED = {"btc(example)": (CurrencyPortfolio, False)}
PrivateAccountResponse._NESTED = {"result": (PrivateAccountResponseResult, False)}
PrivateAccountResponseResult._NESTED = {
    "delta_total_map": (DeltaTotalMap, False),
    "fees": (PrivateAccountResponseResultFees, False),
    "limits": (ApiLimits, False),
    "options_gamma_map": (PrivateAccountResponseResultOptionsGammaMap, False),
    "options_theta_map": (PrivateAccountResponseResultOptionsThetaMap, False),
    "options_vega_map": (PrivateAccountResponseResultOptionsVegaMap, False),
    "trading_products_details": (
        PrivateAccountResponseResultTradingProductsDetails,
        False,
    ),
}
PrivateAccountSummariesResponse._NESTED = {
    "result": (PrivateAccountSummariesResponseResult, False)
}
PrivateAccountSummariesResponseResult._NESTED = {
    "isolated_account_summaries": (
        PrivateAccountSummariesResponseResultIsolatedAccountSummaries,
        True,
    ),
    "summaries": (PrivateAccountSummariesResponseResultSummaries, True),
    "trading_products_details": (
        PrivateAccountSummariesResponseResultTradingProductsDetails,
        False,
    ),
}
PrivateAccountSummariesResponseResultSummaries._NESTED = {
    "delta_total_map": (DeltaTotalMap, False),
    "fees": (PrivateAccountSummariesResponseResultSummariesFees, False),
    "limits": (ApiLimits, False),
    "options_gamma_map": (
        PrivateAccountSummariesResponseResultSummariesOptionsGammaMap,
        False,
    ),
    "options_theta_map": (
        PrivateAccountSummariesResponseResultSummariesOptionsThetaMap,
        False,
    ),
    "options_vega_map": (
        PrivateAccountSummariesResponseResultSummariesOptionsVegaMap,
        False,
    ),
    "trading_products_details": (
        PrivateAccountSummariesResponseResultSummariesTradingProductsDetails,
        False,
    ),
}
PrivateBuyAndSellResponse._NESTED = {"result": (PrivateBuyAndSellResponseResult, False)}
PrivateBuyAndSellResponseResult._NESTED = {
    "order": (Order, False),
    "trades": (UserTrade, True),
}
PrivateCancelResponse._NESTED = {"result": (Order, False)}
PrivateChangeMarginModelResponse._NESTED = {
    "result": (PrivateChangeMarginModelResponseResult, True)
}
PrivateChangeMarginModelResponseResult._NESTED = {
    "new_state": (PrivateChangeMarginModelResponseResultNewState, False),
    "old_state": (PrivateChangeMarginModelResponseResultOldState, False),
}
PrivateCreateComboResponse._NESTED = {"result": (Combo, False)}
PrivateEditResponse._NESTED = {"result": (PrivateEditResponseResult, False)}
PrivateEditResponseResult._NESTED = {
    "order": (Order, False),
    "trades": (UserTrade, True),
}
PrivateGetAccessLogResponse._NESTED = {"result": (AccessLog, True)}
PrivateGetBrokerTradeRequestsResponse._NESTED = {
    "result": (PrivateGetBrokerTradeRequestsResponseResult, True)
}
PrivateGetBrokerTradeRequestsResponseResult._NESTED = {
    "maker": (PrivateGetBrokerTradeRequestsResponseResultMaker, False),
    "taker": (PrivateGetBrokerTradeRequestsResponseResultTaker, False),
    "trades": (PrivateGetBrokerTradeRequestsResponseResultTrades, True),
}
PrivateGetBrokerTradesResponse._NESTED = {
    "result": (PrivateGetBrokerTradesResponseResult, False)
}
PrivateGetBrokerTradesResponseResult._NESTED = {
    "history": (PrivateGetBrokerTradesResponseResultHistory, True)
}
PrivateGetBrokerTradesResponseResultHistory._NESTED = {
    "maker": (PrivateGetBrokerTradesResponseResultHistoryMaker, False),
    "taker": (PrivateGetBrokerTradesResponseResultHistoryTaker, False),
    "trades": (BlockTrade, True),
}
PrivateGetCancelOnDisconnectResponse._NESTED = {
    "result": (PrivateGetCancelOnDisconnectResponseResult, False)
}
PrivateGetLegPricesResponse._NESTED = {
    "result": (PrivateGetLegPricesResponseResult, False)
}
PrivateGetMarginsResponse._NESTED = {"result": (PrivateGetMarginsResponseResult, False)}
PrivateGetMaxOrderSizeResponse._NESTED = {
    "result": (PrivateGetMaxOrderSizeResponseResult, False)
}
PrivateGetMaxOrderSizeResponseResult._NESTED = {
    "max_tradable_amount": (
        PrivateGetMaxOrderSizeResponseResultMaxTradableAmount,
        False,
    ),
    "max_tradable_amount_reduce_only": (
        PrivateGetMaxOrderSizeResponseResultMaxTradableAmountReduceOnly,
        False,
    ),
}
PrivateGetOpenOrdersResponse._NESTED = {"result": (Order, True)}
PrivateGetOrderHistoryResponse._NESTED = {"result": (Order, True)}
PrivateGetOrderMarginByIdsResponse._NESTED = {
    "result": (OrderIdInitialMarginPair, True)
}
PrivateGetOrderStateResponse._NESTED = {"result": (Order, False)}
PrivateGetPositionResponse._NESTED = {"result": (PositionWithOpenOrdersMargin, False)}
PrivateGetPositionsResponse._NESTED = {"result": (PositionWithOpenOrdersMargin, True)}
PrivateGetRiskProfileResponse._NESTED = {
    "result": (PrivateGetRiskProfileResponseResult, False)
}
PrivateGetSubaccountsDetailsResponse._NESTED = {
    "result": (PrivateGetSubaccountsDetailsResponseResult, True)
}
PrivateGetSubaccountsDetailsResponseResult._NESTED = {
    "open_orders": (Order, True),
    "positions": (Position, True),
}
PrivateGetSubaccountsResponse._NESTED = {
    "result": (PrivateGetSubaccountsResponseResult, True)
}
PrivateGetSubaccountsResponseResult._NESTED = {"portfolio": (Portfolio, False)}
PrivateGetTradingLimitsResponse._NESTED = {
    "result": (PrivateGetTradingLimitsResponseResult, False)
}
PrivateGetTransactionLogResponse._NESTED = {
    "result": (PrivateGetTransactionLogResponseResult, False)
}
PrivateGetTransactionLogResponseResult._NESTED = {"logs": (TransactionLog, True)}
PrivateGetTriggerOrderHistoryResponse._NESTED = {
    "result": (PrivateGetTriggerOrderHistoryResponseResult, False)
}
PrivateGetTriggerOrderHistoryResponseResult._NESTED = {
    "entries": (TriggerOrderHistoryRecord, True)
}
PrivateGetUserLocksResponse._NESTED = {
    "result": (PrivateGetUserLocksResponseResult, True)
}
PrivateGetUserTradesByOrderResponse._NESTED = {"result": (UserTrade, True)}
PrivateGetUserTradesHistoryResponse._NESTED = {
    "result": (PrivateGetUserTradesHistoryResponseResult, False)
}
PrivateGetUserTradesHistoryResponseResult._NESTED = {"trades": (UserTrade, True)}
PrivatePmeParamsResponse._NESTED = {"result": (PrivatePmeParamsResponseResult, False)}
PrivatePmeSimulateResponse._NESTED = {
    "result": (PrivatePmeSimulateResponseResult, False)
}
PrivateSettlementResponse._NESTED = {"result": (PrivateSettlementResponseResult, False)}
PrivateSettlementResponseResult._NESTED = {"settlements": (Settlement, True)}
PrivateSimulatePortfolioResponse._NESTED = {
    "result": (PrivateSimulatePortfolioResponseResult, False)
}
PrivateSimulatePortfolioResponseResult._NESTED = {
    "delta_total_map": (PrivateSimulatePortfolioResponseResultDeltaTotalMap, False),
    "options_gamma_map": (PrivateSimulatePortfolioResponseResultOptionsGammaMap, False),
    "options_theta_map": (PrivateSimulatePortfolioResponseResultOptionsThetaMap, False),
    "options_vega_map": (PrivateSimulatePortfolioResponseResultOptionsVegaMap, False),
}
PrivateSubmitTransferResponse._NESTED = {"result": (TransferItem, False)}
PublicAuthResponse._NESTED = {"result": (PublicAuthResponseResult, False)}
PublicGetAnnouncementsResponse._NESTED = {
    "result": (PublicGetAnnouncementsResponseResult, True)
}
PublicGetBookSummaryResponse._NESTED = {"result": (BookSummary, True)}
PublicGetComboDetailsResponse._NESTED = {"result": (Combo, False)}
PublicGetCombosResponse._NESTED = {"result": (Combo, True)}
PublicGetContractSizeResponse._NESTED = {
    "result": (PublicGetContractSizeResponseResult, False)
}
PublicGetCurrenciesResponse._NESTED = {"result": (CurrencyWithApr, True)}
PublicGetDeliveryPricesResponse._NESTED = {
    "result": (PublicGetDeliveryPricesResponseResult, False)
}
PublicGetDeliveryPricesResponseResult._NESTED = {
    "data": (PublicGetDeliveryPricesResponseResultData, True)
}
PublicGetExpirationsResponse._NESTED = {"result": (Expirations, True)}
PublicGetFundingChartDataResponse._NESTED = {
    "result": (PublicGetFundingChartDataResponseResult, False)
}
PublicGetFundingChartDataResponseResult._NESTED = {
    "data": (PublicGetFundingChartDataResponseResultData, True)
}
PublicGetFundingRateHistoryResponse._NESTED = {
    "result": (PublicGetFundingRateHistoryResponseResult, True)
}
PublicGetHistoricalVolatilityResponse._NESTED = {
    "result": (PublicGetHistoricalVolatilityResponseResult, True)
}
PublicGetIndexPriceNamesResponse._NESTED = {
    "result": (PublicGetIndexPriceNamesResponseResult, True)
}
PublicGetIndexPriceResponse._NESTED = {
    "result": (PublicGetIndexPriceResponseResult, False)
}
PublicGetInstrumentResponse._NESTED = {"result": (Instrument, False)}
PublicGetInstrumentsResponse._NESTED = {"result": (Instrument, True)}
PublicGetOrderBookResponse._NESTED = {
    "result": (TickerNotificationWithBidsAndAsks, False)
}
PublicGetTradesVolumesResponse._NESTED = {"result": (TradesVolumes, True)}
PublicGetTradingviewChartDataResponse._NESTED = {
    "result": (PublicGetTradingviewChartDataResponseResult, False)
}
PublicGetVolatilityIndexDataResponse._NESTED = {
    "result": (PublicGetVolatilityIndexDataResponseResult, False)
}
PublicSettlementResponse._NESTED = {"result": (PublicSettlementResponseResult, False)}
PublicSettlementResponseResult._NESTED = {"settlements": (Settlement, True)}
PublicStatusResponse._NESTED = {"result": (PublicStatusResponseResult, False)}
PublicTestResponse._NESTED = {"result": (PublicTestResponseResult, False)}
PublicTickerResponse._NESTED = {"result": (TickerNotification, False)}
PublicTradesHistoryResponse._NESTED = {
    "result": (PublicTradesHistoryResponseResult, False)
}
PublicTradesHistoryResponseResult._NESTED = {"trades": (PublicTrade, True)}
TickerNotification._NESTED = {"greeks": (Greeks, False), "stats": (Stats, False)}
TickerNotificationWithBidsAndAsks._NESTED = {
    "greeks": (Greeks, False),
    "stats": (Stats, False),
}
TransactionLog._NESTED = {"info": (TransactionLogInfo, False)}
UserTrade._NESTED = {"trade_allocations": (UserTradeTradeAllocations, True)}
UserTradeTradeAllocations._NESTED = {
    "client_info": (UserTradeTradeAllocationsClientInfo, False)
}
