from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import RegexValidator, EmailValidator

# 요구사항에 따라 validator, error_messages, widget 등 Form의 구성요소 대다수를 override 하여야 하므로,
# UserCreationForm 대신 ModelForm을 상속하여 Form을 구성하였다.
class UserCreateForm(forms.ModelForm):
    val1 = RegexValidator(regex='^([a-zA-Z0-9])+$') #로마자 및 아라비아 숫자만을 허용한다.
    val2 = EmailValidator()

    # username을 검증하는 RegexValidator에는 username이 unique인지 판단하지 않는다.
    # 그럼에도 불구하고 unique error가 발생하는 것은 User 모델의 username field에서 unique 여부를 판단하기 때문이다.
    # 즉, ModelForm의 field는 form의 validation, model의 validation에서 각각 검증된다.

    err1 = {'unique' : '이미 사용중인 아이디입니다', 'required' : '아이디를 입력하세요', 'invalid' : '아이디에는 영문자와 숫자만 사용할 수 있습니다'}
    err2 = {'required' : '이메일을 입력하세요', 'invalid' : '이메일 형식이 바르지 않습니다'}
    err3 = {'required' : '비밀번호를 입력하세요'}

    wid1 = forms.TextInput(attrs={'class': 'form-control mb-3'})
    wid2 = forms.EmailInput(attrs={'class': 'form-control mb-3'})
    wid3 = forms.PasswordInput(attrs={'class': 'form-control mb-3'})
    
    # 모델에 없는 field 또는 별도의 validation이 필요한 field 등은 다음과 같이 새로 정의할 수 있다.
    # 새로 정의한 field의 경우 기본적으로 required 속성을 가지며 입력 여부가 validation의 대상이 된다.
    # email의 경우 입력하지 않는다면 required 속성에 의하여 한 번, EmailValidator()에 의하여 한 번,
    # 총 두 번의 required error가 발생한다.
    username = forms.CharField(widget=wid1, error_messages=err1, validators=[val1])
    email = forms.EmailField(widget=wid2, error_messages=err2, validators=[val2])
    password1 = forms.CharField(widget=wid3, error_messages=err3)
    password2 = forms.CharField(widget=wid3, error_messages=err3)

    class Meta:
        # 이 ModelForm과 관련한 Model과 그 field를 지정하는 부분으로써 여기에서 지정한 field에 대해서는
        # model의 validation이 추가로 적용된다.
        model = User
        fields = ['username', 'email']