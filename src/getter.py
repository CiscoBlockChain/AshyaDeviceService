from __future__ import absolute_import
from kafka import  KafkaConsumer


def kafka_get_values():
    values = []
    consumer = KafkaConsumer('test')
    #start iterate
    for message in consumer:
        print(message.value)
        values.append(message.value)
        
    return values    
        
    
        
if __name__ == "__main__":
  kafka_get_values()        
    