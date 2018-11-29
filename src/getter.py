from __future__ import absolute_import
from faker import Faker
from kafka import KafkaProducer, KafkaConsumer

def kafka_connect():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    temp = random_data()
    print("here")
    try:
        #producer = KafkaProducer(value_serializer=lambda v: str.encode('utf-8'))
        producer = KafkaProducer(key_serializer=str.encode)
        producer.send('test', key='my message', value=str.encode(temp))
        #producer.send('test',temp)
        producer.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))
        
#def kafka_get_values():
#    consumer = KafkaConsumer('test')
#    for msg in consumer:
#        print(msg)  

def random_data():
    fake = Faker()
    for _ in range(3):
        return fake.text()
        
        
if __name__ == "__main__":
    kafka_connect()   
    