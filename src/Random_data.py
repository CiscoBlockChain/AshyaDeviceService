from __future__ import absolute_import
from kafka import KafkaProducer
from faker_schema.faker_schema import FakerSchema
from faker_schema.schema_loader import load_json_from_string, load_json_from_file 
import json

json_string = '{{"2011-09-11 10:48:38.23": {"persons": 4,"umbrellas": 3,"chairs": 5}}'

def kafka_connect():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    temp = json_faker()
    print("here")
    try:
        producer = KafkaProducer(key_serializer=str.encode)
        producer.send('test', key='my message', value=str.encode(temp))
        producer.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))
        
def json_faker(): 
    schema = load_json_from_string(json_string)
    faker = FakerSchema()
    data = faker.generate_fake(schema)
    print(data)

        
        
if __name__ == "__main__":
    kafka_connect()
