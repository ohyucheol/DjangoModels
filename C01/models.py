from django.db import models

# Create your models here.
class Writer(models.Model):
    #user_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50)
    picture = models.URLField(blank=True)
    work = models.TextField(max_length=1000, blank=True)
    history = models.TextField(max_length=1000, blank=True)
    greeting = models.TextField(max_length=1000, blank=True)