from django import forms
from .models import NovelWriter

class NovelWriterModelForm(forms.ModelForm):
    class Meta:
        model = NovelWriter
        fields = ['name', 'penname', 'picture', 'birthday', 'birthplace', 'work', 'history']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'penname' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'picture' : forms.FileInput(attrs={'class': 'form-control mb-3'}),
            'birthday' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'birthplace' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'work' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'history' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }