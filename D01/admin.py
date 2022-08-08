from django.contrib import admin
from .models import Book, Format, DecimalClassification
# Register your models here.

class BookAdmin(admin.ModelAdmin):
	fields = ('title', 'thumbnail', 'isbn', 'keyword')
	list_display = ['id', 'title', 'thumbnail', 'isbn', 'keyword']

class FormatAdmin(admin.ModelAdmin):
	fields = ('book_id', 'edition', 'impression', 'binding', 'size', 'page', 'weight')
	list_display = ['id', 'book_id', 'edition', 'impression', 'binding', 'size', 'page', 'weight']

class DecimalClassificationAdmin(admin.ModelAdmin):
	fields = ('book_id', 'k_isbn', 'kdc', 'ddc')
	list_display = ['id', 'book_id', 'k_isbn', 'kdc', 'ddc']

admin.site.register(Book, BookAdmin)
admin.site.register(Format, FormatAdmin)
admin.site.register(DecimalClassification, DecimalClassificationAdmin)