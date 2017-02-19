# Django Study Project 
이 저장소는 장고를 공부하기 위해 만든 곳입니다.

## 모델 구조

### 작성자 Custom 추가된 구조
|칼럼명|타입|용도|
|---|---|---|
|`writer_name`|VARCHAR(128) NOT NULL|필명|
|`phone`|VARCHAR(64)|Mobile 번호|

### Post 구조
|칼럼명|타입|용도|
|---|---|---|
|`id`|VARCHAR(128) NOT NULL|작성자|
|`writer`|VARCHAR(128) NOT NULL|필명|
|`title`|VARCHAR(128) NOT NULL|Post 제목|
|`text`|TEXT|Post 내용|
|`publish`|VARCHAR(1)|출판 여부|
|`created_date`|DATETIME NOT NULL|작성 날짜|
|`lastedit_date`|DATETIME NOT NULL|최종 수정 날짜|
