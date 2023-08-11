from django.db.models.signals import post_save
from django.dispatch import receiver
import requests


from Post.models import Post
from .models import Post


@receiver(post_save, sender=Post)
def increment_like(sender, instance, created, **kwargs):

    if created:
        created_by_id=instance.created_by.id
        post_id = instance.id
        data = {
            "post_id": post_id,
            "created_by_id": created_by_id
        }

        response = requests.post('http://localhost:5000/api/register-post/', json=data)

        if response.status_code == 201:
            print("Post created successfully!")
        else:
            print("Failed to create post.")