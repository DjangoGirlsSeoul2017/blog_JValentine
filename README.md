# Django Study Project 
 이 저장소는 장고를 공부하기 위헤 만든 곳입니다.
 
## 모델 구조

### 작성자 구조
|칼럼명|타입|용도|
|---|---|--|
|`id`|VARCHAR(128) NOT NULL|아이디|
|`password`|VARCHAR(512) NOT NULL|비밀번호|
|`writer_name`|VARCHAR(128) NOT NULL|필명|
|`email`|VARCHAR(256) NOT NULL|E-Mail 주소|
|`phone`|VARCHAR(64) NOT NULL|Mobile 번호|
|`create_date`|DATETIME NOT NULL|등록 날짜|
|`lastlogin_date`|DATETIME|마지막 로그인 날짜|


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