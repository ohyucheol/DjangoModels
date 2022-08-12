from django.contrib import admin
from .models import Writer

# Register your models here.
class WriterAdmin(admin.ModelAdmin):
	fields = ('name', 'picture', 'work', 'history', 'greeting')
	list_display = ['id', 'name', 'picture', 'work', 'history', 'greeting']

admin.site.register(Writer, WriterAdmin)