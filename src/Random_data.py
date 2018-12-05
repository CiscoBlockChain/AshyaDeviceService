from __future__ import absolute_import
from kafka import KafkaProducer
from mimesis.schema import Field, Schema
import json

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

        
        
if __name__ == "__main__":
     kafka_connect()
