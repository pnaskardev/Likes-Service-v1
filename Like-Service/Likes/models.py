from django.db import models


class LikeEvent(models.Model):
    user_id = models.BigIntegerField(blank=True, default=-1)
    post_id = models.BigIntegerField(blank=True, default=-1)

    class Meta:
        indexes = [models.Index(fields=["id"])]


class PostEvent(models.Model):
    post_id = models.BigIntegerField(blank=True, default=-1)
    created_by_id = models.BigIntegerField(blank=True, default=-1)
    likes_count = models.IntegerField(default=0)
