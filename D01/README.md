# D01. 만화책
## 설계의 요지

## 설계의 기준
### 기본 시나리오 및 유사사례

### 법률, 시행령, 시행규칙 등
1. 출판문화산업진흥법 **제2조(정의)**, **제22조(간행물 정가 표시 및 판매)**
2. 출판문화산업진흥법 시행령 **제3조(간행물의 기록 사항)**, **제15조(간행물의 정가 표시 등)**
3. 도서관법 **제21조(국제표준자료번호)**
4. 도서관법 시행령 **제14조(국제표준자료번호의 부여)**
5. 주민등록법 **제24조(주민등록증의 발급 등)**

### (사실상의)표준, 관습, 실무사례, 문헌 등
0. 국립중앙도서관 한국서지표준센터 **<한국문헌번호편람>**
3. 국립중앙도서관 한국서지표준센터 **<한국도서번호통보서(개별도서)>**

## 구현의 대상
### 모델(Model)
1. 단행본(Book)

도서를 특정하는 방법이 문제된다. 주민등록법 제24조제2항에서는 사람을 성명, 사진, 주민등록번호로 특정한다. 같은 방식으로 도서를 특정하였다. 제목은 부제를 포함하여 작성할 수 있다(예:상실에 대하여 - 지금, 깊은 상실을 겪고 있는 당신에게). 사진은 웹 스토리지에 저장한 사진의 URL을 저장한다. ISBN은 하이픈 또는 공백을 포함한다.
* 제목(title / CharField)
* 사진(thumbnail / URLField)
* ISBN(isbn / CharField)
* 검색어(keyword / CharField)

2. 판형(Format)
* 단행본ID(book_id / IntegerField)
* 판차(edition / CharField)
* 쇄차(impression / CharField)
* 제본(binding / CharField)
* 치수(size / CharField)
* 매수(page / IntegerField)
* 중량(weight / DecimalField)

3. 십진분류법 등(DecimalClassification)
* 단행본ID(book_id / IntegerField)
* 부가기호(k_isbn / CharField)
* 한국십진분류법(kdc / CharField)
* 듀이십진분류법(ddc / CharField)

4. 저자, 편저자, 역자, 출판사
'사람과 권리' 부분에서 다룬다.

### 뷰(View)
### 템플릿(Template)