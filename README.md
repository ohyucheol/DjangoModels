# DjangoApps
이 과업은 데이터 모델의 유형별 분류기준을 마련함으로써 기획 및 설계상의 미비점을 사전에 식별하고 이를 바탕으로 다양한 산업상 요구에 대응할 수 있는 웹 서비스를 구현하는 것을 목적으로 한다.

## 배경
저명한 웹 서비스들의 면면을 본다. 네이버, 카카오, 라인, 쿠팡, 배달의 민족, 당근마켓, 토스, 센드버드 등... 이들은 정보통신기술을 이용하여 기존 산업의 전부 또는 일부를 확장·변경함으로써 고유한 지위를 획득하는데에 성공하였다. 기존 산업의 확장·변경에 관하여 보다 상세하게는 다양한 정보를 수집·처리·제공함으로써 이용자를 확보하고 이를 바탕으로 광고·선전서비스(네이버)를 제공하는 경우, 이용자와 이용자를 연결하여 통신서비스(카카오, 라인)를 제공하는 경우, 매도인과 매수인을 연결하여 전자상거래서비스(쿠팡, 배달의 민족, 당근마켓)를 제공하는 경우, 기존 서비스의 절차를 간소화하여 편의기능(토스)을 제공하는 경우, 다수 산업에서 공통적으로 사용하는 기능을 독립한 서비스로 구성(센드버드)하여 제공하는 경우 등을 예로 들 수 있다. 이들 서비스는 기존 산업의 문제점 중 일부를 해결하는 것만으로도 다수의 이용자와 막대한 부가가치를 확보할 수 있다는 것을 보여주는 사례로써 그 의미가 상당하다.
<br><br>
뒤이어 수많은 서비스가 명멸한다. 그러나 네카라쿠배당토...의 말석에 앉는 것은 고사하고 종업원 1인당 1억원의 매출을 확보하는 것조차 어려운 것이 현실이다. 이는 목표로 삼은 산업에 대한 이해와 구현의 실패에 기인한다. 산업에 관한 이해는 보통 창업자 또는 기획자에게 맡겨져 있다. 그렇다면 개발자의 역할은 무엇인가? 주어진 기획에 따라 일련의 기능을 구현하는 것만으로 충분한가?
<br><br>
설계와 구현은 보통 기획의 후행과정이므로 기획상의 요구사항이 서로 모순충돌하지는 않는지, 요구사항에 따른 각각의 기능이 서로 맞물려 돌아가는데에 필요한 구성요소가 누락되지는 않았는지 재차 검토하는 기회로 삼을 수 있다. 불특정다수를 대상으로 콘텐츠를 제공함으로써 광고수입을 얻는 것을 사업모델로 하였으나 콘텐츠 열람을 위해서는 반드시 회원가입이 필요한 경우, 매년 이용자의 생일마다 할인 쿠폰을 제공하기로 하였으나 본인인증 등의 기능이 누락되어 이용자가 임의로 생일을 수정할 수 있는 경우 등은 설계 및 구현과정에서 식별·조치할 수 있는 기획상 미비점의 한 예이다.
<br><br>
기획의도에 대한 충분한 이해를 바탕으로 설계 및 구현단계에서 서비스의 완성도를 높이기 위하여 최대 노력할 때 서비스의 산업상 이용가능성 또한 높아지는 것은 자명하다. 그러나 서비스의 완성도라는 추상적 목표의 수준은 각 단계를 수행하는 구성원의 경험 또는 능력에 의존한다는 점이 문제된다. 서비스의 설계와 구현에 관한 일정한 기준과 방법을 마련해야 할 필요가 여기에 있다.

## 데이터 모델의 유형별 분류
서비스의 산업상 이용가능성이라는 것은 달리 말해 '돈을 넣은 만큼 돈이 나오는가'라고 표현할 수 있다. 이용자는 자기가 서비스에 지불한 비용에 상응하는 이익을 기대한다. 이때 이익은 판매관리비용 절감, 근로여건 향상, 노동시간 감소, 재구매율 증가, 생산시간 단축 등 다양한 형태로 나타난다. 동시에 서비스 제공자는 이용자에게 더 많은 이익을 약속하면서 둘은 재산관계로 연결된다.
<br><br>
민법은 민사에 관한 일반법으로써 재산관계를 규율한다. 회원, 그룹, 상품, 광고, 예약, 구매, 배송, 동의, 취소 등 서비스가 다루는 대부분의 사항이 재산관계에 속한다. 민법은 재산관계라는 방대한 주제를 각 사안에 대하여 권리(의무)와 권리의 주체, 객체, 변동으로 나누어 기술한다. 이러한 분류를 이용하면 재산관계에 관한 일반사항을 충분히 포괄할 수 있다는 점에서 서비스의 설계와 구현에 민법의 아이디어를 차용하는 실익이 있다.
<br><br>
이 과업에서는 데이터 모델을 크게 '사람과 권리', '물건과 권리', '사람, 물건, 권리의 상호작용'으로 분류하였다. 각각은 권리의 주체, 권리의 객체, 권리의 변동에 대응한다. 주체가 없는 권리, 객체가 없는 권리 그리고 상호작용 없는 권리는 불완전하다. 데이터 모델을 분류하고 기준에 부합하는지 검토하는 작업을 통해서 취재·기획 단계에서 미처 발견하지 못한 불완전성을 식별하고 견련관계에 있는 모델을 빠짐없이 설계에 반영할 수 있다.

### 사람과 권리
서비스 내에서 권리의무의 주체가 되는 사람을 '이용자'라 한다. 이용자와 서비스 간의 상호작용, 이용자와 이용자 간의 상호작용 등 서비스 내 모든 작용은 이용자의 획득과 유지를 위하여 존재한다고 보아도 무리가 아니다. Django에서 기본 User 모델을 마련해두고 있다는 사실은 이용자가 서비스의 필수요소임을 방증한다. 서비스는 다양한 사람들을 이용자로 받아들이면서 성장한다. 따라서 초기 단계에서부터 이용자와 이들의 다양한 특성을 포함할 수 있는 모델의 설계가 필요하다. '사람과 권리'에서는 이용자와 관련한 모델을 **'자연인'**, **'법인'**, **'인격권 등'** 으로 나누어 살펴본다.

#### A. 자연인
스트리밍 서비스를 구독하는 사람, SNS에 글을 올리는 사람, 온라인 쇼핑몰에서 신발을 구매하는 사람 등 통상의 개인 이용자가 '자연인'에 속한다. 자연인은 Django의 기본 User 모델을 바탕으로 한다. 이 분류에서 고려하여야 할 사항은 다음과 같다.
* 특정 : 이용자는 이름(username)과 비밀번호(password)로 특정된다.
* 명칭 : 이용자는 성(last_name)과 명(first_name)으로 지칭할 수 있다.
* 주소 : 이용자에 대해 이메일 주소(email)을 표준으로 의사표시를 송달할 수 있다. 이용자는 동시에 2 이상의 주소를 가질 수 있다. 또한 이용자는 이메일 주소로 특정될 수 있다.
* 권리능력의 존속기간 : 이용자는 회원가입을 한 때(date_joined)로부터 서비스 내에서 권리의무의 주체가 된다. 또한 탈퇴한 때(is_active)로부터 서비스 내에서 권리능력을 상실한다. 회원가입 없이 서비스의 일부를 이용하는 비회원(AnonymousUser)도 있으나 이는 예외적인 것이다.
* 행위능력 : 정회원과 준회원을 구분하고 각 회원에게 서로 다른 기능을 제공하는 것과 같이 이용자마다 권한(Permission)을 달리 부여할 수 있다. 다수의 권한을 일정한 단위(Group)로 묶어 일괄적으로 관리할 수도 있다.
* 부재와 실종 : 상당한 기간동안 서비스에 접속(last_login)하지 않은 이용자에 대해서는 권리능력을 제한(is_active)를 제한할 수 있다.

#### B. 법인
#### C. 인격권 등

### 물건과 권리
#### D. 동산·부동산
#### E. 지식재산권 등

### 사람, 물건, 권리의 상호작용
#### F. 채권·채무
#### G. 계약
#### H. 기타 상호작용

## 데이터 모델의 설계와 구현

### 설계의 기준
#### 1. 기본 시나리오 및 유사사례
#### 2. 법률, 시행령, 시행규칙 등
#### 3. (사실상의)표준, 관습, 실무사례, 문헌 등

### 구현의 대상
#### 1. 모델(Model)
#### 2. 뷰(View)
#### 3. 폼(Form)
#### 4. 템플릿(Template)

### 구현의 방법
#### 1. Python/Django
#### 2. HTML, CSS, Javascript/Bootstrap
#### 3. AWS 등