from __future__ import absolute_import
from faker import Faker
from kafka import KafkaProducer, KafkaConsumer

def kafka_get_values():
    consumer = KafkaConsumer('test')
    for msg in consumer:
        print(msg)
    consumer.close()    
    
    
if __name__ == "__main__":
    kafka_get_values()
    