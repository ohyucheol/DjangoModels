# DjangoApps
이 과업은 데이터 모델을 유형별로 분류함으로써 설계상의 미비점을 식별하고 요구사항변경에 강건한 앱을 구현하고 이를 바탕으로 산업상 요청에 부응하는 웹 서비스를 개발하는 것을 목적으로 한다.

## 배경
저명한 웹 서비스들의 면면을 본다. 네이버, 카카오, 라인, 쿠팡, 배달의 민족, 당근마켓, 토스, 센드버드 등... 이들은 정보통신기술을 이용하여 기존 산업의 전부 또는 일부를 확장·변경함으로써 고유한 지위를 획득하는데에 성공하였다. 기존 산업의 확장·변경에 관하여 보다 상세하게는 다양한 정보를 수집·처리·제공함으로써 이용자를 확보하고 이를 바탕으로 광고·선전서비스(네이버)를 제공하는 경우, 이용자와 이용자를 연결하여 통신서비스(카카오, 라인)를 제공하는 경우, 매도인과 매수인을 연결하여 전자상거래서비스(쿠팡, 배달의 민족, 당근마켓)를 제공하는 경우, 기존 서비스의 절차를 간소화하여 편의기능(토스)을 제공하는 경우, 다수 산업에서 공통적으로 사용하는 기능을 독립한 서비스로 구성(센드버드)하여 제공하는 경우 등을 예로 들 수 있다. 이들 서비스는 기존 산업의 문제점 중 일부를 해결하는 것만으로도 다수의 이용자와 막대한 부가가치를 확보할 수 있다는 것을 보여주는 사례로써 그 의미가 상당하다.<br>
<br>
뒤이어 수많은 서비스가 명멸한다. 그러나 네카라쿠배당토...의 말석에 앉는 것은 고사하고 종업원 1인당 1억원의 매출을 확보하는 것조차 어려운 것이 현실이다. 이는 목표로 삼은 산업에 대한 이해와 구현의 실패에 기인한다. 산업에 관한 이해는 보통 창업자 또는 기획자에게 맡겨져 있다. 그렇다면 구현은 어떠한가? 산업에 대해 이해하고자 노력하였는가? 산업상 요청을 빠짐없이 담아내었는가? 요구사항변화에 기민하게 대응하였는가? 약정한 시기에 지체없이 필요한 기능을 제공하였는가? 이 과업은 이러한 질문에 관하여 그간 백엔드 엔지니어로서의 고민을 정리한 것이다.

## 데이터 모델의 유형별 분류
서비스의 산업상 이용가능성이라는 것은 달리 말해 '돈을 넣은 만큼 돈이 나오는가'라고 표현할 수 있다. 이용자는 자기가 서비스에 지불한 비용에 상응하는 이익을 기대한다. 이때 이익은 판매관리비용 절감, 근로여건 향상, 노동시간 감소, 재구매율 증가, 생산시간 단축 등 다양한 형태로 나타난다. 동시에 서비스 제공자는 이용자에게 더 많은 이익을 약속하면서 둘은 재산관계로 연결된다.<br>
<br>
민법은 민사에 관한 일반법으로써 재산관계를 규율한다. 회원, 그룹, 상품, 광고, 예약, 구매, 배송, 동의, 취소 등 서비스가 다루는 대부분의 사항이 재산관계에 속한다. 민법은 재산관계라는 방대한 주제를 각 사안에 대하여 권리(의무)와 권리의 주체, 객체, 변동으로 나누어 기술한다. 이러한 분류를 이용하면 재산관계에 관한 일반사항을 충분히 포괄할 수 있다는 점에서 서비스의 설계와 구현에 민법의 아이디어를 차용하는 실익이 있다.<br>
<br>
이 과업에서는 데이터 모델을 '사람과 권리', '물건과 권리', '사람, 물건, 권리의 상호작용'으로 분류하였다. 각각은 권리의 주체, 권리의 객체, 권리의 변동에 대응한다. 주체가 없는 권리, 객체가 없는 권리 그리고 상호작용 없는 권리는 불완전하다. 데이터 모델을 분류하고 기준에 부합하는지 검토하는 작업을 통해서 취재·기획 단계에서 미처 발견하지 못한 불완전성을 식별하고 견련관계에 있는 모델을 빠짐없이 설계에 반영할 수 있다.<br>
<br>
구현해야 할 모델을 확정한 다음에는 각 모델의 일반적인 특성을 설계에 반영하여야 한다. 이에 다음과 같은 세부기준을 마련하였다.

### 사람과 권리
'사람과 권리'에서는 각 모델을 '자연인', '법인', '인격권 등'으로 분류하였다.

#### A. 자연인
'자연인'은 서비스 이용자로서 다른 모델들 뿐만 아니라 서비스 제공자와 상호작용하는 주체가 된다. 따라서 서비스 제공자는 각 이용자를 특정하고 그에게 의사표시를 할 방법을 마련하여야 한다. 이때 '자연인', 즉 개인을 특정하기 위한 정보는 <개인정보보호법>, <신용정보의 이용 및 보호에 관한 법률> 등에 의해 규율된다는 점을 고려하여야 한다.<br>
구체적인 사례는 다음과 같다.
* A01. 금칙어
	* username으로 사용할 수 있는 문자를 제한한 사례
	* 소수의 특정 단어를 username의 전부 또는 일부로 사용할 수 없는 사례
	* 각 이용자간 상호작용을 위한 도구로 username을 사용한 사례

#### B. 법인
'법인'은 '자연인'과 마찬가지로 서비스 제공자와 상호작용하는 주체가 된다. 하지만 '법인'은 개인이 아니므로 '법인'을 특정하기 위한 정보에 관한 보호는 다소 완화되어 있다. '법인'은 사람 또는 재산의 모임에 대해 인격을 부여한 것이므로 '법인' 이용자에게는 다수의 개인 또는 권리가 속할 수 있다는 점을 고려하여야 한다.
* B01. 사업자등록정보
	* 가입절차가 2 이상의 단계로 구성된 사례
	* 가입시 이용자가 입력해야 할 정보를 간소화 한 사례
	* 이용자의 유형에 따라 가입절차 중 일부를 생략한 사례

#### C. 인격권 등
한 사람이 가수이면서 동시에 배우일 수 있는 것과 같이 사람은 하나 이상의 속성을 가질 수 있다는 점에서 '인격권 등'을 별도의 모델로 분류할 실익이 있다. 또한 이용자가 아닌 사람, 즉 데이터로서의 사람을 '인격권 등'으로 분류하면 이후 그 사람이 이용자가 되는 경우에 기존의 데이터와 새로운 이용자를 간이한 방법으로 연결할 수 있다. 사람의 개인정보나 신용정보를 분리하여 보관할 수 있다는 보안상의 이점은 물론이다.
* C01 소설가
	* 필명 등의 정보를 이용하여 동명이인을 구분한 사례
	* 그림 파일을 클라우드 스토리지에 저장한 후 그 파일의 URL만을 데이터베이스에 저장한 사례

### 물건과 권리
'물건과 권리'에서는 각 모델을 '동산', '부동산', '지식재산권 등'으로 분류하였다. '동산'은 종류가 다양하고 같은 종류 안에서도 형상, 모양, 기능 등의 차이로 다시 한 번 나누어 진다는 점에서 이를 어떻게 특정할 것인지를 고려하여야 한다. 농수산물과 같은 자연물의 경우 각각이 완전히 동일할 수는 없다는 점 또한 중요한 문제이다. 반면 '부동산'은 대부분 그 형상, 모양, 기능이 유일하고 주소, 지번으로 특정이 가능하다는 점에서 '동산'과 차이가 있다.<br>
<br>
물건은 그 물건의 속성에 의하여 특정되므로(이 점에서 그 자체로 유일하게 특정되는 사람과 구분된다) '물건과 권리'에서는 물건의 속성을 별도의 모델로 분리하지 않고 그 물건을 표상하는 모델에 포함하였다. 물건 중에서도 특히 '지식재산권 등'은 형태가 없는 무체물로써 각 모델이 구체적인 내용에 의하여 특정되므로 그 모델을 구성하는 요소를 어느 수준까지 구현할 것인지를 고려하여야 한다. '지식재산권 등'을 구성하는 요소에는 글, 그림, 영상, 수식, 소스코드 등이 있으며 그 종류와 형식이 무척 다양하다는 점에서 특색이 있다.

#### D. 동산
* D01. 만화책
	* 표지, 권수 등의 정보를 이용하여 연속간행물의 각 구성요소를 구별한 사례
	* 그림 파일을 클라우드 스토리지에 저장한 후 그 파일의 URL만을 데이터베이스에 저장한 사례
	* 물건에 그 물건의 고유한 속성이 아닌 임의의 속성을 부가한 사례

#### E. 부동산
* E01. 회의실
	* 명칭, 주소(호수) 등을 이용하여 건물의 일부를 특정한 사례
	* 그림 파일을 클라우드 스토리지에 저장한 후 그 파일의 URL만을 데이터베이스에 저장한 사례
	* 글, 그림, 영상 등을 이용하여 물건의 가변적·복합적 속성을 기술한 사례

#### F. 지식재산권 등
* F01. 게시물
	* 글, 그림, 영상 등 다수의 구성요소를 이용하여 게시물을 구성한 사례
	* 임의의 키워드를 이용하여 게시물을 분류한 사례
	* User 모델의 id를 이용하여 이용자와 게시물을 연결한 사례

### 사람, 물건, 권리의 상호작용
'사람, 물건, 권리의 상호작용'에서는 각 모델을 '채권·채무', '법률행위', '사실행위 등'으로 분류하였다. '법률행위'는 의사표시, 대리, 조건과 기한, 무효와 취소, 기간, 소멸시효 등 민법총칙에서 규율하는 법률행위의 일반사항을 고려하여야 한다. 또한 상품의 가격과 같이 '물건과 권리'의 속성으로 보이지만 실제로는 '계약'에 해당하는 것에 주의하여야 한다.<br>
<br>
'사실행위 등'은 대량의 데이터가 정형적으로 수집·처리되고 작성된 이후 변동이 거의 없으며 사람의 사상 또는 감정이 포함되어 있지 않다는 점에서 '지식재산권 등'과 구분된다. 따라서 서비스의 내부 또는 외부에서 필요한 수준의 데이터를 경제적으로 처리할 수 있는 방법을 고려하여야 한다.

#### G. 채권·채무
#### H. 법률행위
#### I. 사실행위 등

## 데이터 모델의 설계와 구현

### 설계의 기준
#### 1. 기본 시나리오 및 유사사례
#### 2. 법률, 시행령, 시행규칙 등
#### 3. (사실상의)표준, 관습, 실무사례, 문헌 등

### 구현의 대상
#### 1. 모델(Model)
#### 2. 뷰(View)
1. Base Views
* View
* TemplateView
* RedirectView
2. Generic Display Views
* ListView
* DetailView
3. Generic Editing Views
* FormView
* CreateView
* UpdateView
* DeleteView
4. Generic Date Views
* ArchiveIndexView
* YearArchiveView
* MonthArchiveView
* WeekArchiveView
* DayArchiveView
* TodayArchiveView
* DateDetailView

#### 3. 폼(Form)
#### 4. 템플릿(Template)

### 구현의 방법
#### 1. Python/Django
#### 2. HTML, CSS, Javascript/Bootstrap
#### 3. AWS 등