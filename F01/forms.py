from django.forms import ModelForm
from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['writer_id', 'title', 'subtitle', 'thumbnail', 'content', 'published', 'keyword']

        widgets = {
            'writer_id' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'title' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'subtitle' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'thumbnail' : forms.URLInput(attrs={'class': 'form-control mb-3'}),
            'content' : forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'published' : forms.DateInput(attrs={'class': 'form-control mb-3'}),
            'keyword' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }