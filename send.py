#!/usr/bin/env python
import pika

import argparse
import os


def initialize_parser(parser: argparse.ArgumentParser = None):
    if parser is None:
        parser = argparse.ArgumentParser()

    parser.add_argument(
        '--host',
        default=os.environ.get('BROKER_HOST', 'localhost'),
        help='The hostname of the RabbitMQ server'
    )

    parser.add_argument(
        '--port',
        default=os.environ.get('BROKER_PORT', 5672),
        help='The port of the RabbitMQ server'
    )

    parser.add_argument(
        '--user',
        default=os.environ.get('BROKER_USER', 'user'),
        help='The username to use when connecting to the RabbitMQ server'
    )

    parser.add_argument(
        '--password',
        default=os.environ.get('BROKER_PASSWORD', 'password'),
        help='The password to use when connecting to the RabbitMQ server'
    )

    parser.add_argument(
        '--queue',
        default='test',
        help='The queue to use when connecting to the RabbitMQ server'
    )

    parser.add_argument(
        '--body',
        default='Hello World!',
        help='The body of the message to send',
    )

    return parser


def main(kwargs):
    credentials = pika.PlainCredentials(kwargs.user, kwargs.password)

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        kwargs.host,
        port=int(kwargs.port),
        credentials=credentials))

    channel = connection.channel()

    channel.queue_declare(queue=kwargs.queue)

    channel.basic_publish(exchange='', routing_key=kwargs.queue, body=kwargs.body)
    print(" [x] Sent '{}'".format(kwargs.body))
    connection.close()


if __name__ == '__main__':
    parser = initialize_parser()
    args = parser.parse_args()
    main(args)
