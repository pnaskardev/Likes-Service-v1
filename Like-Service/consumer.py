import json
import pika
import django
import os

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize Django
django.setup()

from Likes.models import PostEvent, LikeEvent  # Import after Django setup

# connection = pika.BlockingConnection(pika.ConnectionParameters(
#     'localhost', heartbeat=600, blocked_connection_timeout=300))

# Dockerized
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'rabbitmq', heartbeat=600, blocked_connection_timeout=300))

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
    elif properties.content_type == 'like_created':
        user_id = data['user_id']
        quote_id = data['quote_id']

        like_exists = LikeEvent.objects.filter(
            user_id=user_id, post_id=quote_id).exists()
        if like_exists:
            pass
        else:
            like_event = LikeEvent.objects.create(
                user_id=data['user_id'], post_id=data['quote_id'])
            like_event.save()
            quote = PostEvent.objects.get(post_id=quote_id)
            quote.likes_count = quote.likes_count+1
            quote.save()
            print("like created")
    elif properties.content_type == 'quote_deleted':
        quote = PostEvent.objects.get(id=data)

        print(quote)
        quote.delete()
        print("quote deleted")


channel.basic_consume(
    queue='likes', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()
