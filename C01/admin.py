from django.contrib import admin
from .models import NovelWriter

# Register your models here.
class NovelWriterAdmin(admin.ModelAdmin):
	fields = ('name', 'penname', 'birthday',  'birthplace', 'picture', 'work', 'history')
	list_display = ['id', 'name', 'penname', 'birthday',  'birthplace', 'picture', 'work', 'history']

admin.site.register(NovelWriter, NovelWriterAdmin)