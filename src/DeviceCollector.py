from web3 import Web3,HTTPProvider
import AshyaRegistry_ABI
import json

class DeviceColletor():  
    addresses = []

    def write_contract(json_data):
        file_name = "device_contract.json"
        with open(file_name, 'w+') as outfile:
            json.dump(json_data, outfile)

    def read_contract():
        file_name = "device_contract.json"
        try:
            with open(file_name, "r") as f:
                return json.load(f)
        except:
                return{'address':[]}

    def main():
        web3 = Web3(HTTPProvider('https://kovan.infura.io/'))
        print (web3, "web3")
        address = Web3.toChecksumAddress('0xd32c3dd15f59490e49ffd7d5da2373808e4f9d21')
        contract = web3.eth.contract(address=address, abi=AshyaRegistry_ABI.abi)
        newAddresses = {}
    
        nb = contract.functions.getItemCount().call()
        print(nb)
        for i in range(0,nb):
            temp = contract.functions.getItemAtIndex(i).call()
            if DeviceColletor.addresses.count(temp) == 0:
                DeviceColletor.addresses.append(temp)
        print(DeviceColletor.addresses)

        newAddresses['address'] = DeviceColletor.addresses
        addresses = DeviceColletor.read_contract()
        for a in DeviceColletor.addresses:
            print(a)
            print(addresses)
            if (a not in addresses['address']):
                addresses['address'].append(a)

        DeviceColletor.write_contract(addresses)


               

if __name__ == "__main__":
    print ("Script has started...")
    DeviceColletor.main()
    print ("Script has ended...")
