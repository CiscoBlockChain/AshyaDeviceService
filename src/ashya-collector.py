from flask import Flask
import requests, json, threading
import time
from flask_cors import CORS, cross_origin

class JsonF():
     payload = open("urls.json").read()
     urls = json.loads(payload)

jsonF = JsonF()    
app = Flask(__name__)
CORS(app)
   
@app.route("/urls", methods=['GET'])
@cross_origin()
def default():
        return (jsonF.payload)


@app.route("/contract", methods=['POST', 'GET'])
@cross_origin()
def contract():
    if (method == "POST"):
        # takes in argument of a contract { "contract" : "0x4ffff..." }
        write_contract()       
    elif(method == "GET"):
        return contract_address

def background():
 
        for link in jsonF.urls["urls"]:
            response = requests.post(url=link, data=jsonF.payload)
            print(response.json())
            print (link) 
            print("data sent inside for loop")
            
def write_contract(json_data): 
    file_name = "/etc/ashya/device_contract.json"   
    with open(file_name, "w") as f:
        f.write(json_data.dump)
    
def read_contract():
    file_name = "/etc/ashya/device_contract.json"   
    with open(file_name, "r") as f: 
        

def do_stuff():
    while True:  
        background()
        time.sleep(5)
    
_thread = threading.Thread(target=do_stuff)
_thread.setDaemon(True)
_thread.start()


if __name__ == '__main__': 
    app.run(port=5050, debug = True)
    default()
    do_stuff()
    
