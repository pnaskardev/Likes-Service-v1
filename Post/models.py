import uuid

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    likes_count = models.IntegerField(default=0)
