from coinbase.rest import RESTClient

api_key = "organizations/580a132a-4496-40c8-bda9-024a5a70d29c/apiKeys/e0a2dbd7-04b9-4818-ab19-0cd31c011b18"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIDKz6+yFapaq1qxXr/zmhjMZgmdWytxETiviZ/sJhm2joAoGCCqGSM49\nAwEHoUQDQgAEdTND30oBg49TxDWTGR0SLouKU/5XkMqmwjpreb44MgVfOqc0dHnU\n/wuIOw9pioTirzG47igVvHTCX7ry/V5MyQ==\n-----END EC PRIVATE KEY-----\n"

client = RESTClient()
print(client.get_public_products())


#
# def on_message(msg):
#     print(msg)
#
#
# client = WSClient(on_message=on_message)
#
# client.open()
#
# client.user(product_ids=["BTC-USD"])
# # wait 10 seconds
# time.sleep(10)
#
# client.user_unsubscribe(product_ids=["BTC-USD"])
#
# client.close()
