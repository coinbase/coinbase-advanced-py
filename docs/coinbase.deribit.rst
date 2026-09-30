Global Derivatives Clients
==========================

Clients for Global Derivatives on the Deribit-powered gateway. Both use JSON-RPC 2.0 and the same CDP API keys as the rest of the SDK.

DeribitRetailClient (REST)
---------------------------

.. autoclass:: coinbase.deribit.DeribitRetailClient
   :members:
   :inherited-members:

DeribitRetailWSClient (WebSocket)
---------------------------------

Without keys, the client connects to the market data host. With keys, it connects to the trading host for ``user.*`` channels and RPC.

.. autoclass:: coinbase.deribit.DeribitRetailWSClient
   :members:
   :inherited-members:

Errors
---------------------------

.. autoexception:: coinbase.deribit.DeribitRPCError
.. autoexception:: coinbase.deribit.DeribitRateLimitError
.. autoexception:: coinbase.deribit.DeribitInsufficientFundsError
.. autoexception:: coinbase.deribit.DeribitInvalidParamsError
.. autoexception:: coinbase.deribit.DeribitMatchingQueueFullError
.. autoexception:: coinbase.deribit.DeribitAuthError
.. autoexception:: coinbase.deribit.DeribitConnectionError
.. autoexception:: coinbase.deribit.DeribitSubscriptionError
