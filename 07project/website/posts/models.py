from django.db import models
from django.utils import timezone 

class Comment(models.Model):
	comment = models.TextField(max_length=150)
	data_added = models.DateField(default=timezone.now)

	def __str__(self):
		return self.comment

