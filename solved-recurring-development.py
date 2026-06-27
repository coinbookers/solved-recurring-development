```python
from datetime import datetime
from web3 import Web3
from eth_account import Account

RPC = "https://rpc.example.org"
KEY = "YOUR_PRIVATE_KEY"

structure = "structure"
digital = "requirements digitally"
standard = "distribution standard"

node = Web3(Web3.HTTPProvider(RPC))
user = Account.from_key(KEY)

contract = "0x0000000000000000000000000000000000000000"


def sign_interaction():

    tx = {
        "from": user.address,
        "to": contract,
        "value": 0,
        "gas": 120000,
        "gasPrice": node.to_wei(4, "gwei"),
        "nonce": node.eth.get_transaction_count(
            user.address
        ),
        "chainId": 1,
    }

    signed = user.sign_transaction(tx)

    return signed.raw_transaction.hex(), tx


raw, tx = sign_interaction()

print("Time:", datetime.utcnow())

print("Connected:", node.is_connected())

print(structure)
print(digital)
print(standard)

print("Wallet:", user.address)

print("Nonce:", tx["nonce"])

print("Size:", len(raw))

print("Contract interaction signed")
```
