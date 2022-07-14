from solcx import compile_standard, install_solc
import os
import json
from web3 import Web3

# loading .env file
from dotenv import load_dotenv

load_dotenv()

with open("./BasicStorage.sol", "r") as file:
    basic_storage_file = file.read()

SOLCX_VERSION = "0.8.0"


print("Installing solc", SOLCX_VERSION, "...")
install_solc(SOLCX_VERSION)

# Solidity source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"BasicStorage.sol": {"content": basic_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

with open("compiled.json", "w") as file:
    json.dump(compiled_sol, file)


# connecting to ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = "0xd0B12A040403bB0605526C1CB4575593BE6a15c8"

# THIS IS NOT A REAL PRIVATE KEY, GENERATED FROM GANACHE
_private_key = os.getenv("PRIVATE_KEY")
# print(_private_key)

# Getting bytecode
bs_bytecode = compiled_sol["contracts"]["BasicStorage.sol"]["BasicStorage"]["evm"][
    "bytecode"
]["object"]

# Getting abi
bs_abi = compiled_sol["contracts"]["BasicStorage.sol"]["BasicStorage"]["abi"]
BasicStorage = w3.eth.contract(abi=bs_abi, bytecode=bs_bytecode)

nonce = w3.eth.getTransactionCount(my_address)


# 1. build trans
# 2. sign a trans
# 3. send a trans
print("\nBuilding contract...")
transaction = BasicStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)

print("Signing contract...")
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=_private_key)

# sending signed contract
print("Sending contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# waiting for block comfirmation
print("Waiting for comfirmation...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Contract uploaded succesfully.")

# Working with contract
# Contract address
# Contract abi

basic_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=bs_abi)

# call: no state change
# transact: state change

# init fav number
print("\nFirst receive call (no store): ")
print(basic_storage.functions.retrieve().call())

# print(basic_storage.functions.store(15).call())

print("\nUpdating contract...")
store_transaction = basic_storage.functions.store(15).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1,
    }
)

signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=_private_key
)


send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)



tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
print("Waiting for chain..")

print("Contract update successful.")

print("\nSecond retrieve call (after store): ")

print(basic_storage.functions.retrieve().call())

