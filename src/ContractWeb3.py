from web3 import Web3, HTTPProvider, TestRPCProvider
import json
from flask import Flask
import requests, threading
import time
from flask_cors import CORS, cross_origin
#from solc import compile_source
#import contract_ABI
#http://dominikharz.me/blockchain/2017/02/14/ethereum-python-integration.html


class ContractWeb3:
    def test(self):
        contractAddress = '0x3437369f1a8943092d4149b07c9bf48377981580'
        web3 = Web3(TestRPCProvider(host='localhost', port='8545'))
 
        with open(('AshyaRegistry.json'), 'r') as abi_definition:
                 self.abi = json.load(abi_definition)
        self.contract_address = contractAddress
        self.contract = self.web3.eth.contract(self.abi, self.contract_address)
 
        wei_balance = web3.eth.getBalance('0xfe83a8d8fa65db48b00fbd8d1d0809c1d5979082')

        count = self.contract.call().getURLCount()
        print("hi")

        print(wei_balance)    
        
        
c = ContractWeb3()
c.test()
        
        
        

# =============================================================================
# class JsonF():
#      payload = open("urls.json").read()
#      urls = json.loads(payload)
# 
# jsonF = JsonF()    
# app = Flask(__name__)
# CORS(app)
#    
# @app.route("/urls", methods=['GET'])
# @cross_origin()
# def default():
#         return (jsonF.payload)
#             
# def background():
#  
#         for link in jsonF.urls["urls"]:
#             response = requests.post(url=link, data=jsonF.payload)
#             print(response.json())
#             print (link) 
#             print("data sent inside for loop")
# 
# def do_stuff():
#     while True:  
#         background()
#         time.sleep(5)
#     
# _thread = threading.Thread(target=do_stuff)
# _thread.setDaemon(True)
# _thread.start()
# 
# if __name__ == '__main__': 
#     app.run(port=5050, debug = True)
#     default()
#     do_stuff()
# =============================================================================
    