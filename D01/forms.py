from django.forms import ModelForm
from django import forms
from .models import Book

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'thumbnail', 'isbn', 'keyword']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'thumbnail' : forms.URLInput(attrs={'class': 'form-control mb-3'}),
            'isbn' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'keyword' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }

# class BookForm(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
#     thumbnail = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control mb-3'}))
#     isbn = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
#     keyword = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))