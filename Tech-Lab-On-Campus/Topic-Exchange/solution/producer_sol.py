from producer_interface import mqProducerInterface
import pika
import os
import sys

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        self.channel = self.connection.channel()

        # Create the exchange if not already present
        exchange = self.channel.exchange_declare(exchange=self.exchange_name, exchange_type="topic")

    def publishOrder(self, message: str) -> None:
        # Create Appropiate Topic String
        #info = sys.argv[:]
        #ticker = info[0]
        #price = info[1]
        #sector = info[2]

        # Send serialized message or String

        # Print Confirmation
        
        # Basic Publish to Exchange
        #self.channel.basic_publish(
        #    exchange=self.exchange_name,
        #    routing_key=self.routing_key,
        #    body=message,
        #)

        # Close Channel
        self.channel.close()

        # Close Connection
        self.connection.close()