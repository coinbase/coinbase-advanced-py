Websocket API Client
=====================

WSClient Constructor
---------------------------

.. autoclass:: coinbase.websocket.WSClient

WebSocket Utils
---------------------------

.. autofunction:: coinbase.websocket.WSClient.open
.. autofunction:: coinbase.websocket.WSClient.open_async
.. autofunction:: coinbase.websocket.WSClient.close
.. autofunction:: coinbase.websocket.WSClient.close_async
.. autofunction:: coinbase.websocket.WSClient.subscribe
.. autofunction:: coinbase.websocket.WSClient.subscribe_async
.. autofunction:: coinbase.websocket.WSClient.unsubscribe
.. autofunction:: coinbase.websocket.WSClient.unsubscribe_async
.. autofunction:: coinbase.websocket.WSClient.unsubscribe_all
.. autofunction:: coinbase.websocket.WSClient.unsubscribe_all_async
.. autofunction:: coinbase.websocket.WSClient.sleep_with_exception_check
.. autofunction:: coinbase.websocket.WSClient.sleep_with_exception_check_async
.. autofunction:: coinbase.websocket.WSClient.run_forever_with_exception_check
.. autofunction:: coinbase.websocket.WSClient.run_forever_with_exception_check_async
.. autofunction:: coinbase.websocket.WSClient.raise_background_exception

Channels
-----------------------------

.. autofunction:: coinbase.websocket.WSClient.heartbeats
.. autofunction:: coinbase.websocket.WSClient.heartbeats_async
.. autofunction:: coinbase.websocket.WSClient.heartbeats_unsubscribe
.. autofunction:: coinbase.websocket.WSClient.heartbeats_unsubscribe_async
.. autofunction:: coinbase.websocket.WSClient.candles
.. autofunction:: coinbase.websocket.WSClient.candles_async
.. autofunction:: coinbase.websocket.WSClient.candles_unsubscribe
.. autofunction:: coinbase.websocket.WSClient.candles_unsubscribe_async
.. autofunction:: coinbase.websocket.WSClient.market_trades
.. autofunction:: coinbase.websocket.WSClient.market_trades_async
.. autofunction:: coinbase.websocket.WSClient.market_trades_unsubscribe
.. autofunction:: coinbase.websocket.WSClient.market_trades_unsubscribe_async
.. autofunction:: coinbase.websocket.WSClient.status
.. autofunction:: coinbase.websocket.WSClient.status_async
.. autofunction:: coinbase.websocket.WSClient.status_unsubscribe
.. autofunction:: coinbase.websocket.WSClient.status_unsubscribe_async
.. autofunction:: coinbase.websocket.WSClient.ticker
.. autofunction:: coinbase.websocket.WSClient.ticker_async
.. autofunction:: coinbase.websocket.WSClient.ticker_unsubscribe
.. autofunction:: coinbase.websocket.WSClient.ticker_unsubscribe_async
.. autofunction:: coinbase.websocket.WSClient.ticker_batch
.. autofunction:: coinbase.websocket.WSClient.ticker_batch_async
.. autofunction:: coinbase.websocket.WSClient.ticker_batch_unsubscribe
.. autofunction:: coinbase.websocket.WSClient.ticker_batch_unsubscribe_async
.. autofunction:: coinbase.websocket.WSClient.level2
.. autofunction:: coinbase.websocket.WSClient.level2_async
.. autofunction:: coinbase.websocket.WSClient.level2_unsubscribe
.. autofunction:: coinbase.websocket.WSClient.level2_unsubscribe_async
.. autofunction:: coinbase.websocket.WSClient.user
.. autofunction:: coinbase.websocket.WSClient.user_async
.. autofunction:: coinbase.websocket.WSClient.user_unsubscribe
.. autofunction:: coinbase.websocket.WSClient.user_unsubscribe_async
.. autofunction:: coinbase.websocket.WSClient.futures_balance_summary
.. autofunction:: coinbase.websocket.WSClient.futures_balance_summary_async
.. autofunction:: coinbase.websocket.WSClient.futures_balance_summary_unsubscribe
.. autofunction:: coinbase.websocket.WSClient.futures_balance_summary_unsubscribe_async

Exceptions
---------------------------

.. autofunction:: coinbase.websocket.WSClientException
.. autofunction:: coinbase.websocket.WSClientConnectionClosedException
