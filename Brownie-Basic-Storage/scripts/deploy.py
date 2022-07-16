from brownie import accounts, config, BasicStorage, network

def deploy_basic_storage():
    first_account = accounts[0]
    print(first_account)

def main(): 
    deploy_basic_storage()