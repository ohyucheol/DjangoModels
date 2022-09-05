from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import RegexValidator, EmailValidator

# validator, validation error, widget 등의 구성을 위한 FormDecorator
class FormDecorator:
    # username을 검증하는 RegexValidator에는 username이 unique인지 판단하지 않는다.
    # 그럼에도 불구하고 unique error가 발생하는 것은 User 모델의 username field에서 unique 여부를 판단하기 때문이다.
    # 즉, ModelForm의 field는 form의 validation, model의 validation에서 각각 검증된다.

    val_azAZ09 = RegexValidator(regex='^([a-zA-Z0-9])+$')
    val_email = EmailValidator()

    err_username = {'unique' : '이미 사용중인 아이디입니다', 'required' : '아이디를 입력하세요', 'invalid' : '아이디에는 영문자와 숫자만 사용할 수 있습니다'}
    err_email = {'required' : '이메일을 입력하세요', 'invalid' : '이메일 형식이 바르지 않습니다'}
    err_password = {'required' : '비밀번호를 입력하세요'}

    wid_text = forms.TextInput(attrs={'class': 'form-control mb-3'})
    wid_email = forms.EmailInput(attrs={'class': 'form-control mb-3'})
    wid_password = forms.PasswordInput(attrs={'class': 'form-control mb-3'})

# validator 등을 부가한 field를 포함하는 ModelForm의 구성을 위한 CreateUserForm
class CreateUserForm(forms.ModelForm):
    d = FormDecorator()

    # 모델에 없는 field 또는 별도의 기능(validation 등)이 필요한 field들은 다음과 같이 새로 정의할 수 있다.
    # 새로 정의한 field의 경우 기본적으로 required 속성을 가지며 입력 여부가 validation의 대상이 된다.
    # 예컨대 email의 경우 입력하지 않는다면 required 속성에 의하여 한 번, EmailValidator()에 의하여 한 번,
    # 총 두 번의 required error가 발생한다.

    username = forms.CharField(widget=d.wid_text, error_messages=d.err_username, validators=[d.val_azAZ09], label='아이디')
    email = forms.EmailField(widget=d.wid_email, error_messages=d.err_email, validators=[d.val_email], label='이메일')
    password1 = forms.CharField(widget=d.wid_password, error_messages=d.err_password, label='비밀번호')
    password2 = forms.CharField(widget=d.wid_password, error_messages=d.err_password, label='비밀번호확인')

    class Meta:
        # 이 ModelForm과 관련한 Model과 그 field를 지정하는 부분으로써 여기에서 지정한 field에 대해서는
        # model의 validation이 추가로 적용된다.
        model = User
        fields = ['username', 'email']