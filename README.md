# DjangoApps
**목적**  
이 과업은 데이터 모델을 유형별로 분류·설계함으로써 요구사항변경에 강건한 앱을 구현하고 이를 바탕으로 산업상 요청에 부응하는 웹 서비스를 개발하는 것을 목적으로 한다.

## 데이터 모델의 유형별 분류

### 사람과 권리
#### A. 자연인
#### B. 법인
#### C. 인격권 등

### 물건과 권리
#### D. 동산
#### E. 부동산
#### F. 지식재산권 등

### 사람, 물건, 권리의 상호작용
#### H. 법률행위
#### I. 사실행위
#### J. 기타 상호작용

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
모델 폼을 이용하지 아니하는 등의 특별한 사정이 없는 한 구현하지 아니한다.
* CreateView
* UpdateView
* DeleteView
해당 데이터를 삭제하기 전에 삭제 여부를 확인해야 하는 등의 특별한 사정이 없는 한 구현하지 아니한다.
4. Generic Date Views
다음의 뷰는 특별한 사정이 없는 한 구현하지 아니한다.
* ~~ArchiveIndexView~~
* ~~YearArchiveView~~
* ~~MonthArchiveView~~
* ~~WeekArchiveView~~
* ~~DayArchiveView~~
* ~~TodayArchiveView~~
* ~~DateDetailView~~

#### 3. 템플릿(Template)

### 구현의 방법
#### 1. Python/Django
#### 2. HTML, CSS, Javascript/Bootstrap
#### 3. AWS 등