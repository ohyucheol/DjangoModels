from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import RegexValidator, EmailValidator

class UserCreateForm(forms.ModelForm):
    val1 = RegexValidator(regex='^([a-zA-Z0-9])+$')
    val2 = EmailValidator()

    err1 = {'unique' : '이미 사용중인 아이디입니다'}
    err2 = {'required' : '비밀번호를 입력하세요'}

    cls1 = forms.TextInput(attrs={'class': 'form-control mb-3'})
    cls2 = forms.PasswordInput(attrs={'class': 'form-control mb-3'})
    cls3 = forms.PasswordInput(attrs={'class': 'form-control mb-3'})
    

    username = forms.CharField(widget=cls1, error_messages=err1, validators=[val1])
    email = forms.EmailField(widget=cls1, validators=[val2])
    password1 = forms.CharField(widget=cls2, error_messages=err2)
    password2 = forms.CharField(widget=cls3)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class UserCreateForm(UserCreationForm):
#     # username = forms.CharField(validators=[RegexValidator(regex='^([a-zA-Z0-9])+$')], widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}))
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#         widgets = {
#             'username' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
#             # 'email' : forms.EmailInput(attrs={'class': 'form-control mb-3'}),
#             'password1' : forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
#             'password2' : forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
#         }
