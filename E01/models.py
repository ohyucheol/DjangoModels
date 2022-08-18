from django.db import models

# Create your models here.
class MeetingRoom(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200, blank=True)
	picture = models.URLField(max_length=200, blank=True)
	keyword = models.CharField(max_length=200, blank=True)

class Equipment(models.Model):
	meetingroom_id = models.IntegerField()
	space = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
	capacity = models.IntegerField(max_length=200, blank=True)
	equip_audio = models.CharField(max_length=200, blank=True)
	equip_video = models.CharField(max_length=200, blank=True)
	equip_other = models.CharField(max_length=200, blank=True)
	layout = models.CharField(max_length=200, blank=True)
	information = models.TextField(max_length=2000, blank=True)