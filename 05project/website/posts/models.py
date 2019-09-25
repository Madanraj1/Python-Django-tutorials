from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=30)
    post_body = models.TextField()
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_title
