from brownie import BasicStorage, accounts

def test_deploy():
    #Arrange
    account = accounts[0]

    #Act
    basic_storage = BasicStorage.deploy({"from": account})
    starting_value = basic_storage.retrieve() 
    expected = 0

    #Assert
    assert starting_value == expected

def test_updating_storage():
    #Arrange 
    account = accounts[0]
    basic_storage = BasicStorage.deploy({"from": account})

    #Act
    expected = 15
    basic_storage.store(15, {"from": account})

    #Assert
    assert expected == basic_storage.retrieve()