# B01. 사업자등록정보
## 설계의 요지
### 1. 가입절차가 2 이상의 단계로 구성된 사례
이용자는 가입절차를 진행하는 동안 서비스 이용 약관 등에 대한 동의, 개인정보·신용정보 등의 입력, 계정정보입력 등을 수행한다. 이때 가입절차의 복잡도가 문제된다. 이 사례에서는 가입절차 중 이용자가 계정정보 외에도 사업자등록번호를 입력하여야 한다는 점, 이용자가 신용정보회사로부터 조회한 자신의 정보에 오류가 있는지를 검토·수정할 수 있어야 한다는 점, 전체 가입절차가 다소 복잡하다는 점을 고려하여 가입절차를 2 이상의 단계로 분할함으로써 이용자가 느낄 수 있는 불편함을 각 단계로 분산하였다.

### 2. 가입시 이용자가 입력해야 할 정보를 간소화 한 사례
서비스 내에서 추천, 맞춤형 광고 등 개인화 기능을 제공하기 위해서는 이용자로부터 필요한 정보를 수집하여야 한다. 필요한 정보는 방문한 페이지, 체류시간, 검색어 등 서비스 내에서 자동으로 수집할 수 있는 것과 성명, 주소, 사진 등 이용자로부터 입력받아야 하는 것으로 나눌 수 있다. 이때 이용자로부터 필요한 정보를 입력받는 방법이 문제된다. 이 사례에서는 기업(사업자)을 대상으로 서비스를 제공한다는 점, 사업자는 사업자등록번호로써 특정된다는 점, 기업정보는 신용정보회사로부터 조회할 수 있다는 점을 고려하여 회원가입시 이용자로부터 사업자등록번호만을 입력받고 기업명, 대표자명, 설립일자 등 그밖의 필요한 정보는 신용정보회사로부터 수집함으로써 이용자가 입력해야 할 정보를 간소화하였다.

### 3. 이용자의 유형에 따라 가입절차 중 일부를 생략한 사례
같은 서비스 내에서도 자연인과 법인, 매도인과 매수인 등과 같이 각 이용자의 역할은 서로 다를 수 있다. 이때 가입절차의 구성이 문제된다. 이 사례에서는 기업(사업자)을 대상으로 서비스를 제공한다는 점, 서비스 홍보 등의 이유로 잠재고객에 대해서도 회원가입을 허용한다는 점을 고려하여 사업자등록번호가 없는 예비창업자의 경우 가입절차 중 사업자등록번호를 입력하는 등의 단계를 생략할 수 있도록 구성하였다.

## 설계의 기준
### 기본 시나리오
행정사 甲은 지난 6월 A 광역자치단체에서 지방행정사무관으로 정년퇴직하였다. 甲은 A 지역의 신생·중소기업을 대상으로 각 기업이 자신의 업력·규모에 맞는 정부지원사업 등을 검색하고 甲에게 필요한 서류의 작성·제출의 대행을 위임하거나 상담·자문을 요청할 수 있는 웹 서비스를 제공하고자 한다. 서비스의 회원가입과 관련한 甲의 요구사항은 다음과 같다.
1. 가입시 각 기업마다 사업자등록번호를 입력받아 상태(계속사업자, 휴업자, 폐업자)를 조회할 수 있다.
2. 사업자등록번호를 이용하여 기업개요정보(기업명, 대표자명, 설립일자, 기업형태, 전화번호, 주소 등)를 조회할 수 있다.
3. 조회한 기업개요정보에 오류가 있는지를 이용자가 검토·수정할 수 있다.
4. 사업자등록번호, 대표자명, 설립일자를 이용하여 2호에서 조회한 기업개요정보가 진실한 것인지 검증할 수 있다.
5. 사업자등록번호가 없는 예비창업자의 경우 위 1 내지 4호의 과정을 생략하고 가입할 수 있다.

### 관련 법률, 시행령, 시행규칙 등
1. 행정사법
* 행정사의 업무 범위 등
2. 법인세법, 부가가치세법
* 사업자의 정의 등
3. 개인정보 보호법, 신용정보의 이용 및 보호에 관한 법률
* 개인정보·신용정보의 정의 등

### 관련 (사실상의)표준, 관습, 실무사례, 문헌 등
1. 개인정보보호위원회·한국인터넷진흥원 개인정보보호포털(privacy.go.kr) - \[알림마당\] - \[개인정보 바로알기\] - \[개인정보의 이해\]
2. 개인정보보호위원회 <개인정보보호 법령 및 지침 고시 해설서(2020.12)> 1.1.1.개인정보(p.10)
* 개인정보의 정의 및 개인정보에 해당하지 않는 정보에 관한 설명 등

3. 네이버 가입절차
* 약관 등에 대한 동의 - 아이디, 비밀번호, 이름, 생년월일, 성별, 본인확인이메일, 휴대전화 입력

4. 카카오계정 가입절차
* 기존 이메일 사용여부 확인 - 약관 등에 대한 동의 - 전화번호 입력 및 인증 - 비밀번호 입력 - 이름, 생년월일, 성별 입력

5. 구글 가입절차
* 성명, 아이디, 비밀번호 입력 - 전화번호, 복구 이메일 주소, 생년월일, 성별 입력 - 약관 등에 대한 동의


## 구현의 대상
### 모델(Model)
1. class User(AbstractUser):
* django.contrib.auth.models의 기본 User 모델을 그대로 사용한다.

### 뷰(View)
1. class About(TemplateView):
2. class CheckBusinessRegistrationNumberView(FormView):
3. class CheckBusinessInformationView(FormView):
4. class CreateUserView(CreateView):
5. class LoginUserView(LoginView):
6. class LogoutUserView(LogoutView):
7. class UpdateUsernameView(UpdateView):
8. class UpdateEmailView(UpdateView):
9. class UpdatePasswordView(UpdateView):

### 폼(Form)
1. class CheckBusinessRegistrationNumberForm(forms.Form):
2. class CheckBusinessInformationForm(forms.Form):
3. class CreateUserForm(forms.ModelForm):
4. class UpdateUsernameForm(forms.ModelForm):
5. class UpdateEmailForm(forms.ModelForm):
6. class UpdatePasswordForm(forms.ModelForm):
7. class LoginUserForm(AuthenticationForm):
8. class FormDecorator:

### 템플릿(Template)
1. base.html
* 다음 2 내지 10호의 템플릿에서 상단 헤더로 사용된다.
2. about.html
3. check-business-registraion-number.html
4. check-business-information.html
5. create-user.html
6. login-user.html
7. nav.html
* 다음 8 내지 10호의 템플릿에서 좌측 사이드바 내비게이션으로 사용된다.
8. update-username.html
9. update-email.html
10. update-password.html

### 기타