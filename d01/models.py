from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	thumbnail = models.URLField()
	isbn = models.CharField(max_length=200)
	keyword = models.CharField(max_length=200)

class BookMeta(models.Model):
	book = models.ForeignKey("Book", related_name="meta", on_delete=models.CASCADE)
	key = models.CharField(max_length=200)
	value = models.CharField(max_length=200)

class Format(models.Model):
	book = models.ForeignKey("Book", related_name="format", on_delete=models.CASCADE)
	edition = models.CharField(max_length=200)
	impression = models.CharField(max_length=200)
	binding = models.CharField(max_length=200)
	size = models.CharField(max_length=200)
	page = models.IntegerField()
	weight = models.CharField(max_length=200)

class Category(models.Model):
	book = models.ForeignKey("Book", related_name="category", on_delete=models.CASCADE)
	k_isbn = models.CharField(max_length=200)
	kdc = models.CharField(max_length=200)
	ddc = models.CharField(max_length=200)
