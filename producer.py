import time
import threading

from kafka import KafkaProducer

from configs import NUM_TOPICS, NUM_MESSAGES, SLEEP_TIME


def produce_messages(i: int):

    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    topic = f"Topic_{i+1}"
    for m in range(NUM_MESSAGES):
        message = f"message {m+1}"
        print(f"sending message {message} to topic {topic} ... ")
        producer.send(topic, str.encode(message))
        producer.flush()

        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    for i in range(NUM_TOPICS):
        t = threading.Thread(target=produce_messages, args=[i])
        t.start()









