from __future__ import absolute_import
from kafka import KafkaProducer
import datetime
from faker_schema.faker_schema import FakerSchema
from faker_schema.schema_loader import  load_json_from_file


def kafka_connect():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    print("here")
    temp = json_faker()   
    try:
        key_bytes = bytes(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        value_bytes = bytes(temp, encoding='utf-8')
        producer.send("test", key=key_bytes, value=value_bytes)
        producer.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))
        
def json_faker(): 
    print("from faker")
    json_string = '{"2011-09-11 10:48:38.23": {"persons": 4,"umbrellas": 3,"chairs": 5}}'
    faker = FakerSchema()
    data = faker.generate_fake(json_string)
    print(data)
    return data

        
        
if __name__ == "__main__":
    kafka_connect()
