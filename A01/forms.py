from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator

class UserCreateForm(forms.ModelForm):
    username = forms.CharField(validators=[RegexValidator(regex='^([a-zA-Z0-9])+$')], widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

        widgets = {
            # 'username' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
            # 'password2' : forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
        }