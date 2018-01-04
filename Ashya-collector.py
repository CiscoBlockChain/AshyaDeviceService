from flask import Flask
#import requests
import json
import threading
import time



class JsonF():
     payload = open("urls.json").read()
     urls = json.loads(payload)

jsonF = JsonF()    
app = Flask(__name__)
   
@app.route("/urls", methods=['GET'])
def default():
        return (jsonF.payload)
    
        
def background():
 
        for link in jsonF.urls["urls"]:
            #response = requests.post(url=link, data=jsonF.payload)
            #print(response.json())
            print (link) 
            print("data sent inside for loop")

   

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
    