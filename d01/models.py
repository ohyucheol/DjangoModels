from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField
	thumbnail = models.URLField
	isbn = models.CharField
	keyword = models.CharField

class BookMeta(models.Model):
	book_id = models.IntegerField
	key = models.CharField
	value = models.CharField

class Format(models.Model):
	book_id = models.IntegerField
	edition = models.CharField
	impression = models.CharField
	binding = models.CharField
	size = models.CharField
	page = models.IntegerField
	weight = models.CharField

class Category(models.Model):
	book_id = models.IntegerField
	k_isbn = models.CharField
	kdc = models.CharField
	ddc = models.CharField
