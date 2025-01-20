# kafka_producer_huntsman.py

import os
import sys
import time
import random
from dotenv import load_dotenv
from utils.utils_producer import (
    verify_services,
    create_kafka_producer,
    create_kafka_topic,
)
from utils.utils_logger import logger

# Load Environment Variables
load_dotenv()

# Getter Function for Kafka Topic
def get_kafka_topic() -> str:
    """Fetch Kafka topic from environment or use default."""
    topic = os.getenv("KAFKA_TOPIC", "buzzline")
    logger.info(f"Kafka topic: {topic}")
    return topic

# Getter Function for Message Interval
def get_message_interval() -> int:
    """Fetch message interval from environment or use default."""
    interval = int(os.getenv("MESSAGE_INTERVAL_SECONDS", 1))
    logger.info(f"Message interval: {interval} seconds")
    return interval

# Predefined list of sentence-based messages
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Kafka is a powerful tool for real-time streaming.",
    "Python makes data processing so much easier.",
    "Streaming data can help you understand patterns in real-time.",
    "I love building scalable systems using Kafka!",
    "Message processing is a crucial part of any streaming system.",
    "Real-time analytics can transform business decision-making.",
    "Data pipelines are essential for modern data architectures.",
    "Machine learning and real-time data go hand in hand.",
    "Big data and real-time processing are shaping the future."
]

# Message Generator
def generate_messages(producer, topic, interval_secs):
    """
    Generate a stream of sentence-based messages and send them to a Kafka topic.

    Args:
        producer (KafkaProducer): The Kafka producer instance.
        topic (str): The Kafka topic to send messages to.
        interval_secs (int): Time in seconds between sending messages.
    """
    try:
        while True:
            # Randomly pick a sentence from the predefined list
            message_content = random.choice(SENTENCES)
            
            # Log and send the generated sentence
            logger.info(f"Generated buzz: {message_content}")
            producer.send(topic, value=message_content)
            logger.info(f"Sent message to topic '{topic}': {message_content}")
            
            # Wait for the next interval
            time.sleep(interval_secs)
    
    except KeyboardInterrupt:
        logger.warning("Producer interrupted by user.")
    except Exception as e:
        logger.error(f"Error in message generation: {e}")
    finally:
        producer.close()
        logger.info("Kafka producer closed.")

def main():
    """
    Main entry point for this producer.

    - Ensures the Kafka topic exists.
    - Creates a Kafka producer using the `create_kafka_producer` utility.
    - Streams sentence-based messages to the Kafka topic.
    """
    logger.info("START producer.")
    verify_services()

    # fetch .env content
    topic = get_kafka_topic()
    interval_secs = get_message_interval()

    # Create the Kafka producer
    producer = create_kafka_producer()
    if not producer:
        logger.error("Failed to create Kafka producer. Exiting...")
        sys.exit(3)

    # Create topic if it doesn't exist
    try:
        create_kafka_topic(topic)
        logger.info(f"Kafka topic '{topic}' is ready.")
    except Exception as e:
        logger.error(f"Failed to create or verify topic '{topic}': {e}")
        sys.exit(1)

    # Generate and send sentence-based messages
    logger.info(f"Starting message production to topic '{topic}'...")
    generate_messages(producer, topic, interval_secs)

    logger.info("END producer.")

if __name__ == "__main__":
    main()
