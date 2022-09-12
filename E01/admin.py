from django.contrib import admin
from .models import MeetingRoom
# Register your models here.

class MeetingRoomAdmin(admin.ModelAdmin):
	fields = ('name', 'address', 'picture', 'space', 'capacity', 'audio', 'video', 'other', 'information')
	list_display = ['name', 'address', 'picture', 'space', 'capacity', 'audio', 'video', 'other', 'information']
	
admin.site.register(MeetingRoom, MeetingRoomAdmin)