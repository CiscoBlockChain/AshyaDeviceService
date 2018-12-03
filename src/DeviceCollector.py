from __future__ import absolute_import
from web3 import Web3,HTTPProvider
import  device_ABI
import json
import requests
from flask import Flask, request, jsonify
import threading, time
from flask_cors import CORS, cross_origin
from kafka import KafkaConsumer

app = Flask(__name__)
CORS(app)  
<<<<<<< HEAD
contract_file = "C:/CiscoBlockchain/web-service/src/etc/ashya/device_contract.json"
=======
contract_file = "/app/device_contract.json"
>>>>>>> dc0bf2045365b0412b06cc61f9db861763421f33

@app.route("/contract", methods=['POST', 'GET'])
@cross_origin()
def contract():
    if (request.method == "POST"):
        return write_contract(request.json, contract_file)
    elif(request.method == "GET"):
        return jsonify(read_contract(contract_file))
  
def write_contract(json_data, file_name):
    print("json data: ", json_data)
    with app.test_request_context():
        with open(file_name, 'w+') as outfile:
            json.dump(json_data, outfile)  
        return jsonify(read_contract(file_name)), 201

def read_contract(file_name):
   try:
       with open(file_name, "r") as f:
           return json.load(f)
   except Exception as ex:
           print(ex)
           return {'address': ""}
       
@app.route("/urls", methods=['GET'])
@cross_origin()      
def get_urls():
    urls = collect_urls()    
    if urls:
        return jsonify({"urls" : urls}), 200
    return jsonify({"urls":[]}), 200

def collect_urls():
    urls = []
    contractHash = read_contract(contract_file)
    print(contractHash)
    if not 'address' in contractHash:
        return urls
    address = contractHash["address"]
    print("address: {0}".format(address))
    if address:   
        web3 = Web3(HTTPProvider('https://kovan.infura.io/'))
        contract = web3.eth.contract(address= address, abi = device_ABI.abi)
        nb = contract.functions.getURLCount().call()
        print(nb)
        for i in range(0,nb):
            urls = contract.functions.urls(i).call()
            payload = kafka_consumer()
            requests.post(urls(i), data= payload)
        print(urls)  
    return urls
            
#retriving data from kafka service and send them to DeviceUrl        
def kafka_consumer():
    values = []
    print(" insude consumer")
    consumer = KafkaConsumer('test')
    for message in consumer:
        print(message.value)
<<<<<<< HEAD
        values.append(message.value)

            
=======
        values.append(message.value)       
>>>>>>> dc0bf2045365b0412b06cc61f9db861763421f33
 
def do_stuff():
    with app.test_request_context():
        while True:  
            collect_urls()
            kafka_consumer()
            time.sleep(15)  
      
with app.test_request_context():           
    _thread = threading.Thread(target=do_stuff)
    _thread.setDaemon(True)
    _thread.start()
    

if __name__ == "__main__":
    print ("Script has started...")
    app.run(debug = True,host = '0.0.0.0',port=5050)
    do_stuff()
    print ("Script has ended...")
