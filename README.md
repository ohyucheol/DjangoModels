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
스트리밍 서비스를 구독하는 사람, SNS에 글을 올리는 사람, 온라인 쇼핑몰에서 신발을 구매하는 사람 등 통상의 개인 이용자가 '자연인'에 속한다. '자연인'은 Django의 기본 User 모델을 바탕으로 한다. 이 분류의 모델을 설계하는데에 참고한 민법상의 규정과 적용례(field)는 다음과 같다.
* 제781조(자의 성과 본) : 이용자를 특정하기 위한 아이디(username)와 비밀번호(password)
* 제781조(자의 성과 본) : 이용자를 지칭하기 위한 이름(first_name, last_name)
* 제18조(주소) : 이용자에 대해 의사표시를 송달하기 위한 또는 이용자를 특정하기 위한 이메일 주소(email)
* 제3조(권리능력의 존속기간) : 이용자가 회원가입을 한 때(date_joined), 이용자가 탈퇴했는지 여부(is_active)
* 제3조(권리능력의 존속기간) : 비회원(AnonymousUser)의 경우
* 제4조(성년), 제9조(성년후견개시의 심판) : 이용자의 권한(Permission) 또는 이들의 조합(Group)
* 제27조(실종의 선고), 제28조(실종선고의 효과) : 이용자의 최근 접속일(last_login), 이용자가 휴면회원(is_active)인지 여부
* 제29조(실종선고의 취소) : 휴면회원의 권리능력 회복(is_active) 여부

#### B. 법인
1. 사단법인, 재단법인, 주식회사, 유한회사 등의 법인이나 교회, 종중, 동창회 등의 비법인사단(재단) 또는 조합과 같이 그 자체로 서비스 내에서 단일한 권리의무의 주체가 되는 이용자가 '법인'에 속한다. 이들은 Django의 기본 User 모델을 바탕으로 하며 이용자의 특정과 관련하여 사업자등록번호 등을 이용할 수 있다는 점 등을 제외하면 '자연인'과 동일하다. 다만 이 '법인'의 구성원이 별도의 '자연인'으로 서비스에 가입하는 경우에는 다음 2호의 사항을 고려하여야 한다.

2. 다음 카페, 네이버 밴드, 구글 그룹스와 같이 서비스 내 이용자들의 집합 또한 '법인'에 속한다. 이들은 위 1호에서 살펴본 법인, 비법인사단 또는 조합과 달리 현실적·법률적 강제성이 없으므로 각 구성원간의 결합이 느슨하고 가입과 탈퇴가 빈번하다. 각 이용자가 2 이상의 '법인'에 가입할 수 있는 것은 물론이다. 이러한 경우에는 Django의 기본 User 모델을 사용하여 그 '법인'에 권리능력을 부여하는 것 보다는 별도의 모델을 이용하여 '법인'을 각 구성원의 공통된 속성으로써 다루는 것이 적절할 수 있다. 이 분류의 모델을 설계하는데에 참고한 민법상의 규정과 적용례는 다음과 같다.
* 제40조(사단법인의 정관) : 법인의 목적과 운영규칙
* 제31조(법인성립의 준칙) : 법인의 성립방법과 절차
* 제32조(비영리법인의 설립과 허가), 제38조(법인의 설립허가의 취소) : 법인에 대한 서비스 제공자의 허가 또는 취소
* 제37조(법인의 사무의 검사, 감독) : 법인의 활동에 대한 서비스 제공자의 검사·감독
* 제36조(법인의 주소) : 법인에 직접 접속할 수 있는 URL, 법인에 대해 의사표시를 송달하기 위한 이메일 주소 등
* 제58조(이사의 사무집행) : 법인을 대표하거나 관리하는 이용자
* 제703조(조합의 의의), 제716조(임의탈퇴), 제717조(비임의 탈퇴) : 이용자의 법인 가입과 탈퇴의 방법
* 제718조(제명) : 법인의 구성원인 이용자의 제명 방법
* 제77조(해산사유) : 법인의 해산 방법

#### C. 인격권 등
1. 프로필 사진, 자기소개, 학력, 경력, 전화번호 등 기본 User 모델에 포함되지 않는 통상의 개인정보·신용정보가 '인격권 등'에 속한다. 이 분류의 모델을 설계하는데에 참고한 민법상의 규정과 적용례는 다음과 같다.
* 제18조(주소) : 이용자에 대해 직접 접속할 수 있는 URL, 2 이상의 이메일 주소가 있는 경우에 보조 이메일 주소
* 제4조(성년) : 이용자가 성년인지 여부, 본인인증 등 이용자가 성년인지 확인할 수 있는 방법
* 제5조(미성년자의 능력) : 이용자가 미성년자의 경우 법정대리인의 동의가 있었는지 여부
* 제114조(대리행위의 효력), 제118조(대리권의 범위) : 서비스 내에서 법정대리인이 미성년자를 대리하는 경우 그 법정대리인의 권한

2. 이익배당청구권, 잔여재산분배청구권, 결의권, 소수사원권 등의 사원권, 친권, 부권, 상속권 등의 가족권, 그리고 노동권, 참정권 등 그 사람의 신분 기타 특정한 지위로 말미암아 발생하는 인격권 외 기타 권리가 '인격권 등'에 속한다. 이 분류의 모델을 설계하는데에 참고한 민법상의 규정과 적용례는 다음과 같다.
* 제56조(사원권의 양도, 상속금지) : 법인의 구성원으로서 각 이용자에게 부여된 특정한 권한

### 물건과 권리
전자상거래 서비스의 상품, 스트리밍 서비스의 영화 등 서비스 내 권리의 객체를 '물건'이라 한다. '허니버터칩', '이상한 변호사 우영우' 등의 사례에서 볼 수 있듯이 좋은 '물건'은 그 자체로 흡인력이 있으므로 이용자 획득과 유지의 한 축이 된다. 이용자가 늘어남에 따라 서비스에서 다루는 '물건' 또한 다양해지는 것이 일반적이다. 따라서 초기 단계에서부터 '물건'과 이들의 다양한 특성을 포함할 수 있는 모델의 설계가 필요하다.
<br><br>
민법에서는 물건을 유체물 및 전기 기타 관리할 수 있는 자연력(제98조) 즉, **'동산'과 '부동산'** 으로 구분한다. 그러나 웹 서비스에서는 콘텐츠와 같은 자연력 아닌 무체물을 취급하는 경우가 많다는 점, 이들도 서비스 내에서 권리의 객체가 될 수 있다는 점을 고려하여 '물건'의 분류에 **'지식재산권 등'** 을 포함하였다.

#### D. 동산·부동산
다음 각 호는 '동산·부동산'에 속하는 '물건'을 예시한 것이다.
1. 비누 한 상자, 담배 한 보루 등 각 구성물품이 대체로 균질하여 그 개성이 중요하지 않은 공산품
2. 미술품, 주문제작한 가방 등 유일하거나 개성이 중요한 동산, 그리고 위의 1호의 물건 중 일정한 방법으로 특정된 동산
3. 송이버섯, 문어, 오미자, 한우 등 산지, 수확시기 등에 따라 각 물건의 개성이 달라지는 자연물
4. 토지, 건물 등의 부동산
5. 다세대주택 중의 한 호(戶), 건물의 보일러실과 같은 부동산의 일부
<br><br>
위 1 내지 5호의 분류에 속하는 모델을 설계하는데에 참고한 민법상의 규정과 적용례는 다음과 같다.
* 제100조(주물, 종물) : 어떤 물건의 상용에 공하기 위한 목적으로 부속된 물건
* 제101조(천연과실, 법정과실) : 물건의 용법에 의하여 수취하는 산출물, 물건의 사용대가로 받는 금전 기타의 물건
* 제102조(과실의 취득) : 천연과실은 그 원물로부터 분리할 때 취득한다, 법정과실은 수취할 권리의 존속기간일수의 비율로 취득한다

6. 소유권, 점유권 등 '동산·부동산'과 관련한 '권리'도 이 분류에 속한다. 관련 모델을 설계하는데에 참고한 민법상의 규정과 적용례는 다음과 같다.
* 제211조(소유권의 내용) : 물건을 사용, 수익, 처분할 권리
* 제215조(건물의 구분소유) : 구분할 수 있는 물건의 일부와 그에 관한 권리
* 제256조(부동산에의 부합), 제257조(동산간의 부합), 제258조(혼화), 제259조(가공), 제260조(첨부의 효과) : 2 이상의 물건이 하나의 물건으로 된 경우
* 제262조(물건의 공유) : 물건의 권리자가 2 이상인 경우
* 제280조(존속기간을 약정한 지상권), 제284조(갱신과 존속기간) : 물건에 관한 권리의 존속기간
* 제349조(지명채권에 대한 질권의 대항요건) : 물건에 관한 권리를 다른 이용자에 대하여 주장하기 위하여 필요한 요건
* 제359조(과실에 대한 효력) : 과실에 관한 권리

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