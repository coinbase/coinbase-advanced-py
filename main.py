import json
import time

from coinbase.rest import RESTClient
from coinbase.websocket import WebsocketResponse, WSClient

# STAGING
# api_key = "organizations/c1decaa3-372a-41b7-b13b-68edabe98394/apiKeys/e49e2e58-5a7f-42c3-802b-10dce0fb9047"
# api_secret = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEICM+ltppB/4mHJxMnflZTe1dCCbXQ9hdYUeiEDKUt6CRoAoGCCqGSM49\nAwEHoUQDQgAEkvGEL9GBx6APBM8TNoTmtmelUcWT/N6taCWLGmoAw8MZRTesiQlw\nIV+0zvgEUgIfDxNMIrotR1g26ZHXgWRWeQ==\n-----END EC PRIVATE KEY-----\n"

# PROD
api_key = "organizations/580a132a-4496-40c8-bda9-024a5a70d29c/apiKeys/0c39a2ff-7bc8-4fe6-94d9-2649be2f81db"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIOG+sS5c6n71zzzZdAwo6tBzS2Mwm1HgHt7I+G9LaH1BoAoGCCqGSM49\nAwEHoUQDQgAEZPb5BnUVRAYAZY3yJzdw+5iVJCv1O0wc4BM2kfwIZWgj2jR977/m\ncfCrZlBXCMNc4AZHoWdt1f2MUtvt+dJdtQ==\n-----END EC PRIVATE KEY-----\n"


client = RESTClient(api_key=api_key, api_secret=api_secret, rate_limit_headers=True)
res = client.get_accounts()
print(res.accounts[0].platform)
print(type(res))

# public_products = client.get_public_products()
# print(json.dumps(public_products.to_dict(), indent=2))
# accounts = client.get_accounts();
# print(json.dumps(accounts.to_dict(), indent=2))


# def on_message(msg):
#     ws_object = WebsocketResponse(json.loads(msg))
#     # print(json.dumps(ws_object.to_dict(), indent=2))
#     if ws_object.channel == "ticker":
#         for event in ws_object.events:
#             print(json.dumps(event.to_dict(), indent=2))
#     #         for ticker in event.tickers:
#     #             print(ticker.product_id + ": " + ticker.price)
#
#
# client = WSClient(api_key=api_key, api_secret=api_secret, on_message=on_message)
#
# client.open()
# client.subscribe(product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"])
# time.sleep(10)
# client.unsubscribe(product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"])
# client.close()
