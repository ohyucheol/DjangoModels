from django import forms
from .models import ComicBook

class ComicBookModelForm(forms.ModelForm):
    cover_file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control mb-3'}), label='표지')

    class Meta:
        model = ComicBook
        fields = ['title', 'cover_file', 'number', 'author', 'genre', 'tag']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'number' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'author' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'genre' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'tag' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }

        labels = {
            'title' : '제목', 'number' : '권수', 'author' : '작가', 'genre' : '장르', 'tag' : '태그',
        }