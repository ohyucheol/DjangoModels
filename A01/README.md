# A01. 금칙어
username의 전부 또는 일부가 사용할 수 없는 단어인 경우에 관한 사례이다.

## 설계의 기준
### 기본 시나리오 및 유사사례
연예기획사 甲은 인기 아이돌 그룹 A, B, C와 전속계약을 체결하였다. A 그룹의 멤버는 alfa, bravo, charlie 이고, B 그룹의 멤버는 delta, echo, foxtrot, golf, hotel 이며, C 그룹의 멤버는 india, juliet, kilo, lima, mike 이다. 甲은 소속 그룹의 팬들을 위하여 웹 서비스를 제공하고자 한다. 서비스의 회원가입과 관련한 甲의 요구사항은 다음과 같다.
1. 가입시 각 이용자마다 example.com/**username**과 같이 자신의 username을 url로 하는 개인 페이지를 할당한다.
2. 이용자는 example.com/bigfanof**A**, example.com/ilove**charlie**와 같이 甲에 소속된 그룹의 명칭 또는 가수의 이름을 자신의 username에 포함할 수 있다.
3. 이용자는 example.com/**C**, example.com/**juliet**과 같이 甲에 소속된 그룹의 명칭 또는 가수의 이름만으로 된 username으로 가입할 수 없다.
4. 이용자는 example.com/**official**foxtrot과 같이 다른 이용자가 그 이용자를 甲 또는 甲의 직원이라고 혼동할 수 있는 단어를 username에 포함할 수 없다.
5. 이용자는 example.com/lima**sucks**와 같이 甲에 소속된 그룹 또는 가수의 명성을 손상시킬 수 있거나 공서양속에 반하는 단어를 username에 포함할 수 없다.
6. 이용자는 example.com/**K**, example.com/**quebec**과 같이 甲과 경쟁관계에 있는 연예기획사 乙에 소속된 그룹의 명칭 또는 가수의 이름을 username에 포함할 수 없다.
7. 甲은 username의 전부 또는 일부로 사용할 수 없는 단어를 추가, 삭제, 변경할 수 있다.
8. 甲은 부적절한 username을 사용하는 이용자에게 username의 변경을 요청할 수 있으며 상당한 기간이 지난 후에도 username을 변경하지 않는 경우 그 username을 url로 하는 개인 페이지로의 접속을 차단하거나 강제로 username을 변경할 수 있다.

### 법률, 시행령, 시행규칙 등
### (사실상의)표준, 관습, 실무사례, 문헌 등

## 구현의 대상
### 모델(Model)
### 뷰(View)
### 템플릿(Template)