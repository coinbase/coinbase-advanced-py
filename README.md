# Coinbase Advanced Trading API Python SDK

Welcome to the official Coinbase Advanced Trading API Python SDK. This python project was created to allow coders to easily plug into the [Coinbase Advanced Trade API](https://docs.cloud.coinbase.com/advanced-trade-api/docs/welcome).

## Installation

To install, please clone this git repo, cd into the root and run:
```bash
pip3 install .
```

## Cloud API Keys

This SDK uses the Coinbase Cloud API keys. To use this SDK, you will need to create a Coinbase Cloud API key and secret. You can do this by following the instructions [here](https://docs.cloud.coinbase.com/advanced-trade-api/docs/auth#cloud-api-keys).
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
You can also set a timeout in seconds for your REST requests like so:
```python
client = RESTClient(api_key=api_key, api_secret=api_secret, timeout=5)
```

### Using the Client

You can then use any of the API hooks to make calls to the Coinbase API. For example:
```python
from json import dumps

accounts = client.get_accounts()
print(dumps(accounts, indent=2))

order = client.market_order_buy("clientOrderId", "BTC-USD", "1")
print(dumps(order, indent=2))
```
This code calls the `get_accounts` and `market_order_buy` endpoints.

You can refer to the [Advanced Trade API Reference](https://docs.cloud.coinbase.com/advanced-trade-api/reference) for detailed information on each exposed endpoint.
You can look at the following [mapping](Todo--add link here) to see which API hook corresponds to which endpoint.


### Passing in additional parameters
You can use `kwargs` to pass in any additional parameters. For example:
```python
kwargs = {
    "param1": 10,
    "param2": "mock_param"
}
product = client.get_product(product_id="BTC-USD", **kwargs)
```

### Generic REST Calls
You can also make generic REST calls using the `get`, `post`, `put`, and `delete` methods. For example:
```python
market_trades = client.get("/api/v3/brokerage/products/BTC-USD/ticker", params={"limit": 5})

portfolio = client.post("/api/v3/brokerage/portfolios", data={"name": "TestPortfolio"})
```
Here we are calling the [GetMarketTrades](https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getmarkettrades) and [CreatePortfolio](https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_createportfolio) endpoints through the generic REST functions.
Once again, the built in way to query these through the SDK would be:
```python
market_trades = client.get_market_trades("BTC-USD", 5)

portfolio = client.create_portfolio("TestPortfolio")
```

## Authentication
Authentication of Cloud API Keys is handled automatically by the SDK when making a REST request.

However, if you wish to handle this yourself, you must create a JWT token and attach it to your request as detailed in the Cloud API docs [here](https://docs.cloud.coinbase.com/advanced-trade-api/docs/rest-api-auth#making-requests). You can use the built in `jwt_generator` to create your JWT token. For example:
```python
from coinbase import jwt_generator

api_key = "organizations/{org_id}/apiKeys/{key_id}"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nYOUR PRIVATE KEY\n-----END EC PRIVATE KEY-----\n"

uri = "/api/v3/brokerage/orders"

jwt_uri = jwt_generator.format_jwt_uri("POST", uri)
jwt = jwt_generator.build_rest_jwt(jwt_uri, api_key, api_secret)
```
This will create a JWT token for the POST `/api/v3/brokerage/orders` endpoint. You can then pass this JWT token in the `Authorization` header of your request as:
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
You can use this JWT to connect to the Websocket API by setting it in the "jwt" field of your subscription requests. See the docs [here](https://docs.cloud.coinbase.com/advanced-trade-api/docs/ws-overview#sending-messages-using-cloud-api-keys) for more details.

## Contributing

If you've found a bug within this project, please open an issue on this repo and add the "bug" label to it.
If you would like to request a new feature, please open an issue on this repo and add the "enhancement" label to it.
Please direct concerns or questions on the API to the [Advanced Trade API Developer Forum](https://forums.coinbasecloud.dev/c/advanced-trade-api/20).
