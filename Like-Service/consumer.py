# from Likes.models import PostEvent
# import json
# import pika
# import django
# from sys import path
# from os import environ
# import os
# import sys


# # path.append('/home/john/Dev/SECTION/Likes/Likes/settings.py')
# # Get the base directory of the project
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Append the path to settings.py
# settings_path = os.path.join(BASE_DIR, 'Likes-Service', 'core', 'settings.py')
# sys.path.append(settings_path)
# environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# django.setup()

# connection = pika.BlockingConnection(pika.ConnectionParameters(
#     'localhost', heartbeat=600, blocked_connection_timeout=300))
# channel = connection.channel()
# channel.queue_declare(queue='likes')


# def callback(ch, method, properties, body):
#     print("Received in likes...")
#     print(body)
#     data = json.loads(body)
#     print(data)

#     # if properties.content_type == 'quote_created':
#     #     quote = PostEvent.objects.create(
#     #         post_id=data['id'], title=data['title'])
#     #     quote.save()
#     #     print("quote created")
#     # elif properties.content_type == 'quote_updated':
#     #     quote = PostEvent.objects.get(id=data['id'])
#     #     quote.title = data['title']

#     #     quote.save()
#     #     print("quote updated")
#     # elif properties.content_type == 'quote_deleted':
#     #     quote = PostEvent.objects.get(id=data)

#     #     print(quote)
#     #     quote.delete()
#     #     print("quote deleted")


# channel.basic_consume(
#     queue='likes', on_message_callback=callback, auto_ack=True)
# print("Started Consuming...")
# channel.start_consuming()


import json
import pika
import django
import os

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize Django
django.setup()

from Likes.models import PostEvent  # Import after Django setup

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='likes')


def callback(ch, method, properties, body):
    print("Received in likes...")
    print(body)
    data = json.loads(body)
    print(data)
    print(properties.content_type)
    # Your logic to process the received data goes here
    # For example:
    # post = PostEvent.objects.create(post_id=data['post_id'], ...)
    # post.save()

    if properties.content_type == 'quote_created':
        quote = PostEvent.objects.create(
            post_id=data['id'], created_by_id=data['created_by'])
        quote.save()
        print("quote created")
    # elif properties.content_type == 'quote_updated':
    #     quote = PostEvent.objects.get(id=data['id'])
    #     quote.title = data['title']

    #     quote.save()
    #     print("quote updated")
    # elif properties.content_type == 'quote_deleted':
    #     quote = PostEvent.objects.get(id=data)

    #     print(quote)
    #     quote.delete()
    #     print("quote deleted")

channel.basic_consume(
    queue='likes', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()
