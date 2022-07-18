from brownie import accounts, config, BasicStorage, network


def deploy_basic_storage():
    account = accounts.add(config["wallets"]["from_key"])
    basic_storage = BasicStorage.deploy({"from": account})
    stored_value = basic_storage.retrieve()
    print(stored_value)
    transaction = basic_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = basic_storage.retrieve()
    print(updated_stored_value)




def main(): 
    deploy_basic_storage()