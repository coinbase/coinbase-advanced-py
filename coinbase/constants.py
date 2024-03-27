from coinbase.__version__ import __version__

API_ENV_KEY = "COINBASE_API_KEY"
API_SECRET_ENV_KEY = "COINBASE_API_SECRET"
USER_AGENT = f"coinbase-advanced-py/{__version__}"

# REST Constants
BASE_URL = "api.coinbase.com"
API_PREFIX = "/api/v3/brokerage"
REST_SERVICE = "retail_rest_api_proxy"

# Websocket Constants
WS_BASE_URL = "wss://advanced-trade-ws.coinbase.com"
WS_SERVICE = "public_websocket_api"

WS_RETRY_MAX = 5
WS_RETRY_BASE = 5
WS_RETRY_FACTOR = 1.5

# Message Types
SUBSCRIBE_MESSAGE_TYPE = "subscribe"
UNSUBSCRIBE_MESSAGE_TYPE = "unsubscribe"

# Channels
HEARTBEATS = "heartbeats"
CANDLES = "candles"
MARKET_TRADES = "market_trades"
STATUS = "status"
TICKER = "ticker"
TICKER_BATCH = "ticker_batch"
LEVEL2 = "level2"
USER = "user"
