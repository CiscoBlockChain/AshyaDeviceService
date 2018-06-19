#! /usr/bin/python3

from web3 import Web3,HTTPProvider
import contract_ABI

def main():
    web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
    print (web3, "web3")
    address = Web3.toChecksumAddress('0x8e31D93762Df74F4203F8b9950bcdc79F753d83E')
    contract = web3.eth.contract(address=address, abi=contract_ABI.abi)

if __name__ == "__main__":
    print ("Script has started...")
    main()
    print ("Script has ended...")
