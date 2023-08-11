from django.db import models

from User.models import User
from Post.models import Post


class Like(models.Model):
    # created_by = models.ForeignKey(
    #     User, related_name='likes', on_delete=models.CASCADE)
    user_id = models.BigIntegerField(blank=True, default=-1)

    # liked_post = models.ForeignKey(
    #     Post, related_name='liked_post', blank=True, on_delete=models.CASCADE)

    post_id = models.BigIntegerField(blank=True, default=-1)

    class Meta:
        indexes = [models.Index(fields=["id"])]
