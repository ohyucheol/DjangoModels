from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # fields = ('user_id', 'title', 'thumbnail', 'content', 'published', 'modified', 'tag', 'is_public')
    # list_display = ['id', 'user_id', 'title', 'thumbnail', 'content', 'published', 'modified', 'tag', 'is_public']

    fields = ('user_id', 'title', 'thumbnail', 'content', 'published', 'modified', 'tag')
    list_display = ['id', 'user_id', 'title', 'thumbnail', 'content', 'published', 'modified', 'tag']

admin.site.register(Article, ArticleAdmin)