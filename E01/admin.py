from django.contrib import admin
from .models import Classroom, Equipment
# Register your models here.

class ClassroomAdmin(admin.ModelAdmin):
	fields = ('name', 'address', 'picture', 'keyword')
	list_display = ['id', 'name', 'address', 'picture', 'keyword']

class EquipmentAdmin(admin.ModelAdmin):
	fields = ('classroom_id', 'capacity', 'equip_audio', 'equip_video', 'equip_other', 'layout', 'information')
	list_display = ['id', 'classroom_id', 'capacity', 'equip_audio', 'equip_video', 'equip_other', 'layout', 'information']

admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Equipment, EquipmentAdmin)