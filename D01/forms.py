from django.forms import ModelForm
from django import forms
from .models import Book, Format, DecimalClassification

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

class FormatModelForm(forms.ModelForm):
    class Meta:
        model = Format
        fields = ['book_id', 'edition', 'impression', 'binding', 'size', 'page', 'weight']

        widgets = {
            'book_id' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'edition' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'impression' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'binding' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'size' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'page' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'weight' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }

class DecimalClassificationModelForm(forms.ModelForm):
    class Meta:
        model = DecimalClassification
        fields = ['book_id', 'k_isbn', 'kdc', 'ddc']

        widgets = {
            'book_id' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'k_isbn' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'kdc' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'ddc' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }