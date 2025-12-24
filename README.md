# Live Vitals Producer

This project simulates a live vitals producer that sends data to a Kafka topic.

## Usage

1.  **Prerequisites:**
    *   Kafka broker running.
    *   Python 3.6+
    *   `kafka-python` library installed (`pip install kafka-python`)

2.  **Configuration:**
    *   Update `KAFKA_BROKER` in `producer.py` with your Kafka broker address.
    *   Ensure the `vitals` topic exists in Kafka.

3.  **Run the producer:**
    ```bash
    python producer.py
    ```

## Docker

A Dockerfile is included to containerize the application.  Use the following commands to build and run the Docker image:

```bash
docker build -t live-vitals-producer .
docker run -d --name live-vitals-producer live-vitals-producer
```
