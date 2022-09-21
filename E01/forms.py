from django.forms import ModelForm
from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
    thumbnail_file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control mb-3'}), label='썸네일')

    class Meta:
        model = Article
        fields = ['title', 'thumbnail_file', 'content', 'tag']
        # fields = ['title', 'thumbnail_file', 'content', 'tag', 'is_public']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'content' : forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'tag' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            # 'is_public' : forms.RadioSelect([('True', '공개'), ('False', '비공개')])
        }

        labels = {
            'title' : '제목',
            'thumbnail' : '썸네일',
            'content' : '내용',
            'tag' : '태그',
            # 'is_public' : '공개여부',
        }