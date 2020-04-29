import pika
import time

from config import rabbit_mq_data

credentials = pika.PlainCredentials(rabbit_mq_data['login'], rabbit_mq_data['password'])
connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_mq_data['host'],
                                                               rabbit_mq_data['port'],
                                                               rabbit_mq_data['v_host'],
                                                               credentials))

channel = connection.channel()


def _main():

    while True:

        method_frame, header_frame, body = channel.basic_get(rabbit_mq_data['queue_name'])
        if method_frame:
            print(body.encode())
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print('No messages')

        time.sleep(5)


if __name__ == '__main__':
    _main()

