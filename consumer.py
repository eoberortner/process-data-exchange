import threading

from kafka import KafkaConsumer

from configs import NUM_TOPICS


def consume_messages(i: int):
    """consumes messages from topic i"""
    topic = f"Topic_{i}"
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092')

    print(f"consuming messages on topic {topic}")
    for msg in consumer:
        print(msg)


if __name__ == "__main__":

    # for each topic, we have one thread listening for new messages
    for i in range(NUM_TOPICS):
        t = threading.Thread(target=consume_messages, args=[(i+1)])
        t.start()

