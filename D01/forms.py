from django import forms
from .models import ComicBook

class ComicBookModelForm(forms.ModelForm):
    class Meta:
        model = ComicBook
        fields = ['title', 'cover', 'number', 'author', 'isbn', 'genre', 'tag']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'thumbnail' : forms.URLInput(attrs={'class': 'form-control mb-3'}),
            'isbn' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'keyword' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }