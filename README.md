Here, I demonstrate a simple scenerio of two processes exchanging data following an event-driven messaging style, specifically 
the Publish-Subscriber pattern and an event streaming platform (i.e., Apache Kafka).

P1 is the producer of messages and P2 is the consumer of the messages produced by P1.

### Step 1: Setup Apache Kafka

For the data exchange platform, I decided to utilize Apache Kafka (https://kafka.apache.org/) since Kafka is a high throughput distributed queue which is built for storing a large amount of data for longer periods of time. 

The setup the Kafka server, follow the steps provided at https://kafka.apache.org/quickstart

```
# Start the ZooKeeper service
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```

```
# Start the Kafka broker service
$ bin/kafka-server-start.sh config/server.properties
```

### Step 2: Start both processes

