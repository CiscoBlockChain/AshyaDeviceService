import web3
from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source, compile_files, link_code
from web3.auto import w3
from solc import compile_source
from web3 import Web3, HTTPProvider, TestRPCProvider
#import contract_ABI
import AshyaRegistry

# =============================================================================
# def get_Block_number():
#    my_provider = Web3(Web3.HTTPProvider("http://localhost:9545/"))
#    w3.eth.blockNumber
#    w3.eth.getBlock('latest')
# =============================================================================
   
compiled_sol = compile_source(AshyaRegistry) # Compiled source code
contract_interface = compiled_sol['<stdin>:Ashyaregistry']
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
   



#def check_whether_address_is_approved(contract):
    #return contractAddress.functions.getItemCount().call()

     #with open('ABI.json', 'r') as abi_definition:
         #abi = json.load(abi_definition)
         
     #web3 = Web3(HTTPProvider('http://127.0.0.1:5050'))
     #compiled_sol = compile_source(abi)
     #Device = web3.eth.contract(contractAddress,abi=abi)


#contract = Web3.EthereumTesterProvider.contract(address = contractAddress, abi = contract_ABI.abi)
