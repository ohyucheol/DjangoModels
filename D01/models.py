from django.db import models

# Create your models here.
class ComicBook(models.Model):
	title = models.CharField(max_length=200)
	cover = models.URLField(blank=True)
	number = models.IntegerField(blank=True)
	author = models.CharField(max_length=200)
	isbn = models.CharField(max_length=200, blank=True)
	genre = models.CharField(max_length=200, blank=True)
	tag = models.CharField(max_length=200, blank=True)