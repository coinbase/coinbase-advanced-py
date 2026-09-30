"""GENERATED from the Deribit Retail AsyncAPI spec — do not edit."""

# Subscription-channel builders. Pass the result(s) to the WS client's
# subscribe(); the builder fills the instrument/currency/interval segments.


def announcements():
    return f"announcements"


def book_instrument_name_group_depth_interval(instrument_name, group, depth, interval):
    return f"book.{instrument_name}.{group}.{depth}.{interval}"


def book_instrument_name_interval(instrument_name, interval):
    return f"book.{instrument_name}.{interval}"


def chart_trades_instrument_name_resolution(instrument_name, resolution):
    return f"chart.trades.{instrument_name}.{resolution}"


def deribit_price_index_index_name(index_name):
    return f"deribit_price_index.{index_name}"


def deribit_price_ranking_index_name(index_name):
    return f"deribit_price_ranking.{index_name}"


def deribit_price_statistics_index_name(index_name):
    return f"deribit_price_statistics.{index_name}"


def deribit_volatility_index_index_name(index_name):
    return f"deribit_volatility_index.{index_name}"


def estimated_expiration_price_index_name(index_name):
    return f"estimated_expiration_price.{index_name}"


def incremental_ticker_instrument_name(instrument_name):
    return f"incremental_ticker.{instrument_name}"


def instrument_creation_kind_currency(kind, currency):
    return f"instrument.creation.{kind}.{currency}"


def instrument_state_kind_currency(kind, currency):
    return f"instrument.state.{kind}.{currency}"


def markprice_options_index_name(index_name):
    return f"markprice.options.{index_name}"


def perpetual_instrument_name_interval(instrument_name, interval):
    return f"perpetual.{instrument_name}.{interval}"


def platform_state():
    return f"platform_state"


def platform_state_public_methods_state():
    return f"platform_state.public_methods_state"


def quote_instrument_name(instrument_name):
    return f"quote.{instrument_name}"


def ticker_instrument_name_interval(instrument_name, interval):
    return f"ticker.{instrument_name}.{interval}"


def trades_instrument_name_interval(instrument_name, interval):
    return f"trades.{instrument_name}.{interval}"


def trades_kind_currency_interval(kind, currency, interval):
    return f"trades.{kind}.{currency}.{interval}"


def user_access_log():
    return f"user.access_log"


def user_changes_instrument_name_interval(instrument_name, interval):
    return f"user.changes.{instrument_name}.{interval}"


def user_changes_kind_currency_interval(kind, currency, interval):
    return f"user.changes.{kind}.{currency}.{interval}"


def user_combo_trades_instrument_name_interval(instrument_name, interval):
    return f"user.combo_trades.{instrument_name}.{interval}"


def user_combo_trades_kind_currency_interval(kind, currency, interval):
    return f"user.combo_trades.{kind}.{currency}.{interval}"


def user_isolated_changes_instrument_name_interval(instrument_name, interval):
    return f"user.isolated.changes.{instrument_name}.{interval}"


def user_isolated_changes_kind_currency_interval(kind, currency, interval):
    return f"user.isolated.changes.{kind}.{currency}.{interval}"


def user_isolated_liquidation():
    return f"user.isolated.liquidation"


def user_isolated_orders_instrument_name_interval(instrument_name, interval):
    return f"user.isolated.orders.{instrument_name}.{interval}"


def user_isolated_orders_kind_currency_interval(kind, currency, interval):
    return f"user.isolated.orders.{kind}.{currency}.{interval}"


def user_isolated_portfolio_currency(currency):
    return f"user.isolated.portfolio.{currency}"


def user_isolated_trades_instrument_name_interval(instrument_name, interval):
    return f"user.isolated.trades.{instrument_name}.{interval}"


def user_isolated_trades_kind_currency_interval(kind, currency, interval):
    return f"user.isolated.trades.{kind}.{currency}.{interval}"


def user_lock():
    return f"user.lock"


def user_orders_instrument_name_interval(instrument_name, interval):
    return f"user.orders.{instrument_name}.{interval}"


def user_orders_instrument_name_raw(instrument_name):
    return f"user.orders.{instrument_name}.raw"


def user_orders_kind_currency_interval(kind, currency, interval):
    return f"user.orders.{kind}.{currency}.{interval}"


def user_orders_kind_currency_raw(kind, currency):
    return f"user.orders.{kind}.{currency}.raw"


def user_portfolio_currency(currency):
    return f"user.portfolio.{currency}"


def user_position_lock():
    return f"user.position_lock"


def user_trades_instrument_name_interval(instrument_name, interval):
    return f"user.trades.{instrument_name}.{interval}"


def user_trades_kind_currency_interval(kind, currency, interval):
    return f"user.trades.{kind}.{currency}.{interval}"


def user_trailing_orders_trigger_price_currency(currency):
    return f"user.trailing_orders.trigger_price.{currency}"
