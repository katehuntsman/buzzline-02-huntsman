# kafka_consumer_huntsman.py

import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
from utils.utils_logger import logger

# Load Environment Variables
load_dotenv()

# Getter Function for Kafka Topic
def get_kafka_topic() -> str:
    """Fetch Kafka topic from environment or use default."""
    topic = os.getenv("KAFKA_TOPIC", "buzzline")
    logger.info(f"Kafka topic: {topic}")
    return topic

# Getter Function for Kafka Consumer Group ID
def get_kafka_consumer_group_id() -> str:
    """Fetch Kafka consumer group ID from environment or use default."""
    group_id = os.getenv("KAFKA_CONSUMER_GROUP_ID", "default_group")
    logger.info(f"Kafka consumer group ID: {group_id}")
    return group_id

# Process each message consumed
def process_message(message: str) -> None:
    """
    Process a single message.
    Args:
        message (str): The message to process.
    """
    logger.info(f"Processing message: {message}")

def main():
    """
    Main entry point for the consumer.
    - Reads the Kafka topic name and consumer group ID from environment variables.
    - Creates a Kafka consumer.
    - Processes messages from the Kafka topic.
    """
    logger.info("START consumer.")

    # Fetch .env content
    topic = get_kafka_topic()
    group_id = get_kafka_consumer_group_id()
    logger.info(f"Consumer: Topic '{topic}' and group '{group_id}'...")

    # Create Kafka consumer instance
    consumer = KafkaConsumer(
        topic,
        group_id=group_id,
        auto_offset_reset='earliest',  # Start from the beginning of the topic
        enable_auto_commit=True,  # Automatically commit offsets
        value_deserializer=lambda m: m.decode('utf-8') if isinstance(m, bytes) else m  # Only decode if it's bytes
    )

    # Poll and process messages
    logger.info(f"Polling messages from topic '{topic}'...")
    try:
        for message in consumer:
            message_str = message.value  # The message content is decoded as string
            logger.debug(f"Received message at offset {message.offset}: {message_str}")
            process_message(message_str)
    except KeyboardInterrupt:
        logger.warning("Consumer interrupted by user.")
    except Exception as e:
        logger.error(f"Error while consuming messages: {e}")
    finally:
        consumer.close()
        logger.info(f"Kafka consumer for topic '{topic}' closed.")

    logger.info(f"END consumer for topic '{topic}' and group '{group_id}'.")

if __name__ == "__main__":
    main()
