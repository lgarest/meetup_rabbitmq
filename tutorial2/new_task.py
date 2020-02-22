#!/usr/bin/env python
import pika
import sys

# This is the producer program because it `produces` a message

ADDRESS = "192.168.230.133"
QUEUE = "My testing queue"

connection = pika.BlockingConnection(pika.ConnectionParameters(ADDRESS))
channel = connection.channel()

# queue declaration
channel.queue_declare(queue=QUEUE)


def publish(msg):
    channel.basic_publish(exchange="", routing_key=QUEUE, body=msg)
    print(f"  [x] Sent '{msg}'!")


message = " ".join(sys.argv[1:]) or "2::Testing message"
# publishing to the queue
publish(message)

connection.close()
