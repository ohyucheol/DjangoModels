# A01. 금칙어
## 설계의 요지
### 1. username으로 사용할 수 있는 문자를 제한한 사례
Django에서는 기본 User 모델의 username으로 150자 이내의 문자, 아라비아 숫자, \_, @, +, ., -를 사용할 수 있다. 문자는 로마자로 제한되지 않으므로 이용자는 한글 등을 username으로 사용할 수 있다. 이때 username의 검증(validation)이 문제된다. 이 사례에서는 각 이용자가 자신의 username을 url로 하는 개인 페이지를 가진다는 점, 각 문자 또는 언어별로 금칙어를 수집·처리하는데에는 과도한 비용이 발생한다는 점을 고려하여 username으로 사용할 수 있는 문자를 로마자와 아라비아 숫자로 제한하였다.
### 2. 소수의 특정 단어를 username의 전부 또는 일부로 사용할 수 없는 사례
username의 전부 또는 일부가 금칙어에 해당하는지를 판단하기 위해서는 이용자가 입력한 username을 수집·처리한 모든 금칙어와 비교하여야 한다. 이때 비교작업의 시간복잡도가 문제된다. 이 사례에서는 username으로 사용할 수 있는 문자를 로마자와 아라비아 숫자로 제한하고 있다는 점, 금칙어가 경업관계에 있는 다른 그룹의 명칭 또는 가수의 이름 등으로 그 수가 비교적 적다는 점, 가입 이후에도 서비스 제공자가 이용자의 username을 변경할 수 있다는 점을 고려하여 금칙어를 json 파일에 배열로 저장하고 Django에서 그 값을 username과 비교하였다.
### 3. 각 이용자간 상호작용을 위한 도구로 username을 사용한 사례
서비스 체류시간을 높이기 위하여 댓글, 채팅, 쪽지 등 이용자간 상호작용을 위한 기능을 도입할 수 있다. 이때 이용자의 특정과 상호작용 방법이 문제된다. 이 사례에서는 username은 서비스 내에서 유일하다는 점, 각 이용자가 다른 이용자의 이메일·SNS 등을 알 수 없게 함으로써 서비스 내에서만 상호작용하도록 유도할 필요가 있다는 점을 고려하여 자신의 username을 url로 하는 개인 페이지를 각 이용자간 상호작용을 위한 도구로 사용하였다.

## 설계의 기준
### 기본 시나리오
연예기획사 甲은 인기 아이돌 그룹 A, B와 전속계약을 체결하였다. A 그룹의 멤버는 alfa, bravo, charlie 이고, B 그룹의 멤버는 delta, echo, foxtrot, golf, hotel이다. 甲은 자사 소속 그룹의 팬들을 대상으로 팬 상호간 자신이 촬영·제작한 사진, 영상 또는 이를 이용한 2차저작물, 기념품 등을 공유·판매할 수 있는 웹 서비스를 제공하고자 한다. 서비스의 회원가입과 관련한 甲의 요구사항은 다음과 같다.
1. 가입시 각 이용자마다 example.com/**username**과 같이 자신의 username을 url로 하는 개인 페이지를 할당한다.
2. 이용자는 example.com/bigfanof**A**, example.com/ilove**charlie**와 같이 甲에 소속된 그룹의 명칭 또는 가수의 이름을 자신의 username에 포함할 수 있다.
3. 이용자는 example.com/**B**, example.com/**delta**과 같이 甲에 소속된 그룹의 명칭 또는 가수의 이름만으로 된 username으로 가입할 수 없다.
4. 이용자는 example.com/**official**foxtrot과 같이 다른 이용자가 그 이용자를 甲 또는 甲의 직원이라고 혼동할 수 있는 단어를 username에 포함할 수 없다.
5. 이용자는 example.com/golf**sucks**와 같이 甲에 소속된 그룹 또는 가수의 명성을 손상시킬 수 있거나 공서양속에 반하는 단어를 username에 포함할 수 없다.
6. 이용자는 example.com/**Z**, example.com/**yankee**과 같이 甲과 경업관계에 있는 연예기획사 乙에 소속된 그룹의 명칭 또는 가수의 이름을 username에 포함할 수 없다.
7. 甲은 username의 전부 또는 일부로 사용할 수 없는 단어를 추가, 삭제, 변경할 수 있다.
8. 甲은 부적절한 username을 사용하는 이용자에게 username의 변경을 요청할 수 있으며 상당한 기간이 지난 후에도 username을 변경하지 않는 경우 그 이용자의 서비스 이용을 제한할 수 있다.

### 법률, 시행령, 시행규칙 등
1. 상표법 **제2조(정의)**, **제89조(상표권의 효력)**, **제108조(침해로 보는 행위)**

### (사실상의)표준, 관습, 실무사례, 문헌 등
1. ISO 기본 로마자 및 아라비아 숫자(ISO/IEC 646)
* 정규표현식
    * 로마자와 아라비아 숫자만을 허용하는 경우 : ^([a-zA-Z0-9])+$
    * 로마자, 아라비아 숫자 및 공백만을 허용하는 경우 : ^([a-zA-Z0-9\s])+$

2. 네이버쇼핑 스마트스토어
* smartstore.naver.com/**username**

3. 인스타그램
* instagram.com/**username**

## 구현의 대상
### 모델(Model)
1. class User(AbstractUser):
* django.contrib.auth.models의 기본 User 모델을 그대로 사용한다.

### 뷰(View)
1. class About(TemplateView):
2. class CreateUserView(CreateView):
3. class LoginUserView(LoginView):
4. class LogoutUserView(LogoutView):
5. class MyPageView(TemplateView):
6. class UpdateUsernameView(UpdateView):
7. class UpdateEmailView(UpdateView):
8. class UpdatePasswordView(UpdateView):
9. class UpdateBannedKeywordView(FormView):

### 폼(Form)
1. class CreateUserForm(forms.ModelForm):
2. class LoginUserForm(AuthenticationForm):
3. class UpdateUsernameForm(forms.ModelForm):
4. class UpdateEmailForm(forms.ModelForm):
5. class UpdatePasswordForm(forms.ModelForm):
6. class UpdateBannedKeywordForm(forms.Form):
7. class FormDecorator:
* validator, (field)error_message, widget의 관리를 위한 클래스로써 각 Form에서 사용된다.

### 템플릿(Template)
1. base.html
* 다음 2 내지 10호의 템플릿에서 상단 헤더로 사용된다.
2. about.html
3. create-user.html
4. login-user.html
5. mypage.html
6. nav.html
* 다음 7 내지 10호의 템플릿에서 좌측 사이드바 내비게이션으로 사용된다.
7. update-username.html
8. update-email.html
9. update-password.html
10. update-banned-keyword.html

### 기타
1. banned-keyword.json
* 금칙어 목록을 저장한 파일로써 아이디로 사용할 수 없는 단어는 'full', 아이디에 포함할 수 없는 단어는 'part'로 구분하며 다음과 같은 형식으로 구성된다.
```json
{
    "full": ["alfa", "bravo", "charlie"],
    "part": ["delta", "echo", "foxtrot"]
}
```
* username과 금칙어를 비교하는 작업에 소요되는 시간은 다음과 같다.
    * full, part 각   100건 : 평균 0.0000091초(5회 수행)
    * full, part 각  3600건 : 평균 0.000025초(5회 수행)
    * full, part 각 14400건 : 평균 0.00082초(5회 수행)
    * 측정환경
        * MacBook Pro (13-inch, 2020, Four Thunderbolt 3 ports)
        * Processor : 2.3 GHz 쿼드 코어 Intel Core i7
        * RAM : 32GB 3733 MHz LPDDR4X

2. settings.py
* LoginView, LogoutView를 사용하는 경우 다음과 같이 redirect url을 설정해주어야 한다.
```python
LOGIN_REDIRECT_URL = '/A01/'
LOGOUT_REDIRECT_URL = '/A01/'
```
* 이용자가 가입한 이후 금칙어 정책이 변경되는 등의 이유로 이용자의 username에 금칙어가 포함되는 경우 관리자는 그 계정을 비활성화 할 수 있다. Django는 기본적으로 비활성화(inactive)된 이용자를 authenticate()를 이용하여 찾을 수 없으므로 비활성화 된 계정으로 로그인을 시도하면 invalid_login error가 발생한다. invalid_login error 만으로는 이용자가 자신이 가입하지 않은 것인지(또는 탈퇴한 것인지) 계정이 정지된 것인지 알 수 없으므로 비활성화된 계정의 로그인 시도에 대하여 inactive error를 발생시키기 위해서는 다음과 같이 authentication backend를 변경해주어야 한다.
```python
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']
```