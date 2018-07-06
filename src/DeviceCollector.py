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
            
    def read_contract():
        file_name = "/etc/ashya/device_contract.json"   
        with open(file_name, "r") as f:  
            print(json.load(f))
               

if __name__ == "__main__":
    print ("Script has started...")
    DeviceColletor.main()
    print ("Script has ended...")
