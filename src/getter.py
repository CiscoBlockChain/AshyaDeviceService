from __future__ import absolute_import
import paho.mqtt.client as mqtt

topic = "yolo"
port = 1883
host = "iot.eclipse.org"
client= mqtt.Client()
 
def get_values():
    client.connect(host, port)
    recieved_msgs = client.subscribe(topic)
    for msg in recieved_msgs:
        print(msg)
    client.loop_start()
            
    
if __name__ == "__main__":
    get_values()
    
