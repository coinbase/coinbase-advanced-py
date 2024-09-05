Websocket User API Client
=====================

WSUserClient Constructor
---------------------------

.. autoclass:: coinbase.websocket.WSUserClient

WebSocket Utils
---------------------------

.. autofunction:: coinbase.websocket.WSUserClient.open
.. autofunction:: coinbase.websocket.WSUserClient.open_async
.. autofunction:: coinbase.websocket.WSUserClient.close
.. autofunction:: coinbase.websocket.WSUserClient.close_async
.. autofunction:: coinbase.websocket.WSUserClient.subscribe
.. autofunction:: coinbase.websocket.WSUserClient.subscribe_async
.. autofunction:: coinbase.websocket.WSUserClient.unsubscribe
.. autofunction:: coinbase.websocket.WSUserClient.unsubscribe_async
.. autofunction:: coinbase.websocket.WSUserClient.unsubscribe_all
.. autofunction:: coinbase.websocket.WSUserClient.unsubscribe_all_async
.. autofunction:: coinbase.websocket.WSUserClient.sleep_with_exception_check
.. autofunction:: coinbase.websocket.WSUserClient.sleep_with_exception_check_async
.. autofunction:: coinbase.websocket.WSUserClient.run_forever_with_exception_check
.. autofunction:: coinbase.websocket.WSUserClient.run_forever_with_exception_check_async
.. autofunction:: coinbase.websocket.WSUserClient.raise_background_exception

Channels
-----------------------------

.. autofunction:: coinbase.websocket.WSUserClient.heartbeats
.. autofunction:: coinbase.websocket.WSUserClient.heartbeats_async
.. autofunction:: coinbase.websocket.WSUserClient.heartbeats_unsubscribe
.. autofunction:: coinbase.websocket.WSUserClient.heartbeats_unsubscribe_async
.. autofunction:: coinbase.websocket.WSUserClient.user
.. autofunction:: coinbase.websocket.WSUserClient.user_async
.. autofunction:: coinbase.websocket.WSUserClient.user_unsubscribe
.. autofunction:: coinbase.websocket.WSUserClient.user_unsubscribe_async
.. autofunction:: coinbase.websocket.WSUserClient.futures_balance_summary
.. autofunction:: coinbase.websocket.WSUserClient.futures_balance_summary_async
.. autofunction:: coinbase.websocket.WSUserClient.futures_balance_summary_unsubscribe
.. autofunction:: coinbase.websocket.WSUserClient.futures_balance_summary_unsubscribe_async

Exceptions
---------------------------

.. autofunction:: coinbase.websocket.WSUserClientException
.. autofunction:: coinbase.websocket.WSUserClientConnectionClosedException
