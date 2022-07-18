# Brownie-Basic-Storage
Uses the brownie framework to make a state change to a simple smart contract and then deploys it on a local blockchain (ganache CLI) or Rinkeby test net (Does the same thing as Web3-Basic-Storage but uses brownie with the addition of testing capabilities.)

Some file/folder descriptions: 
 >  - contracts/BasicStorage.sol is the basic storage example smart contract
 >  - scripts/deploy.py compiles the .sol code, connects to ganache, and then builds, signs, and sends a transaction
  >  - tests/test_basic_storage runs transactions tests

Usage: 
 > 1. ensure local enviorment is configured with Ganache (if not using rinkeby)
 > 2. change properties in deploy.py accordingly (update address key, chain id, private key)
 > 3. brownie run scripts/deploy.py

Notes: 
> Either create an .env or run locally: export $PRIVATE_KEY={insert private key} to insert a private key (DON'T USE REAL). 
> Currently configred for local ganache enviorment 