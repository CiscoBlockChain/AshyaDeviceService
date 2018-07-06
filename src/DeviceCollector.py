<<<<<<< HEAD
from web3 import Web3,HTTPProvider
import AshyaRegistry_ABI
import json

class DeviceColletor():  
    data = []
    
    
    def main():
        web3 = Web3(HTTPProvider('https://kovan.infura.io/'))
        print (web3, "web3")
        address = Web3.toChecksumAddress('0xd32c3dd15f59490e49ffd7d5da2373808e4f9d21')
        contract = web3.eth.contract(address=address, abi=AshyaRegistry_ABI.abi)
    
        nb = contract.functions.getItemCount().call()
        for i in range(0,nb):
            temp = contract.functions.getItemAtIndex(i).call()
            if DeviceColletor.data.count(temp) == 0:
                DeviceColletor.data.append(temp)
        print(DeviceColletor.data)
        DeviceColletor.write_contract(DeviceColletor.data)  
    

    def write_contract(json_data): 
        file_name = "/etc/ashya/device_contract.json"   
        with open(file_name, 'w') as outfile:
            json.dump(json_data, outfile)
               

if __name__ == "__main__":
    print ("Script has started...")
    DeviceColletor.main()
=======
from web3 import Web3,HTTPProvider
import AshyaRegistry_ABI
import json
    
    
def main():
    data = []
    web3 = Web3(HTTPProvider('https://kovan.infura.io/'))
    print (web3, "web3")
    address = Web3.toChecksumAddress('0x3437369f1a8943092d4149b07c9bf48377981580')
    contract = web3.eth.contract(address=address, abi=AshyaRegistry_ABI.abi)

    nb = contract.functions.getItemCount().call()
    for i in range(0,nb):
            data.append(contract.functions.getItemAtIndex(i).call())
    print(data)
    write_contract(data)  
    

def write_contract(json_data): 
    file_name = "/etc/ashya/device_contract.json"   
    with open(file_name, 'w') as outfile:
        json.dump(json_data, outfile)
               

if __name__ == "__main__":
    print ("Script has started...")
    main()
>>>>>>> a8905af5f772e173d01834a2718da9c72485fe2e
    print ("Script has ended...")