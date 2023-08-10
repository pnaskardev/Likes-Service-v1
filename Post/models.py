import uuid

from django.db import models


class User(models.Model):
    pass


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200, blank=True)
    likes_count = models.IntegerField(default=0)
