import json, os, time

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

# validator, validation error, widget 등의 구성을 위한 FormDecorator
class FormDecorator:

    val_09 = RegexValidator(regex='^([0-9])+$')
    val_email = EmailValidator()
    val_azAZ09whitespace = RegexValidator(regex='^([a-zA-Z0-9\s])+$')

    err_username = {'unique' : '이미 사용중인 아이디입니다', 'required' : '아이디를 입력하세요', 'invalid' : '아이디에는 영문자와 숫자만 사용할 수 있습니다', 'max_length' : '아이디는 150자 이하여야 합니다', 'invalid_login':'입력하신 정보와 일치하는 계정이 없습니다'}
    err_email = {'required' : '이메일을 입력하세요', 'invalid' : '이메일 형식이 바르지 않습니다'}
    err_password = {'required' : '비밀번호를 입력하세요'}
    err_banned_keyword = {'invalid' : '금칙어에는 영문자와 숫자만 사용할 수 있습니다. 각 금칙어를 띄어쓰기로 구분해주세요'}

    wid_text = forms.TextInput(attrs={'class': 'form-control mb-3'})
    wid_email = forms.EmailInput(attrs={'class': 'form-control mb-3'})
    wid_password = forms.PasswordInput(attrs={'class': 'form-control mb-3'})

    wid_textarea = forms.Textarea(attrs={'class': 'form-control mb-3'})

class CreateUserForm(forms.ModelForm):
    d = FormDecorator()

    username = forms.CharField(widget=d.wid_text, error_messages=d.err_username, label='아이디')
    email = forms.EmailField(widget=d.wid_email, error_messages=d.err_email, validators=[d.val_email], label='이메일')
    password1 = forms.CharField(widget=d.wid_password, error_messages=d.err_password, label='비밀번호')
    password2 = forms.CharField(widget=d.wid_password, error_messages=d.err_password, label='비밀번호확인')

    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateUsernameForm(forms.ModelForm):
    d = FormDecorator()
    username = forms.CharField(widget=d.wid_text, error_messages=d.err_username, label='새로운 아이디')

    class Meta:
        model = User
        fields = ['username']

class UpdateEmailForm(forms.ModelForm):
    d = FormDecorator()
    email = forms.EmailField(widget=d.wid_email, error_messages=d.err_email, validators=[d.val_email], label='새로운 이메일')

    class Meta:
        model = User
        fields = ['email']

class UpdatePasswordForm(forms.ModelForm):
    d = FormDecorator()
    password = forms.CharField(widget=d.wid_password, error_messages=d.err_password, label='현재 비밀번호')
    password1 = forms.CharField(widget=d.wid_password, error_messages=d.err_password, label='새로운 비밀번호')
    password2 = forms.CharField(widget=d.wid_password, error_messages=d.err_password, label='새로운 비밀번호 확인')

    class Meta:
        model = User
        fields = ['password']

class LoginUserForm(AuthenticationForm):
    d = FormDecorator()
    username = forms.CharField(widget=d.wid_text, error_messages=d.err_username, label='아이디')
    password = forms.CharField(widget=d.wid_password, error_messages=d.err_password, label='비밀번호')

    error_messages = { 'invalid_login': '일치하는 정보를 찾을 수 없습니다. 아이디와 비밀번호를 확인하세요', 'inactive': '비활성화 된 계정입니다. 관리자에게 문의하세요', }
    
    # ModelForm이 아니므로(AuthenticationForm은 Form을 상속함) Meta가 필수는 아니지만
    # form_invalid()에서의 error 처리 코드를 재사용하기 위하여 정의하였다.
    class Meta:
        fields = ['username', 'password']
