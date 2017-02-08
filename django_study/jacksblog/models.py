from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=1024)
    text = models.TextField()
    publish = models.CharField(max_length=1)
    created_date = models.DateTimeField(
        blank=True, null=True
    )
