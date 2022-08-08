from django.contrib import admin
from .models import Book, Format, DecimalClassification
# Register your models here.

class BookAdmin(admin.ModelAdmin):
	fields = ('title', 'thumbnail', 'isbn', 'keyword')
	list_display = ['title', 'thumbnail', 'isbn', 'keyword']

admin.site.register(Book, BookAdmin)
admin.site.register(Format)
admin.site.register(DecimalClassification)