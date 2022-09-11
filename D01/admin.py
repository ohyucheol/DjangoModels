from django.contrib import admin
from .models import ComicBook
# Register your models here.

class ComicBookAdmin(admin.ModelAdmin):
	fields = ('title', 'cover', 'number', 'author', 'isbn', 'genre', 'tag')
	list_display = ['id', 'title', 'cover', 'number', 'author', 'isbn', 'genre', 'tag']

admin.site.register(ComicBook, ComicBookAdmin)