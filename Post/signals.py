from django.db.models.signals import post_save
from django.db.models import F
from django.dispatch import receiver

from Likes.models import Like
from .models import Post


@receiver(post_save, sender=Like)
def increment_like(sender, instance, created, **kwargs):

    if created:
        user_id=instance.user_id
        post_id = instance.post_id
        post = Post.objects.get(pk=post_id)
        post.likes_count = post.likes_count + 1
        post.save()
        # Post.objects.filter(pk=post_id).update(likes_count=F('likes_count') + 1)
        if post.likes_count==100:
            print(f"Notification to {user_id} for post id:- {post_id}")