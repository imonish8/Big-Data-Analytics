from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(bootstrap_servers = 'localhost:9092', value_serializer = lambda v : json.dumps(v).encode('utf-8'))

while True:
    temperature_data = {
        'machine_id' : random.randint(1, 5),
        'temperautre' : random.uniform(20.00, 100.00),
        'timestamp' : time.time()
    }
    producer.send('temperature_data', temperature_data)
    time.sleep(1)