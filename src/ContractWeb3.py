from web3 import Web3,HTTPProvider
import device_ABI
from flask import Flask
import requests,threading
import time
from flask_cors import CORS, cross_origin

def main():
    web3 = Web3(HTTPProvider('https://kovan.infura.io/'))
    print (web3, "web3")
    #address = Web3.toChecksumAddress('0x8e31D93762Df74F4203F8b9950bcdc79F753d83E')
    address = Web3.toChecksumAddress('0x0d7B49A97775EbC2a42D0105bEF7086F9bD92722')
    contract = web3.eth.contract(address=address, abi=device_ABI.abi)

    nb = contract.functions.getURLCount().call()
    for i in range(0,nb):
        print(contract.functions.urls(i).call())
        


if __name__ == "__main__":
    print ("Script has started...")
    main()
    print ("Script has ended...")
