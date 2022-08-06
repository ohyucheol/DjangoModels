from django import forms

class BookForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    thumbnail = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control mb-3'}))
    isbn = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    keyword = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))