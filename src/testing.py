from web3 import Web3, HTTPProvider
import json 

class testing:
  def tset(self):
      
    web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

    with open(('AshyaRegistry.json'), 'r') as abi_definition:
                   abi = json.load(abi_definition)
    
    #contract_address = web3.toChecksumAddress('0x3437369f1a8943092d4149b07c9bf48377981580') {
    testC = web3.eth.contract()
    testC.address = web3.toChecksumAddress('0x8d2f0474df7625026781f458cc19a4426382df75')
    print(testC.address)
    testC.abi = abi
    #print(testC.call().getItemCount())
    temp = web3.eth.getBalance(web3.toChecksumAddress(web3.eth.accounts[0]))
    print(web3.eth.accounts[0], "balance: ", web3.fromWei(temp, 'ether'))
    


c = testing()
c.tset()