# D01. 만화책
## 설계의 요지
### 1. 표지, 권수 등의 정보를 이용하여 연속간행물의 각 구성요소를 구별한 사례
만화책은 제호로 호칭·특정할 수 있다. 이때 같은 제호의 연속간행물을 구성하는 각 만화책의 구별이 문제된다. 이 사례에서는 만화책은 각 권마다 표지가 다르다는 점, 각 권마다 권수를 표시한다는 점을 고려하여 표지, 권수를 이용하여 같은 제호의 연속간행물을 구성하는 각 만화책의 구별하였다.

### 2. 그림 파일을 클라우드 스토리지에 저장한 후 그 파일의 URL만을 데이터베이스에 저장한 사례
Django에서는 그림 파일을 저장할 수 있는 FileField, ImageField를 제공한다. 이 field를 이용하면 파일은 서버 내부의 스토리지(MEDIA 등)에 저장된다. 이때 서버의 저장용량 및 전송 대역폭이 문제된다. 이 사례에서는 그림 파일을 서비스 제공자만이 업로드한다는 점, 누구든지 그림 파일을 열람할 수 있다는 점을 고려하여 그림 파일을 클라우드 스토리지에 공개적(public)으로 저장하고 그 URL만을 데이터베이스에 저장하였다.

### 3. 물건에 그 물건의 고유한 속성이 아닌 임의의 속성을 부가한 사례
물건은 형상, 모양, 색채, 용도, 생산·판매부문, 수요자의 범위 등 다수의 속성으로 특정할 수 있다. 형상, 모양, 색채 등은 그 물건의 고유한 속성이라고 할 수 있겠으나 용도 등은 연필꽂이를 수저통으로 사용하는 것과 같이 혼용이 가능하므로 그 물건의 생산·판매부문, 수요자의 범위에 따라 달라질 수 있다. 이때 속성의 임의성이 문제된다. 이 사례에서는 단골손님을 대상으로 만화책을 배달·대여한다는 점, 대여 후 회수까지 상당 기간이 필요하다는 점을 고려하여 만화책에 '인기', '추천' 등 임의의 속성을 부가함으로써 만화책의 회전율을 조절할 수 있도록 하였다.

## 설계의 기준
### 기본 시나리오
만화대여점을 운영하는 甲은 최근 A 감염병의 영향으로 일 매출이 40% 이상 감소하였다. 甲은 매출 감소분을 벌충하기 위하여 단골손님을 대상으로 음료 등의 먹을거리와 함께 만화책을 배달·대여하는 웹 서비스를 제공하고자 한다. 서비스의 만화책과 관련한 甲의 요구사항은 다음과 같다.
1. 만화책은 제목, 표지, 권수, 작가로 특정한다.
2. 연속간행물이 아닌 경우(단행본) 권수의 입력을 생략할 수 있다.
3. 글·그림 작가, 번역가 등은 별도의 구분없이 작가 항목에 입력한다.
4. 만화책은 '웹툰', '무협', '순정', '추리' 등의 장르로 분류할 수 있다.
5. 만화책에는 '신간', '인기', '추천', '영화원작' 등의 태그를 2 이상 부가할 수 있다.

### 법률, 시행령, 시행규칙 등
1. 출판문화산업진흥법 **제2조(정의)**, **제22조(간행물 정가 표시 및 판매)**
2. 출판문화산업진흥법 시행령 **제3조(간행물의 기록 사항)**, **제15조(간행물의 정가 표시 등)**
3. 도서관법 **제21조(국제표준자료번호)**
4. 도서관법 시행령 **제14조(국제표준자료번호의 부여)**
5. 주민등록법 **제24조(주민등록증의 발급 등)**
6. 청소년보호법 **제2조(정의)**
7. 질병관리청장이 지정하는 감염병의 종류 고시 **제1호가목**

### (사실상의)표준, 관습, 실무사례, 문헌 등
1. 국립중앙도서관 한국서지표준센터 **<한국문헌번호편람>**
2. 국립중앙도서관 한국서지표준센터 **<한국도서번호통보서(개별도서)>**

## 구현의 대상
### 모델(Model)
1. 만화책(ComicBook)
* 제호(title / CharField)
* 표지(cover / URLField)
* 권수(number / IntegerField)
* 작가(author / CharField)
* 장르(genre / CharField)
* 태그(tag / CharField)

### 뷰(View)
1. class About(TemplateView):
2. class ListComicBookView(ListView):
3. class CreateComicBookView(CreateView):
4. class UpdateComicBookView(UpdateView):
5. class DeleteComicBookView(DeleteView):

### 폼(Form)
1. class ComicBookModelForm(forms.ModelForm):

### 템플릿(Template)
1. about.html
2. create-comicbook.html
3. update-comicbook.html
4. list-comicbook.html
5. delete-comicbook.html

### 기타
0. AWS IAM 등 권한 설정
* AWS Python SDK를 사용하는데에 필요한 IAM 등 권한 설정은 완료되어 있는 것으로 간주한다. 

1. AWS Python SDK(Boto3) 설치
* AWS S3를 사용하기 위해서는 다음과 같이 Python SDK(Boto3)를 설치하여야 한다.
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
HOST = 'https://s3.ap-northeast-2.amazonaws.com' # 서울 리전
BUCKET = 'bucket-name'
PREFIX_D01 = 'folder-name'
```