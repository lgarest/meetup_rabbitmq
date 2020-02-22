#!/usr/bin/env python
import pika
import time

# This is the consumer program because it `consumes` a message

ADDRESS = "192.168.230.133"
QUEUE = "My testing queue"
# QUEUE = "hi"

connection = pika.BlockingConnection(pika.ConnectionParameters(ADDRESS))
channel = connection.channel()

# queue declaration
channel.queue_declare(queue=QUEUE)


def callback(ch, method, properties, body):
    print(f"  [x] Received '{body}' message!")
    time.sleep(body.count(b".") * 2)
    print("  [x] Done")


# set up the queue where to start listening
channel.basic_consume(queue=QUEUE, auto_ack=True, on_message_callback=callback)

print(" [*] Waiting for messages. To exit press CTRL+C")
# start listening in a while(1) fashion
channel.start_consuming()
