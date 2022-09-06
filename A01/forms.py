import json, os

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.validators import ASCIIUsernameValidator

from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

# validator, validation error, widget 등의 구성을 위한 FormDecorator
class FormDecorator:
    def val_banned(self, username):
        # banned.json의 구조
        # {
        # "full": ["alfa", "bravo", "charile"],
        # "part": ["delta", "echo", "foxtrot"]
        # }
        path = os.path.dirname(__file__) + '/banned.json'
        file = open(path)
        banned_keyword = json.load(file)

        for k in banned_keyword['full']:
            if username == k:
                raise ValidationError( '"%(banned)s"는 사용할 수 없는 아이디입니다', params={'banned': k})

        for k in banned_keyword['part']:
            if k in username:
                raise ValidationError( '아이디에 "%(banned)s"를 포함할 수 없습니다', params={'banned': k})

    val_azAZ09 = RegexValidator(regex='^([a-zA-Z0-9])+$')
    val_email = EmailValidator()
    val_azAZ09whitespace = RegexValidator(regex='^([a-zA-Z0-9\s])+$')

    # username을 검증하는 RegexValidator에는 username이 unique인지 판단하지 않는다.
    # 그럼에도 불구하고 unique error가 발생하는 것은 User 모델의 username field에서 unique 여부를 판단하기 때문이다.
    # 즉, ModelForm의 field는 form의 validation, model의 validation에서 각각 검증된다.

    err_username = {'unique' : '이미 사용중인 아이디입니다', 'required' : '아이디를 입력하세요', 'invalid' : '아이디에는 영문자와 숫자만 사용할 수 있습니다', 'max_length' : '아이디는 150자 이하여야 합니다', 'invalid_login':'입력하신 정보와 일치하는 계정이 없습니다'}
    err_email = {'required' : '이메일을 입력하세요', 'invalid' : '이메일 형식이 바르지 않습니다'}
    err_password = {'required' : '비밀번호를 입력하세요'}
    err_banned_keyword = {'invalid' : '금칙어에는 영문자와 숫자만 사용할 수 있습니다. 각 금칙어를 띄어쓰기로 구분해주세요'}

    wid_text = forms.TextInput(attrs={'class': 'form-control mb-3'})
    wid_email = forms.EmailInput(attrs={'class': 'form-control mb-3'})
    wid_password = forms.PasswordInput(attrs={'class': 'form-control mb-3'})

    wid_textarea = forms.Textarea(attrs={'class': 'form-control mb-3'})

# password validation(8자 이상) 등을 사용하지 않기 위하여 UserCreationForm 대신 ModelForm을 사용하였다.
class CreateUserForm(forms.ModelForm):
    d = FormDecorator()

    # 모델에 없는 field 또는 별도의 기능(validation 등)이 필요한 field들은 다음과 같이 새로 정의할 수 있다.
    # 새로 정의한 field의 경우 기본적으로 required 속성을 가지며 입력 여부가 validation의 대상이 된다.
    # 예컨대 email의 경우 입력하지 않는다면 required 속성에 의하여 한 번, EmailValidator()에 의하여 한 번,
    # 총 두 번의 required error가 발생한다.

    username = forms.CharField(widget=d.wid_text, error_messages=d.err_username, validators=[d.val_azAZ09, d.val_banned], label='아이디')
    email = forms.EmailField(widget=d.wid_email, error_messages=d.err_email, validators=[d.val_email], label='이메일')
    password1 = forms.CharField(widget=d.wid_password, error_messages=d.err_password, label='비밀번호')
    password2 = forms.CharField(widget=d.wid_password, error_messages=d.err_password, label='비밀번호확인')

    class Meta:
        # 이 ModelForm과 관련한 Model과 그 field를 지정하는 부분으로써 여기에서 지정한 field에 대해서는
        # model의 validation이 추가로 적용된다.
        model = User
        fields = ['username', 'email']

class UpdateUsernameForm(forms.ModelForm):
    d = FormDecorator()
    username = forms.CharField(widget=d.wid_text, error_messages=d.err_username, validators=[d.val_azAZ09], label='새로운 아이디')

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
    username = forms.CharField(widget=d.wid_text, error_messages=d.err_username, validators=[d.val_azAZ09, d.val_banned], label='아이디')
    password = forms.CharField(widget=d.wid_password, error_messages=d.err_password, label='비밀번호')

    error_messages = { 'invalid_login': '일치하는 정보를 찾을 수 없습니다. 아이디와 비밀번호를 확인하세요', 'inactive': '비활성화 된 계정입니다. 관리자에게 문의하세요', }
    
    # ModelForm이 아니므로(AuthenticationForm은 Form을 상속함) Meta가 필수는 아니지만
    # form_invalid()에서의 error 처리 코드를 재사용하기 위하여 정의하였다.
    class Meta:
        fields = ['username', 'password']

class UpdateBannedKeywordForm(forms.Form):
    d = FormDecorator()
    full = forms.CharField(widget=d.wid_textarea, error_messages=d.err_banned_keyword, validators=[d.val_azAZ09whitespace], label='아이디로 사용할 수 없는 단어')
    part = forms.CharField(widget=d.wid_textarea, error_messages=d.err_banned_keyword, validators=[d.val_azAZ09whitespace], label='아이디에 포함할 수 없는 단어')

    class Meta:
        fields = ['full', 'part']