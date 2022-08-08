from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	thumbnail = models.URLField(blank=True)
	isbn = models.CharField(max_length=200, blank=True)
	keyword = models.CharField(max_length=200, blank=True)

class Format(models.Model):
	book_id = models.IntegerField()
	edition = models.CharField(max_length=200,blank=True)
	impression = models.CharField(max_length=200,blank=True)
	binding = models.CharField(max_length=200,blank=True)
	size = models.CharField(max_length=200,blank=True)
	page = models.IntegerField(null=True, blank=True)
	weight = models.CharField(max_length=200,blank=True)

class DecimalClassification(models.Model):
	book_id = models.IntegerField()
	k_isbn = models.CharField(max_length=200,blank=True)
	kdc = models.CharField(max_length=200,blank=True)
	ddc = models.CharField(max_length=200,blank=True)
