import inotify.adapters
import pika

from config import rabbit_mq_data, directory_path

i = inotify.adapters.Inotify()

credentials = pika.PlainCredentials(rabbit_mq_data['login'], rabbit_mq_data['password'])
connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_mq_data['host'],
                                                               rabbit_mq_data['port'],
                                                               rabbit_mq_data['v_host'],
                                                               credentials))
channel = connection.channel()
channel.queue_declare(queue=rabbit_mq_data['queue_name'])


def _main():

    i.add_watch(directory_path)

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event

        message = "PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
            path, filename, type_names)

        channel.basic_publish(exchange='', routing_key=rabbit_mq_data['queue_name'], body=message)


if __name__ == '__main__':
    _main()
    connection.close()
