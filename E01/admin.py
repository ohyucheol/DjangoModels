from django.contrib import admin
from .models import MeetingRoom, Equipment
# Register your models here.

class MeetingRoomAdmin(admin.ModelAdmin):
	fields = ('name', 'address', 'picture', 'keyword')
	list_display = ['id', 'name', 'address', 'picture', 'keyword']

class EquipmentAdmin(admin.ModelAdmin):
	fields = ('meetingroom_id', 'space', 'capacity', 'audio', 'video', 'other', 'layout', 'information')
	list_display = ['id', 'meetingroom_id', 'space', 'capacity', 'audio', 'video', 'other', 'layout', 'information']

admin.site.register(MeetingRoom, MeetingRoomAdmin)
admin.site.register(Equipment, EquipmentAdmin)