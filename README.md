# Coinbase Advanced API Python SDK
[![PyPI version](https://badge.fury.io/py/coinbase-advanced-py.svg)](https://badge.fury.io/py/coinbase-advanced-py)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/license/apache-2-0/)
[![Code Style](https://img.shields.io/badge/code_style-black-black)](https://black.readthedocs.io/en/stable/)

Welcome to the official Coinbase Advanced API Python SDK. This python project was created to allow coders to easily plug into the [Coinbase Advanced API](https://docs.cloud.coinbase.com/advanced-trade-api/docs/welcome).
This SDK also supports easy connection to the [Coinbase Advanced Trade WebSocket API](https://docs.cloud.coinbase.com/advanced-trade-api/docs/ws-overview).

## Installation

```bash
pip3 install coinbase-advanced-py
```

## Cloud API Keys

This SDK uses the Coinbase Cloud API keys. To use this SDK, you will need to create a Coinbase Cloud API key and secret by following the instructions [here](https://docs.cloud.coinbase.com/advanced-trade-api/docs/auth#cloud-api-keys).
Make sure to save your API key and secret in a safe place. You will not be able to retrieve your secret again.

WARNING: We do not recommend that you save your API secrets directly in your code outside of testing purposes. Best practice is to use a secrets manager and access your secrets that way. You should be careful about exposing your secrets publicly if posting code that leverages this library.

Optional: Set your API key and secret in your environment (make sure to put these in quotation marks). For example:
```bash
export COINBASE_API_KEY="organizations/{org_id}/apiKeys/{key_id}"
export COINBASE_API_SECRET="-----BEGIN EC PRIVATE KEY-----\nYOUR PRIVATE KEY\n-----END EC PRIVATE KEY-----\n"
```

## REST API Client
In your code, import the RESTClient class and instantiate it:
```python
from coinbase.rest import RESTClient

client = RESTClient() # Uses environment variables for API key and secret
```
If you did not set your API key and secret in your environment, you can pass them in as arguments:
```python
from coinbase.rest import RESTClient

api_key = "organizations/{org_id}/apiKeys/{key_id}"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nYOUR PRIVATE KEY\n-----END EC PRIVATE KEY-----\n"

client = RESTClient(api_key=api_key, api_secret=api_secret)
```
After creating your API key, a json file will be downloaded to your computer. It's possible to  pass in the path to this file as an argument:
```python
client = RESTClient(key_file="path/to/coinbase_cloud_api_key.json")
```
We also support passing a file-like object as the `key_file` argument:
```python
from io import StringIO
client = RESTClient(key_file=StringIO('{"name": "key-name", "privateKey": "private-key"}'))
```
You can also set a timeout in seconds for your REST requests like so:
```python
client = RESTClient(api_key=api_key, api_secret=api_secret, timeout=5)
```

### Using the REST Client

You are able to use any of the API hooks to make calls to the Coinbase API. For example:
```python
from json import dumps

accounts = client.get_accounts()
print(dumps(accounts, indent=2))

order = client.market_order_buy(client_order_id="clientOrderId", product_id="BTC-USD", quote_size="1")
print(dumps(order, indent=2))
```
This code calls the `get_accounts` and `market_order_buy` endpoints.

Refer to the [Advanced API Reference](https://docs.cloud.coinbase.com/advanced-trade-api/reference) for detailed information on each exposed endpoint.
Look in the `coinbase.rest` module to see the API hooks that are exposed.

### Passing in additional parameters
Use `kwargs` to pass in any additional parameters. For example:
```python
kwargs = {
    "param1": 10,
    "param2": "mock_param"
}
product = client.get_product(product_id="BTC-USD", **kwargs)
```

### Generic REST Calls
You can make generic REST calls using the `get`, `post`, `put`, and `delete` methods. For example:
```python
market_trades = client.get("/api/v3/brokerage/products/BTC-USD/ticker", params={"limit": 5})

portfolio = client.post("/api/v3/brokerage/portfolios", data={"name": "TestPortfolio"})
```
Here we are calling the [GetMarketTrades](https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getmarkettrades) and [CreatePortfolio](https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_createportfolio) endpoints through the generic REST functions.
Once again, the built-in way to query these through the SDK would be:
```python
market_trades = client.get_market_trades(product_id="BTC-USD", limit=5)

portfolio = client.create_portfolio(name="TestPortfolio")
```

## WebSocket API Client
We offer a WebSocket API client that allows you to connect to the [Coinbase Advanced Trade WebSocket API](https://docs.cloud.coinbase.com/advanced-trade-api/docs/ws-overview).
Refer to the [Advanced Trade WebSocket Channels](https://docs.cloud.coinbase.com/advanced-trade-api/docs/ws-channels) page for detailed information on each offered channel.

In your code, import the WSClient class and instantiate it. The WSClient requires an API key and secret to be passed in as arguments. You can also use a key file or environment variables as described in the RESTClient instructions above.

You must specify an `on_message` function that will be called when a message is received from the WebSocket API. This function must take in a single argument, which will be the raw message received from the WebSocket API. For example:
```python
from coinbase.websocket import WSClient

api_key = "organizations/{org_id}/apiKeys/{key_id}"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nYOUR PRIVATE KEY\n-----END EC PRIVATE KEY-----\n"

def on_message(msg):
    print(msg)

client = WSClient(api_key=api_key, api_secret=api_secret, on_message=on_message)
```
In this example, the `on_message` function simply prints the message received from the WebSocket API.

You can also set a `timeout` in seconds for your WebSocket connection, as well as a `max_size` in bytes for the messages received from the WebSocket API.
```python
client = WSClient(api_key=api_key, api_secret=api_secret, on_message=on_message, timeout=5, max_size=65536) # 64 KB max_size
```
Other configurable fields are the `on_open` and `on_close` functions. If provided, these are called when the WebSocket connection is opened or closed, respectively. For example:
```python
def on_open():
    print("Connection opened!")

client = WSClient(api_key=api_key, api_secret=api_secret, on_message=on_message, on_open=on_open)
```

### Using the WebSocket Client
Once you have instantiated the client, you can connect to the WebSocket API by calling the `open` method, and disconnect by calling the `close` method.
The `subscribe` method allows you to subscribe to specific channels, for specific products. Similarly, the `unsubscribe` method allows you to unsubscribe from specific channels, for specific products. For example:

```python
# open the connection and subscribe to the ticker and heartbeat channels for BTC-USD and ETH-USD
client.open()
client.subscribe(product_ids=["BTC-USD", "ETH-USD"], channels=["ticker", "heartbeats"])

# wait 10 seconds
time.sleep(10)

# unsubscribe from the ticker channel and heartbeat channels for BTC-USD and ETH-USD, and close the connection
client.unsubscribe(product_ids=["BTC-USD", "ETH-USD"], channels=["ticker", "heartbeats"])
client.close()
```

We also provide channel specific methods for subscribing and unsubscribing. For example, the below code is equivalent to the example from above:
```python
client.open()
client.ticker(product_ids=["BTC-USD", "ETH-USD"])
client.heartbeats(product_ids=["BTC-USD", "ETH-USD"])

# wait 10 seconds
time.sleep(10)

client.ticker_unsubscribe(product_ids=["BTC-USD", "ETH-USD"])
client.heartbeats_unsubscribe(product_ids=["BTC-USD", "ETH-USD"])
client.close()
```

### Automatic Reconnection to the WebSocket API
The WebSocket client will automatically attempt to reconnect the WebSocket API if the connection is lost, and will resubscribe to any channels that were previously subscribed to.

The client uses an exponential backoff algorithm to determine how long to wait before attempting to reconnect, with a maximum number of retries of 5.

If you do not want to automatically reconnect, you can set the `retry` argument to `False` when instantiating the client.
```python
client = WSClient(api_key=api_key, api_secret=api_secret, on_message=on_message, retry=False)
```

### Catching WebSocket Exceptions
The WebSocket API client will raise exceptions if it encounters an error. On forced disconnects it will raise a `WSClientConnectionClosedException`, otherwise it will raise a `WSClientException`.

NOTE: Errors on forced disconnects, or within logic in the message handler, will not be automatically raised since this will be running on its own thread.

We provide the `sleep_with_exception_check` and `run_forever_with_exception_check` methods to allow you to catch these exceptions. `sleep_with_exception_check` will sleep for the specified number of seconds, and will check for any exception raised during that time. `run_forever_with_exception_check` will run forever, checking for exceptions every second. For example:

```python
from coinbase.websocket import (WSClient, WSClientConnectionClosedException,
                                WSClientException)

client = WSClient(api_key=api_key, api_secret=api_secret, on_message=on_message)

try:
    client.open()
    client.subscribe(product_ids=["BTC-USD", "ETH-USD"], channels=["ticker", "heartbeats"])
    client.run_forever_with_exception_check()
except WSClientConnectionClosedException as e:
    print("Connection closed! Retry attempts exhausted.")
except WSClientException as e:
    print("Error encountered!")
```

This code will open the connection, subscribe to the ticker and heartbeat channels for BTC-USD and ETH-USD, and will sleep forever, checking for exceptions every second. If an exception is raised, it will be caught and handled appropriately.

If you only want to run for 5 seconds, you can use `sleep_with_exception_check`:
```python
client.sleep_with_exception_check(sleep=5)
```

Note that if the automatic reconnection fails after the retry limit is reached, a `WSClientConnectionClosedException` will be raised.

If you wish to implement your own reconnection logic, you can catch the `WSClientConnectionClosedException` and handle it appropriately. For example:
```python
client = WSClient(api_key=api_key, api_secret=api_secret, on_message=on_message, retry=False)

def connect_and_subscribe():
    try:
        client.open()
        client.subscribe(product_ids=["BTC-USD", "ETH-USD"], channels=["ticker", "heartbeats"])
        client.run_forever_with_exception_check()
    except WSClientConnectionClosedException as e:
        print("Connection closed! Sleeping for 20 seconds before reconnecting...")
        time.sleep(20)
        connect_and_subscribe()
```

### Async WebSocket Client
The functions described above handle the asynchronous nature of WebSocket connections for you. However, if you wish to handle this yourself, you can use the `async_open`, `async_subscribe`, `async_unsubscribe`, and `async_close` methods.

We similarly provide async channel specific methods for subscribing and unsubscribing such as `ticker_async`, `ticker_unsubscribe_async`, etc.

## Debugging the Clients
You can enable debug logging for the REST and WebSocket clients by setting the `verbose` variable to `True` when initializing the clients. This will log useful information throughout the lifecycle of the REST request or WebSocket connection, and is highly recommended for debugging purposes.
```python
rest_client = RESTClient(api_key=api_key, api_secret=api_secret, verbose=True)

ws_client = WSClient(api_key=api_key, api_secret=api_secret, on_message=on_message, verbose=True)
```

## Authentication
Authentication of Cloud API Keys is handled automatically by the SDK when making a REST request or sending a WebSocket message.

However, if you wish to handle this yourself, you must create a JWT token and attach it to your request as detailed in the Cloud API docs [here](https://docs.cloud.coinbase.com/advanced-trade-api/docs/rest-api-auth#making-requests). Use the built in `jwt_generator` to create your JWT token. For example:
```python
from coinbase import jwt_generator

api_key = "organizations/{org_id}/apiKeys/{key_id}"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nYOUR PRIVATE KEY\n-----END EC PRIVATE KEY-----\n"

uri = "/api/v3/brokerage/orders"

jwt_uri = jwt_generator.format_jwt_uri("POST", uri)
jwt = jwt_generator.build_rest_jwt(jwt_uri, api_key, api_secret)
```
This will create a JWT token for the POST `/api/v3/brokerage/orders` endpoint. Pass this JWT token in the `Authorization` header of your request as:
`
"Authorization": "Bearer " + jwt
`

You can also generate JWTs to use with the Websocket API. These do not require passing a specific URI. For example:
```python
from coinbase import jwt_generator

api_key = "organizations/{org_id}/apiKeys/{key_id}"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nYOUR PRIVATE KEY\n-----END EC PRIVATE KEY-----\n"

jwt = jwt_generator.build_ws_jwt(api_key, api_secret)
```
Use this JWT to connect to the Websocket API by setting it in the "jwt" field of your subscription requests. See the docs [here](https://docs.cloud.coinbase.com/advanced-trade-api/docs/ws-overview#sending-messages-using-cloud-api-keys) for more details.

## Changelog
For a detailed list of changes, see the [Changelog](https://github.com/coinbase/coinbase-advanced-py/blob/master/CHANGELOG.md).

## Contributing

If you've found a bug within this project, open an issue on this repo and add the "bug" label to it.
If you would like to request a new feature, open an issue on this repo and add the "enhancement" label to it.
Direct concerns or questions on the API to the [Advanced API Developer Forum](https://forums.coinbasecloud.dev/c/advanced-trade-api/20).
