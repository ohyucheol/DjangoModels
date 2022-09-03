from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator

class UserCreateForm(forms.ModelForm):
    password2 = forms.CharField(max_length=150, validators=[RegexValidator(regex='([a-zA-Z0-9])+')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
            'password2' : forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
        }