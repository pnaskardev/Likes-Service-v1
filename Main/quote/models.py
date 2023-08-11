from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Quote(models.Model):
    title = models.CharField(max_length=200)
    created_by=models.IntegerField(default=1)

    def __dir__(self):
        return self.title