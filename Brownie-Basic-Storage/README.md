# Brownie-Basic-Storage
Uses the brownie framework to make a state change to a simple smart contract and then deploys it on a local blockchain (ganache CLI) or Rinkeby test net (Does the same thing as Web3-Basic-Storage but uses brownie with the addition of testing capabilities and a contract reader.)

Some file/folder descriptions: 
 >  - contracts/BasicStorage.sol is the basic storage example smart contract
 >  - scripts/deploy.py compiles the .sol code, connects to ganache, and then builds, signs, and sends a transaction
  >  - tests/test_basic_storage runs transactions tests
  > - build/deployments contains all past deployments separated by chain id
    > - scripts/read.py reads the contract and can find certain args

To deploy locally: 
 > 1. ensure local enviorment is configured with Ganache 
 > 2. change properties in deploy.py and .env accordingly (update address key, private key)
 > 3. brownie run scripts/deploy.py

To deploy to rinkeby:
 > 1. change properties in deploy.py and .env accordingly (update address key, private key)
 > 2. brownie run scripts/deploy.py --network rinkeby

 To read deployed contract:
 > 1. brownie run scripts/read.py --network rinkeby

 To run tests:
 > 1. brownie test 
 > 2. for one function: brownie test -k functionName
 > 3. for PDB py shell test: brownie test --pdb
 > 4. for more desc: brownie test -s

 To use brownie console:
> 1. brownie console


Notes: 
> Either create an .env or run locally: export $PRIVATE_KEY={insert private key} to insert a private key (DON'T USE REAL). 
> Currently configred for local ganache enviorment 