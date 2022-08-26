from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	fields = ('writer_id', 'title', 'subtitle', 'thumbnail', 'content', 'published', 'keyword')
	list_display = ['id', 'writer_id', 'title', 'subtitle', 'thumbnail', 'content', 'published', 'keyword']

admin.site.register(Article, ArticleAdmin)