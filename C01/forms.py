from django.forms import ModelForm
from django import forms
from .models import Writer

class WriterModelForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ['name', 'picture', 'work', 'history', 'greeting']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'picture' : forms.URLInput(attrs={'class': 'form-control mb-3'}),
            'work' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'history' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'greeting' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }