from django.db import models

# Create your models here.
class MeetingRoom(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)
    picture = models.URLField(max_length=200, blank=True)
    space = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    capacity = models.IntegerField(blank=True)
    audio = models.CharField(max_length=200, blank=True)
    video = models.CharField(max_length=200, blank=True)
    other = models.CharField(max_length=200, blank=True)
    information = models.TextField(max_length=2000, blank=True)