from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	adultcontent = models.BooleanField(default=False)
	book_photo = models.ImageField(null=True, blank=True)
	def __str__(self):
		return self.title