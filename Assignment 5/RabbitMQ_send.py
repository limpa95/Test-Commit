import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='message')

channel.basic_publish(exchange='', routing_key='message', body='A message from CS361')
print(" [x] Sent 'A message from CS361'")

connection.close()