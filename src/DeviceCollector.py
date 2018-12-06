from __future__ import absolute_import
from web3 import Web3,HTTPProvider
import  device_ABI
import requests
import json, os, sys
from flask import Flask, request, jsonify
import threading, time
from flask_cors import CORS, cross_origin
from kafka import KafkaConsumer

app = Flask(__name__)
CORS(app)  
#contract_file = "C:/CiscoBlockchain/web-service/src/etc/ashya/device_contract.json"
contract_file = "/app/contracts/device_contract.json"
kafka_service = os.environ['KAFKA_HOST']
kafka_topic = 'yolo'


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
    """
    1. Check to see if there is a contract on this device
    2. Get the subscribers of the device by querying the blockchain
    """
    urls = []
    contractHash = read_contract(contract_file)
    print(contractHash)
    # make sure there is a contract in place.
    if not 'address' in contractHash:
        return urls
    address = contractHash["address"]
    print("address: {0}".format(address))
    if address:   
        web3 = Web3(HTTPProvider('https://kovan.infura.io/'))
        contract = web3.eth.contract(address= address, abi = device_ABI.abi)
        nb = contract.functions.getURLCount().call()
        for i in range(0,nb):
            urls.append(contract.functions.urls(i).call())
    return urls
           
def send_data_to_subscribers(urls): 
    """
    Sending data to the subscribers
    """
    try:
        consumer = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_service)
    except Exception as e:
        print("Could not connect to Kafka service: ", kafka_service)
        print(e)
        
        sys.exit(1)

    for msg in consumer:
        for u in urls:
            print(msg)
            requests.post(u, data=json.dumps(msg))
    consumer.close()


def do_stuff():
    with app.test_request_context():
        while True:  
            urls = collect_urls()
            send_data_to_subscribers(urls)
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
