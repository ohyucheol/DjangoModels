from django.db import models

# Create your models here.
class Article(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200)
    thumbnail = models.URLField(blank=True)
    content = models.TextField(max_length=3000, blank=True)
    published = models.DateField(null=True, blank=True)
    modified = models.DateField(null=True, blank=True)
    tag = models.CharField(max_length=200, blank=True)
    # is_public = models.BooleanField(default=True)