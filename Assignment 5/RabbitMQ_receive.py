import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='message')

    def callback(ch, method, properties, body):
        str = body.decode()
        print(f" [x] Received '{str}'")

    channel.basic_consume(queue='message', on_message_callback=callback, auto_ack=True,)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)