import json
import time
import random
import uuid
import threading
from kafka import KafkaProducer

# Configuration
KAFKA_BROKER = 'localhost:9092'  # Replace with your Kafka broker address
TOPIC_NAME = 'vitals'
NUM_PRODUCERS = 2
MESSAGES_PER_PRODUCER = 5

# Serializer to convert Python dictionary to JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=serializer
)

# Monotonic sequence number
sequence_number = 0
sequence_lock = threading.Lock()


def generate_vitals(producer_id):
    global sequence_number
    while True:
        # Simulate vital signs data
        heart_rate = random.randint(60, 100)
        temperature = round(random.uniform(36.5, 37.5), 1)
        blood_pressure = f"{random.randint(110, 130)}/{random.randint(70, 90)}"
        respiratory_rate = random.randint(12, 20)

        # Create a message
        message = {
            "producer_id": producer_id,
            "timestamp": time.time(),
            "heart_rate": heart_rate,
            "temperature": temperature,
            "blood_pressure": blood_pressure,
            "respiratory_rate": respiratory_rate,
        }

        # Add sequence number
        with sequence_lock:
            sequence_number += 1
            message["sequence_number"] = sequence_number

        # Send the message to Kafka
        print(f"Sending: {message}")
        producer.send(TOPIC_NAME, message)

        # Wait for a random time interval
        time.sleep(random.uniform(0.5, 1.5))


def run_producer(producer_id):
    print(f"Starting producer {producer_id}")
    for i in range(MESSAGES_PER_PRODUCER):
        generate_vitals(producer_id)
    print(f"Producer {producer_id} finished")

if __name__ == '__main__':
    threads = []
    for i in range(NUM_PRODUCERS):
        thread = threading.Thread(target=run_producer, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    producer.close()
    print("All producers finished")