from django import forms
from .models import NovelWriter

class NovelWriterModelForm(forms.ModelForm):
    picture_file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control mb-3'}), label='사진')

    class Meta:
        model = NovelWriter
        fields = ['name', 'penname', 'picture_file', 'birthday', 'birthplace', 'work', 'history']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'penname' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            # 'picture' : forms.FileInput(attrs={'class': 'form-control mb-3'}),
            'birthday' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'birthplace' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'work' : forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'history' : forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }

        labels = { 
            'name' : '성명', 'penname' : '필명', # 'picture' : '사진',
            'birthday' : '생년월일', 'birthplace' : '출생지', 'work' : '작품', 'history' : '약력'
        }