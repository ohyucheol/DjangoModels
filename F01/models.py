from django.db import models

# Create your models here.
class Article(models.Model):
	writer_id = models.IntegerField()
	title = models.CharField(max_length=200, blank=True)
	subtitle = models.CharField(max_length=200, blank=True)
	thumbnail = models.URLField(blank=True)
	content = models.TextField(max_length=2000, blank=True)
	published = models.DateField(blank=True)
	keyword = models.CharField(max_length=200, blank=True)