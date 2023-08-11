from django.db.models.signals import post_save
from django.db.models import F
from django.dispatch import receiver

from .models import PostEvent


@receiver(post_save, sender=PostEvent)
def increment_like(sender, instance, created, **kwargs):
    if not created:
        created_by_id = instance.created_by_id
        post_id = instance.post_id
        likes_count = instance.likes_count
        if likes_count == 100:
            print(f"Notification to {created_by_id} for post id:- {post_id}")
