from producer_interface import mqProducerInterface
import pika
import os
import sys

class mqProducer(mqProducerInterface):
    def __init__(self, exchange_name: str) -> None:
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

    def publishOrder(self, ticker: str, price: float, sector: str) -> None:
        message = ticker + " price is now $" + str(price)

        # Create Appropiate Topic String
        topic_string = ticker + "." + sector

        # Send serialized message or String
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=topic_string,
            body=message
        )

        # Print Confirmation
        print("Sent order of: " + message)
        
        # Close Channel
        self.channel.close()

        # Close Connection
        self.connection.close()