from django.db import models

# Create your models here.
class NovelWriter(models.Model):
    #user_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, blank=True)
    penname = models.CharField(max_length=50, blank=True)
    picture = models.URLField(blank=True)
    birthday = models.CharField(max_length=50, blank=True)
    birthplace = models.CharField(max_length=50, blank=True)
    work = models.TextField(max_length=1000, blank=True)
    history = models.TextField(max_length=1000, blank=True)