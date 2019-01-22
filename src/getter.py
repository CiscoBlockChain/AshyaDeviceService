from __future__ import absolute_import
import paho.mqtt.client as mqtt
import time

topic = "yolo"
port = 1883
host = "iot.eclipse.org"
client= mqtt.Client("p1")

def on_message(client, userdata, msg):
    print("message received " ,str(msg.payload.decode("utf-8"))) 
    
def get_values():
    client.on_message = on_message
    client.connect(host, port)
    while not client.on_disconnect:
        client.subscribe(topic)
        client.loop_start()
        time.sleep(4)
    recieved_msgs = client.subscribe(topic)
    for msg in recieved_msgs:
        print(msg)
    client.loop_start()

            
    
if __name__ == "__main__":
    get_values()
    
