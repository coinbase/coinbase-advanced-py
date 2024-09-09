REST API Client
=====================


RESTClient Constructor
-------------------------------

.. autoclass:: coinbase.rest.RESTClient

REST Utils
-------------------------------

.. autofunction:: coinbase.rest.RESTClient.get
.. autofunction:: coinbase.rest.RESTClient.post
.. autofunction:: coinbase.rest.RESTClient.put
.. autofunction:: coinbase.rest.RESTClient.delete

Accounts
-----------------------------

.. autofunction:: coinbase.rest.RESTClient.get_accounts
.. autofunction:: coinbase.rest.RESTClient.get_account

Products
-----------------------------

.. autofunction:: coinbase.rest.RESTClient.get_products
.. autofunction:: coinbase.rest.RESTClient.get_product
.. autofunction:: coinbase.rest.RESTClient.get_product_book
.. autofunction:: coinbase.rest.RESTClient.get_best_bid_ask

Market Data
---------------------------------

.. autofunction:: coinbase.rest.RESTClient.get_candles
.. autofunction:: coinbase.rest.RESTClient.get_market_trades

Orders
---------------------------

.. autofunction:: coinbase.rest.RESTClient.create_order
.. autofunction:: coinbase.rest.RESTClient.market_order
.. autofunction:: coinbase.rest.RESTClient.market_order_buy
.. autofunction:: coinbase.rest.RESTClient.market_order_sell
.. autofunction:: coinbase.rest.RESTClient.limit_order_ioc
.. autofunction:: coinbase.rest.RESTClient.limit_order_ioc_buy
.. autofunction:: coinbase.rest.RESTClient.limit_order_ioc_sell
.. autofunction:: coinbase.rest.RESTClient.limit_order_gtc
.. autofunction:: coinbase.rest.RESTClient.limit_order_gtc_buy
.. autofunction:: coinbase.rest.RESTClient.limit_order_gtc_sell
.. autofunction:: coinbase.rest.RESTClient.limit_order_gtd
.. autofunction:: coinbase.rest.RESTClient.limit_order_gtd_buy
.. autofunction:: coinbase.rest.RESTClient.limit_order_gtd_sell
.. autofunction:: coinbase.rest.RESTClient.limit_order_fok
.. autofunction:: coinbase.rest.RESTClient.limit_order_fok_buy
.. autofunction:: coinbase.rest.RESTClient.limit_order_fok_sell
.. autofunction:: coinbase.rest.RESTClient.stop_limit_order_gtc
.. autofunction:: coinbase.rest.RESTClient.stop_limit_order_gtc_buy
.. autofunction:: coinbase.rest.RESTClient.stop_limit_order_gtc_sell
.. autofunction:: coinbase.rest.RESTClient.stop_limit_order_gtd
.. autofunction:: coinbase.rest.RESTClient.stop_limit_order_gtd_buy
.. autofunction:: coinbase.rest.RESTClient.stop_limit_order_gtd_sell
.. autofunction:: coinbase.rest.RESTClient.trigger_bracket_order_gtc
.. autofunction:: coinbase.rest.RESTClient.trigger_bracket_order_gtc_buy
.. autofunction:: coinbase.rest.RESTClient.trigger_bracket_order_gtc_sell
.. autofunction:: coinbase.rest.RESTClient.trigger_bracket_order_gtd
.. autofunction:: coinbase.rest.RESTClient.trigger_bracket_order_gtd_buy
.. autofunction:: coinbase.rest.RESTClient.trigger_bracket_order_gtd_sell
.. autofunction:: coinbase.rest.RESTClient.get_order
.. autofunction:: coinbase.rest.RESTClient.list_orders
.. autofunction:: coinbase.rest.RESTClient.get_fills
.. autofunction:: coinbase.rest.RESTClient.edit_order
.. autofunction:: coinbase.rest.RESTClient.preview_edit_order
.. autofunction:: coinbase.rest.RESTClient.cancel_orders
.. autofunction:: coinbase.rest.RESTClient.preview_order
.. autofunction:: coinbase.rest.RESTClient.preview_market_order
.. autofunction:: coinbase.rest.RESTClient.preview_market_order_buy
.. autofunction:: coinbase.rest.RESTClient.preview_market_order_sell
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_ioc
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_ioc_buy
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_ioc_sell
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_gtc
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_gtc_buy
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_gtc_sell
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_gtd
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_gtd_buy
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_gtd_sell
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_fok
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_fok_buy
.. autofunction:: coinbase.rest.RESTClient.preview_limit_order_fok_sell
.. autofunction:: coinbase.rest.RESTClient.preview_stop_limit_order_gtc
.. autofunction:: coinbase.rest.RESTClient.preview_stop_limit_order_gtc_buy
.. autofunction:: coinbase.rest.RESTClient.preview_stop_limit_order_gtc_sell
.. autofunction:: coinbase.rest.RESTClient.preview_stop_limit_order_gtd
.. autofunction:: coinbase.rest.RESTClient.preview_stop_limit_order_gtd_buy
.. autofunction:: coinbase.rest.RESTClient.preview_stop_limit_order_gtd_sell
.. autofunction:: coinbase.rest.RESTClient.preview_trigger_bracket_order_gtc
.. autofunction:: coinbase.rest.RESTClient.preview_trigger_bracket_order_gtc_buy
.. autofunction:: coinbase.rest.RESTClient.preview_trigger_bracket_order_gtc_sell
.. autofunction:: coinbase.rest.RESTClient.preview_trigger_bracket_order_gtd
.. autofunction:: coinbase.rest.RESTClient.preview_trigger_bracket_order_gtd_buy
.. autofunction:: coinbase.rest.RESTClient.preview_trigger_bracket_order_gtd_sell
.. autofunction:: coinbase.rest.RESTClient.close_position

Portfolios
-------------------------------

.. autofunction:: coinbase.rest.RESTClient.get_portfolios
.. autofunction:: coinbase.rest.RESTClient.create_portfolio
.. autofunction:: coinbase.rest.RESTClient.get_portfolio_breakdown
.. autofunction:: coinbase.rest.RESTClient.move_portfolio_funds
.. autofunction:: coinbase.rest.RESTClient.edit_portfolio
.. autofunction:: coinbase.rest.RESTClient.delete_portfolio

Futures
----------------------------

.. autofunction:: coinbase.rest.RESTClient.get_futures_balance_summary
.. autofunction:: coinbase.rest.RESTClient.list_futures_positions
.. autofunction:: coinbase.rest.RESTClient.get_futures_position
.. autofunction:: coinbase.rest.RESTClient.schedule_futures_sweep
.. autofunction:: coinbase.rest.RESTClient.list_futures_sweeps
.. autofunction:: coinbase.rest.RESTClient.cancel_pending_futures_sweep
.. autofunction:: coinbase.rest.RESTClient.get_intraday_margin_setting
.. autofunction:: coinbase.rest.RESTClient.get_current_margin_window
.. autofunction:: coinbase.rest.RESTClient.set_intraday_margin_setting

Perpetuals
---------------------------

.. autofunction:: coinbase.rest.RESTClient.allocate_portfolio
.. autofunction:: coinbase.rest.RESTClient.get_perps_portfolio_summary
.. autofunction:: coinbase.rest.RESTClient.list_perps_positions
.. autofunction:: coinbase.rest.RESTClient.get_perps_position
.. autofunction:: coinbase.rest.RESTClient.get_perps_portfolio_balances
.. autofunction:: coinbase.rest.RESTClient.opt_in_or_out_multi_asset_collateral

Fees
-------------------------

.. autofunction:: coinbase.rest.RESTClient.get_transaction_summary

Converts
----------------------------

.. autofunction:: coinbase.rest.RESTClient.create_convert_quote
.. autofunction:: coinbase.rest.RESTClient.get_convert_trade
.. autofunction:: coinbase.rest.RESTClient.commit_convert_trade

Public
---------------------------

.. autofunction:: coinbase.rest.RESTClient.get_unix_time
.. autofunction:: coinbase.rest.RESTClient.get_public_product_book
.. autofunction:: coinbase.rest.RESTClient.get_public_products
.. autofunction:: coinbase.rest.RESTClient.get_public_product
.. autofunction:: coinbase.rest.RESTClient.get_public_candles
.. autofunction:: coinbase.rest.RESTClient.get_public_market_trades

Payments
-------------------------------

.. autofunction:: coinbase.rest.RESTClient.list_payment_methods
.. autofunction:: coinbase.rest.RESTClient.get_payment_method

Data API
-------------------------------

.. autofunction:: coinbase.rest.RESTClient.get_api_key_permissions