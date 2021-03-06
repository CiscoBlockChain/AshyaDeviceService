from __future__ import absolute_import
from web3 import Web3,HTTPProvider
import  device_ABI
import requests
import json, sys,os
from flask import Flask, request, jsonify
import threading, time
from flask_cors import CORS, cross_origin
import paho.mqtt.client as mqtt
import logging


app = Flask(__name__)
CORS(app)  
#contract_file = "C:/CiscoBlockchain/web-service/src/etc/ashya/device_contract.json"
contract_file = "/app/contracts/device_contract.json"
MQTT_topic = "yolo"
MQTT_port = 1883
MQTT_host = os.environ.get("MQTT_HOST")
MQTT_client= mqtt.Client()
msg_payload = ""
logging.basicConfig(format='%(asctime)s %(message)s', level = logging.INFO)




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

def on_message(client, userdata, msg):
   print("message received " , str(msg.payload.decode("utf-8")))
   global msg_payload 
   msg_payload = str(msg.payload.decode("utf-8"))
       
@app.route("/urls", methods=['GET'])
@cross_origin()      
def get_urls():
    urls = collect_urls()    
    if urls:
        return jsonify({"urls" : urls}), 200
    return jsonify({"urls":[]}), 200

#1.Check to see if there is a contract on this device
#2. Get the subscribers of the device by querying the blockchain
def collect_urls():
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
           
def send_data_to_subscribers(): 
    try:
        MQTT_client.on_message = on_message
        MQTT_client.connect(MQTT_host,MQTT_port)
        while not MQTT_client.on_disconnect:
            urls = collect_urls()
            MQTT_client.subscribe(MQTT_topic)
            print("subscribing to" , MQTT_topic , "topic")
            print("sending data to: ", urls)
            for u in urls:
                if msg_payload != "":
                    print("Posting" ,msg_payload, "to", u)
                    r= requests.post(u, json.dumps(msg_payload))
                    logging.info("Delivered json data to suscribers %s" , r)
            MQTT_client.loop_start()
            time.sleep(10)
            
    except Exception as e:
        print("Could not connect to mqtt broker: ")
        print(e)
        sys.exit(1)
   
   
def do_stuff():
    """
    Enter into thread to send data to subscribers. 
    """
    with app.test_request_context():
        while True:  
            send_data_to_subscribers()
      
with app.test_request_context():           
    _thread = threading.Thread(target=do_stuff)
    _thread.setDaemon(True)
    _thread.start()
    

if __name__ == "__main__":
    print ("Script has started...")
    app.run(debug = True,host = '0.0.0.0',port=5050)
    do_stuff()
    print ("Script has ended...")

