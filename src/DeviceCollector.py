from web3 import Web3,HTTPProvider
import AshyaRegistry_ABI, device_ABI
from flask import Flask
import threading, json, time
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)   

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
        DeviceColletor.write_contract(DeviceColletor.data,"/etc/ashya/device_contract.json") 
        DeviceColletor.read_contract()
        
    def write_contract(json_data, fileName): 
        file_name = fileName 
        with open(file_name, 'w') as outfile:
            json.dump(json_data, outfile)
            
    def read_contract():
        file_name = "/etc/ashya/device_contract.json"   
        with open(file_name, "r") as f:         
               print(json.load(f))     

@app.route("/urls", methods=['GET'])
@cross_origin()      
def Collect_Urls():
        web3 = Web3(HTTPProvider('https://kovan.infura.io/'))
        print (web3, "web3")
        address = Web3.toChecksumAddress('0x0d7B49A97775EbC2a42D0105bEF7086F9bD92722')
        contract = web3.eth.contract(address=address, abi = device_ABI.abi)
        nb = contract.functions.getURLCount().call()
        for i in range(0,nb):
            urls = contract.functions.urls(i).call() 
            DeviceColletor.write_contract(urls, "/etc/ashya/urls.json")
            print(urls)
            return urls
        
def do_stuff():
    with app.test_request_context():
        while True:  
            Collect_Urls()
            time.sleep(15)  

with app.test_request_context():           
    _thread = threading.Thread(target=do_stuff)
    _thread.setDaemon(True)
    _thread.start()

if __name__ == "__main__":
    print ("Script has started...")
    DeviceColletor.main()
    do_stuff()
    app.run(port=5050, debug = True)
    print ("Script has ended...")
