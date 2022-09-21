# D02. 회의실
## 설계의 요지
### 1. 명칭, 주소(호수) 등을 이용하여 건물의 일부를 특정한 사례
건물은 그 건물 전체를 사용할 수도 있고 일부만을 사용할 수도 있다. 이때 회의실과 같이 건물의 일부분을 특정하는 방법이 문제된다. 이 사례에서는 각 방실(房室)이 벽으로 구분되고 별도의 출입문이 있다는 점, 각 방실에는 명칭, 호수(號數) 등을 기재한 표찰이 있다는 점을 고려하여 명칭, 주소(호수)를 이용하여 건물의 일부를 특정하였다.

### 2. 그림 파일을 클라우드 스토리지에 저장한 후 그 파일의 URL만을 데이터베이스에 저장한 사례
Django에서는 그림 파일을 저장할 수 있는 FileField, ImageField를 제공한다. 이 field를 이용하면 파일은 서버 내부의 스토리지(MEDIA 등)에 저장된다. 이때 서버의 저장용량 및 전송 대역폭이 문제된다. 이 사례에서는 그림 파일을 서비스 제공자만이 업로드한다는 점, 누구든지 그림 파일을 열람할 수 있다는 점을 고려하여 그림 파일을 클라우드 스토리지에 공개적(public)으로 저장하고 그 URL만을 데이터베이스에 저장하였다.

### 3. 글, 그림, 영상 등을 이용하여 물건의 가변적·복합적 속성을 기술한 사례
건물은 증·개축, 대수선, 리모델링 등으로 인하여 그 성질이 이전과 상당히 달라질 수 있다. 또한 수도·전기·통신시설 등 다수의 종물(從物) 내지 부합물을 구성요소로 포함할 수 있다. 이때 믈건의 가변적·복합적 속성의 기술이 문제된다. 이 사례에서는 회의실에 음향·영상·기타시설이 구비되어 있다는 점, 각 시설들로 인하여 그 건물(의 일부)이 회의실로써 기능할 수 있다는 점을 고려하여 글, 그림, 영상 등을 이용하여 회의실의 속성을 기술하였다.

## 설계의 기준
### 기본 시나리오
창업보육센터를 운영하는 재단법인 甲은 전용면적 500㎡의 공간에 회의실, 입찰실, 공유사무실 등을 두고 30여개 입주기업을 지원하고 있다. 최근 대면영업이 증가세로 돌아서면서 회의실 예약을 두고 입주자간 갈등이 발생하고 있다. 甲은 입찰실을 회의실로 리모델링하는 동시에 입주자를 대상으로 일시를 정하여 회의실을 예약할 수 있는 웹 서비스를 제공하고자 한다. 서비스의 회의실과 관련한 甲의 요구사항은 다음과 같다.
1. 회의실은 명칭과 주소로 특정한다.
2. 이용자는 사진으로 회의실의 형상을 확인할 수 있다.
3. 이용자는 회의실의 면적·수용인원을 확인할 수 있다.
4. 이용자는 회의실의 음향·영상·기타시설을 확인할 수 있다.
5. 이용자는 이용규칙 등 그밖의 필요한 정보를 확인할 수 있다.

### 법률, 시행령, 시행규칙 등
1. 건축물대장의 기재 및 관리 등에 관한 규칙 **제5조(건축물대장의 작성방법)**, **별지 제1호 서식 일반건축물대장(갑)**
2. 학원의 설립ㆍ운영 및 과외교습에 관한 법률 **제6조(학원 설립ㆍ운영의 등록)**
3. 학원의 설립ㆍ운영 및 과외교습에 관한 법률 시행령 **제5조(학원 설립ㆍ운영의 등록)**
4. 학원의 설립ㆍ운영 및 과외교습에 관한 법률 시행규칙 **제5조(조건부설립)**, **별지 제6호서식 시설ㆍ설비계획서**
5. 중소기업창업 지원법 **제10조(창업 활성화 지원사업의 추진 등)**, **제53조(창업보육센터사업자의 지정 등)**
6. 중소기업창업 지원법 시행령 **제6조(창업 활성화 지원사업)**
7. 창업보육센터 운영요령 **제2조(정의)**

### (사실상의)표준, 관습, 실무사례, 문헌 등
1. 공유누리
* 상세설명(수용인원, 이용시간, 이용요금, 직접 준비·정리 여부, 문의전화), 주의사항, 연관자원

2. 대한상공회의소
* 장소, 회의실명, 규모, 소개 사진·동영상, 수용인원
* 회의실 특징, 문의 연락처
* 이용요금, 주차권, 동시통역제공여부, 기자재사용료, 현수막

3. 회의실닷컴
* 시설안내 일반
* 영업시간, 휴무일, 입퇴실시간, 결제구분, 평점, 수용형태, 편의시설, 식음료, 수화물, 주차
* 임차료, 면적, 최저이용시간, 수용인원, 부가서비스, 레이아웃

## 구현의 대상
### 모델(Model)
1. 회의실(MeetingRoom)
* 명칭(name / CharField)
* 주소(address / CharField)
* 사진(picture / URLField)
* 면적(space / DecimalField)
* 수용인원(capacity / IntegerField)
* 음향시설(audio / CharField)
* 영상시설(video / CharField)
* 기타시설(other / CharField)
* 상세설명(information / TextField)

### 뷰(View)
1. class About(TemplateView):
2. class ListMeetingRoomView(ListView):
3. class DetailMeetingRoomView(DetailView):
4. class CreateMeetingRoomView(CreateView):
5. class UpdateMeetingRoomView(UpdateView):
6. class DeleteMeetingRoomView(DeleteView):
7. def modal_list_file(request):
* tinyMCE와 AWS S3를 이용하여 파일 목록 표시, 삭제 기능을 수행한다.
8. def modal_list_upload(request):
* tinyMCE와 AWS S3를 이용하여 파일 업로드 기능을 수행한다.

### 폼(Form)
1. class MeetingRoomModelForm(forms.ModelForm):

### 템플릿(Template)
1. base.html
* 다음 2 내지 7호의 템플릿에서 상단 헤더로 사용된다.
2. about.html
3. list-meetingroom.html
4. detail-meetingroom.html
5. create-meetingroom.html
6. update-meetingroom.html
7. delete-meetingroom.html

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
PREFIX_D02 = 'folder-name'
```

4. tinyMCE
* tinyMCE(CDN 호스팅)를 사용하기 위해서는 다음과 같이 필요한 스크립트(tinymce.min.js)를 탑재한 후 texarea를 tinyMCE를 이용하여 초기화하여야 한다.
```html
<script src="https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js" referrerpolicy="origin"></script>
<script>
  tinymce.init({
    selector: 'textarea',
    plugins: 'image media table preview',
    menubar: 'edit insert format table help',
    toolbar: 'undo redo | blocks | bold italic | alignleft aligncentre alignright alignjustify | indent outdent | bullist numlist | upload image media table | preview ',
    language: 'ko_KR',
    setup: (editor) => {
      editor.ui.registry.addButton('upload', {
        icon: 'gallery',
        onAction: () => editor.windowManager.openUrl({
          title: '파일 관리',
          url: '{% url 'D02:modal-list-file' %}',
        })  //onAction
      }); //editor.ui.registry.addButton
    }, //setup
  }).then((editors) => {
    //do something
  });
</script>
```