# C01. 소설가
## 설계의 요지
### 1. 필명 등의 정보를 이용하여 동명이인을 구분한 사례
자연인은 성명으로 호칭·특정할 수 있다. 이때 동명이인의 구별이 문제된다. 이 사례에서는 소설가 중 필명 또는 별호(別號)를 사용하는 경우가 많다는 점, 생년월일, 출생지, 사진을 공개한 경우가 많다는 점을 고려하여 필명, 별호, 생년월일, 출생지, 사진을 이용하여 동명이인을 구별하였다.

### 2. 그림 파일을 클라우드 스토리지에 저장한 후 그 파일의 URL만을 데이터베이스에 저장한 사례
Django에서는 그림 파일을 저장할 수 있는 FileField, ImageField를 제공한다. 이 field를 이용하면 파일은 서버 내부의 스토리지(MEDIA 등)에 저장된다. 이때 서버의 저장용량 및 전송 대역폭이 문제된다. 이 사례에서는 그림 파일을 서비스 제공자만이 업로드한다는 점, 누구든지 그림 파일을 열람할 수 있다는 점을 고려하여 그림 파일을 클라우드 스토리지에 공개적(public)으로 저장하고 그 URL만을 데이터베이스에 저장하였다.

## 설계의 기준
### 기본 시나리오
A 문학관을 운영하는 재단법인 甲은 매월 마지막 수요일에 최근 작품을 발표한 소설가를 초청하여 '작가와의 만남' 행사를 개최한다. 甲은 시민을 대상으로 행사에 참가하는 소설가에 대한 정보를 제공하고 행사 전 그 소설가에게 전달할 사전질문을 받을 수 있는 웹 서비스를 제공하고자 한다. 서비스의 소설가 정보와 관련한 甲의 요구사항은 다음과 같다.
1. 성명 앞에는 필명 또는 별호를 표시한다.
2. 성명은 한글로 입력하되 필요한 경우 괄호안에 한문 또는 영문 성명을 병기할 수 있다.
3. 사진파일을 업로드 할 수 있다.
4. 저서, 약력은 별도의 서식없이 책날개 또는 띠지에 수록할 수 있을 정도의 분량(한 문단 이내)으로 입력한다.

### 관련 법률, 시행령, 시행규칙 등
1. 주민등록법
* 제24조(주민등록증의 발급 등)

### 관련 (사실상의)표준, 관습, 실무사례, 문헌 등
1. 한국소설가협회 입회원서
* 실명(한글, 한자), 필명(한글, 한자), 생년월일(생년월일, 주민등록번호, 출생지)
* 주소(우편번호, 주소, 전화번호), 이메일, 휴대폰, 은행계좌
* 학력 및 경력(년도, 학력 및 경력, 전공), 등단작품(년도, 작품 및 저서, 발표지 또는 출판사)
* 작품(년도, 작품 및 저서, 발표지 또는 출판사), 상훈기록(년도, 상훈내용, 수여기관)

2. 부산소설가협회 회원정보
* 성명, 필명, 출생년도, 주소, 전화번호, 이메일
* 학력, 등단, 작품활동, 수상경력, 주요경력

3. 교보문고 작가소개
* 작가소개, 학력, 수상, 경력, 추가정보

4. yes24 작가마을
* 대표작, 약력, 작가소개, 작가한마디, 수상경력, 활동내역, 작품리스트
* 작품밑줄긋기, 작가관련사진, 작가에게 한마디, 작가의 추천, 채녈예스기사, 독자마당

## 구현의 대상
### 모델(Model)
1. 소설가(NovelWriter)
* 성명(name / CharField)
* 필명(penname / CharField)
* *사진(picture / URLField)*
* 생년월일(birthday / CharField)
* 출생지(birthplace / CharField)
* 저서(work / TextField)
* 약력(history / TextField)

### 뷰(View)
1. class About(TemplateView):
2. class ListNovelWriterView(ListView):
3. class DetailNovelWriterView(DetailView):
4. class CreateNovelWriterView(CreateView):
* FileField로 입력받은 파일을 클라우드 스토리지에 저장하고 NovelWriter 모델에는 그 파일의 URL만을 저장한다.
5. class UpdateNovelWriterView(UpdateView):
* FileField로 입력받은 파일을 클라우드 스토리지에 저장하고 NovelWriter 모델에는 그 파일의 URL만을 저장한다.
6. class DeleteNovelWriterView(DeleteView):

### 폼(Form)
1. class NovelWriterModelForm(forms.ModelForm):
* 성명(name / CharField)
* 필명(penname / CharField)
* *사진 파일(picture_file / FileField)*
	* 모델과 달리 FileField로써 파일을 업로드 할 수 있다.
* 생년월일(birthday / CharField)
* 출생지(birthplace / CharField)
* 저서(work / TextField)
* 약력(history / TextField)

### 템플릿(Template)
1. base.html
* 다음 2 내지 7호의 템플릿에서 상단 헤더로 사용된다.
2. about.html
3. list-writer.html
4. detail-writer.html
5. create-writer.html
6. update-writer.html
7. delete-writer.html

### 기타
0. AWS IAM 등 권한 설정
* AWS Python SDK를 사용하는데에 필요한 IAM 등 권한 설정은 완료되어 있는 것으로 간주한다. 

1. AWS Python SDK(Boto3) 설치
* AWS S3를 사용하기 위해서는 다음과 같이 SDK(Boto3)를 설치하여야 한다.
```bash
pip install boto3
```

2. AWS Credntials 및 Region 설정
* AWS S3를 사용하기 위해서는 Credential을 설정하여야 한다. Boto3는 기본적으로 \~/.aws/credentials을 검색하므로 이 파일에 다음과 같이 키와 시크릿 키를 저장한다.
```bash
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```
* 또한 AWS의 각 서비스가 동작하는 리전을 설정하여야 한다. Boto3는 기본적으로 \~/.aws/config를 검색하므로 이 파일에 다음과 같이 리전(이 사례에서는 서울 리전)을 저장한다.
```bash
	[default]
region=ap-northeast-2
```

3. settings.py
* AWS S3를 사용하기 위해서는 다음과 같이 호스트, 버킷명, 폴더명을 지정해주어야 한다.
```python
S3_HOST = 'https://s3.ap-northeast-2.amazonaws.com' # 서울 리전
BUCKET_C01 = 'bucket-name'
PREFIX_C01 = 'folder-name'
```