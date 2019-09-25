from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body  = models.TextField()
    uploaded = models.DateTimeField(default=timezone.now)
    commentext = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
