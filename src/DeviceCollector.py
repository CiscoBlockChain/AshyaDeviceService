from __future__ import absolute_import
from web3 import Web3,HTTPProvider
import  device_ABI
import requests
from mimesis.schema import Field, Schema
import json
from flask import Flask, request, jsonify
import threading, time
from flask_cors import CORS, cross_origin
from kafka import KafkaProducer

app = Flask(__name__)
CORS(app)  
contract_file = "C:/CiscoBlockchain/web-service/src/etc/ashya/device_contract.json"
contract_file = "/app/device_contract.json"


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
            payload = generate()
            print("from collect urls")
            print(payload)
            requests.post(urls(i), data= json.dumps(payload))
        print(urls)  
    return urls
            
#retriving data from kafka service and send them to DeviceUrl        
def kafka_connect():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    print("here")
    temp = generate()   
    try:
        val = json.dumps(temp).encode()
        producer.send('test', value=val)
        #producer.send("test", temp)
        producer.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))
        
def generate():
    _ = Field('en')
    description = (
    lambda: {
        'timestamp': _('timestamp', posix=False),
        'id': _('uuid'),
        'name': _('text.word'),
        'owner': {
                'token': _('token')
                },
                }
        )
    schema = Schema(schema=description)
    r = schema.create(iterations=1)
    print(r)
    return r      
 
def do_stuff():
    with app.test_request_context():
        while True:  
            collect_urls()
            kafka_connect()
            time.sleep(5)  
      
with app.test_request_context():           
    _thread = threading.Thread(target=do_stuff)
    _thread.setDaemon(True)
    _thread.start()
    

if __name__ == "__main__":
    print ("Script has started...")
    app.run(debug = True,host = '0.0.0.0',port=5050)
    do_stuff()
    print ("Script has ended...")
