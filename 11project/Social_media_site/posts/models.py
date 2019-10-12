from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


from django.conf import settings

class Post(models.Model):
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    title   = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250,unique_for_date='created')
    body    = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created',)

    def __Str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.created.year,
                                            self.created.month,
                                            self.created.day,
                                            self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body  = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class Profile(models.Model):
    user          = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    photo         = models.ImageField(upload_to='users/%Y/%M/%D/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.usernames) 