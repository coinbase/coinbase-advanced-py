import os
import time
from json import dumps

import dill
import dill as pickle
import requests

from coinbase.rest import RESTClient

key = "organizations/580a132a-4496-40c8-bda9-024a5a70d29c/apiKeys/e6e16ce6-827a-405f-96d0-d6523758b14d"
secret = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIPhjuWXMPoQcrNm5IgMPDxonIA9c1bDS4ioBXqc6z0o/oAoGCCqGSM49\nAwEHoUQDQgAE+nni/csAlpdq35JYgc0Kp+E8nqbYrFO94aLT9o7CEJrUyLkpv1qY\n76fLprJ6fdQUTIz8wJx830/6YR6fvdW5lQ==\n-----END EC PRIVATE KEY-----\n"

client = RESTClient(api_key=key, api_secret=secret)
#
# client.get_unix_time()
# client.get_unix_time()
# client.get_unix_time()
# client.get_unix_time()
# client.get_unix_time()


client.get_accounts()
client.get_accounts()
client.get_accounts()
client.get_accounts()
client.get_accounts()


