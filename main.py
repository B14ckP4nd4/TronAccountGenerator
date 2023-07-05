
from tronpy.keys import PrivateKey

import json

wallet = dict()

priv_key = PrivateKey.random()
wallet['private'] = str(priv_key)

account = priv_key.public_key.to_base58check_address()
wallet['address'] = str(account)

print(json.dumps(wallet))