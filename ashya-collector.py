from flask import Flask
import requests
import json
import time

class JsonF():
    payload = open("urls.json").read()
    urls = json.loads(payload)

jsonF = JsonF()    
app = Flask(__name__)
   
@app.route("/urls", )
def default():
        return jsonF.payload
   
def send_data_loop():
    while True:
        print("sending data")
        payload = open("urls.json").read()
        urls = json.loads(payload)
        for link in jsonF.urls["urls"]:
            response = requests.post(url=link, data=jsonF.payload)
            print(response.json())
        time.sleep(5)


 
if __name__ == '__main__': 
    #app.run(port=5050, debug = True)
    send_data_loop()
    
        
