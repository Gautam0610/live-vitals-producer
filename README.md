# Live Vitals Producer

This project generates continuous vitals data and sends it to a Kafka topic.

## Prerequisites

*   Docker (for containerization)
*   Kafka cluster running (e.g., on localhost:9092)

## Usage

1.  **Build the Docker image:**

    ```bash
    docker build -t live-vitals-producer .
    ```

2.  **Run the Docker container:**

    ```bash
    docker run -it --rm --name vitals-producer live-vitals-producer
    ```

    Make sure your Kafka broker is accessible from within the container.  If Kafka is running on your host machine, you might need to adjust the `KAFKA_BOOTSTRAP_SERVERS` in `producer.py` to use your host's IP address or configure Docker networking appropriately.

## Configuration

*   `KAFKA_TOPIC`: The Kafka topic to send data to (default: `vitals`).
*   `KAFKA_BOOTSTRAP_SERVERS`: The Kafka broker address (default: `localhost:9092`).  Change this in `producer.py` if your Kafka broker is running elsewhere.