from brownie import BasicStorage, accounts, config

def read_contract():
    basic_storage = BasicStorage[-1] #most recent deployment
    #need to know ABI and address

    print(basic_storage.retrieve())

def main():
    read_contract()