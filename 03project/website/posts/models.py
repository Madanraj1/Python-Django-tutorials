from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=20)
    post_body = models.TextField()
    uploaded_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
