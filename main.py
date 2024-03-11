import time
from datetime import datetime, timedelta
from json import dumps

from coinbase.jwt_generator import build_rest_jwt
from coinbase.rest import RESTClient
from coinbase.rest.accounts import get_accounts
from coinbase.rest.rest_base import RESTBase
from coinbase.rest.staging_client import StagingRESTClient
from coinbase.websocket import WSClient

# ###PROD
api_key = "organizations/580a132a-4496-40c8-bda9-024a5a70d29c/apiKeys/8168323d-51ec-4b08-9fa1-ee1c05e610d0"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIMglnytj2g+tOQA+/pIVlAM2r67V7+Hggw4dMrK7P8+ToAoGCCqGSM49\nAwEHoUQDQgAE0ers7u+7pukmPtJVQEdtXoVpwnb2aVAs4iMwaa5X1dh70phRWRld\ndGH47vIatWlO1grdbnouWooIDXxVu1hR0w==\n-----END EC PRIVATE KEY-----\n"

###STAGING
# api_key = "organizations/c3b33303-9d4c-4750-9c55-82cc94282138/apiKeys/86a0cb1f-149e-4ba2-8cbd-889e7db7a43e"
# api_secret =  "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIDF8Bubw+q63aLtc5ITDPAUgilT8+Q13MftsRSlzMs56oAoGCCqGSM49\nAwEHoUQDQgAElUxG+v93MlCaKMuIcq0J+9RJkIfdTVcTw+qODnYez6XX4lA3FdfF\njUbcNMndIBPoNU7n02s1oiWBRqED0J88SQ==\n-----END EC PRIVATE KEY-----\n"
#
#
client = RESTClient(api_key=api_key, api_secret=api_secret)
# client = StagingRESTClient(api_key=api_key, api_secret=api_secret)

# payments = client.get_payment_methods()
# print(dumps(payments, indent=2))
#
# payments = client.get_payment_method("b8e7a64f-62d8-50cf-8b71-1a26492aba25")
# print(dumps(payments, indent=2))

# print(build_rest_jwt("GET https://api.coinbase.com/api/v3/brokerage/accounts", api_key, api_secret))
# print(client.get_unix_time())
# print("test")
#
# print(client.get_unix_time())
start_time = time.time()
accounts = client.get_accounts(start_time)
print((time.time() - start_time) * 1000)

# print(build_rest_jwt(uri="https://api.coinbase.com/api/v3/brokerage/accounts", key_var=api_key, secret_var=api_secret))
#


# order = client.limit_order_ioc(
#     client_order_id="08789aaada9a279aaA",
#     product_id="BTC-USDC",
#     side="SELL",
#     base_size="0.0001",
#     limit_price="50000",
# )


#  order_configuration= {
#                                 "market_market_ioc": {
#                                     "quote_size": "10"
#                                 }}

# print('AFTER', new_string)
# order = client.market_order(client_order_id="08789aafsaaa3d9279", product_id="BTC-USDC", side="BUY",
#                                    quote_size="10", )

# print(dumps(order, indent=2))
#
# order = client.preview_limit_order_ioc(
#     product_id="BTC-USDC", side="SELL", base_size="0.0001", limit_price="50000"
# )
#
# print(dumps(order, indent=2))


# def on_message(msg):
#     print("Message: ", msg)
#
#
# def on_open():
#     print("Connection opened!")
#
#
# client = WSClient(
#     api_key=api_key,
#     api_secret=api_secret,
#     on_message=on_message,
#     on_open=on_open,
#     verbose=True,
# )
#
# client.open()
#
# while True:
#     print("---")
#     time.sleep(5)
#     client.subscribe(["BTC-USD"], ["ticker"])
#
#     time.sleep(5)
#     client.unsubscribe_all()
#     client.unsubscribe_all()
#     time.sleep(5)
# client.close()
