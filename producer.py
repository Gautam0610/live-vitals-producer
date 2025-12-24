import time
import random
import json
from kafka import KafkaProducer

# Kafka configuration
KAFKA_TOPIC = 'vitals'
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']  # Change if your Kafka broker is running elsewhere

def generate_vitals():
    """Generates random vitals data."""
    return {
        'timestamp': time.time(),
        'heart_rate': random.randint(60, 100),
        'temperature': round(random.uniform(36.5, 37.5), 1),
        'blood_pressure': f"{random.randint(110, 140)}/{random.randint(70, 90)}"
    }

def main():
    """Produces vitals data to Kafka."""
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    try:
        while True:
            vitals = generate_vitals()
            print(f"Producing message: {vitals}")
            producer.send(KAFKA_TOPIC, value=vitals)
            time.sleep(1)  # Send data every 1 second

    except KeyboardInterrupt:
        print("Stopping producer...")
    finally:
        producer.close()

if __name__ == "__main__":
    main()