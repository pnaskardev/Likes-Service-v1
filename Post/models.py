from django.db import models

from User.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200, blank=True)
    likes_count = models.IntegerField(default=0)

    created_by = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
