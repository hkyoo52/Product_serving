# CI/CD

## 현업 개발 프로세스
#### 개발 환경
* Local : 각자의 컴퓨터에서 개발, 각자의 환경을 통일시키기 위해 Docker 사용
* DEV : Local에서 개발한 기능을 테스트 할 수 있는 환경, Test 서버
* Staging : Production 환경에 배포되기 전에 운영하거나 보안, 성능 측정하는 환경
* Production : 실제 서비스 운영하는 환경, 운영서버

#### 개발 환경 나누는 이유
* 실제 운영중인 서비스가 장애가 발생하면 안됨
* DEV = Staging = Production인 경우는 소스 코드 저장하면 바로 반영됨


## CI/CD 개념
#### Continuous Integreation(CI)
* 새롭게 작성한 코드 변경사항이 Build, Test 진행 후 Test Case 통과했는지 확인
* 지속적인 코드 품질 관리
* 10명의 개발자가 코드 수행하면 모두 CI 프로세스 진행

#### Continuous Deploy/Delivery(CD)
* 작성한 코드가 항상 신뢰 가능한 상태가 되면 자동으로 배포하는 과정
* CI 이후 CD 진행
* dev/staging/main 브랜치에 merge 될 경우 자동으로 서버 배포



# Github Action

## Github Action 소개
* workflow 자동화를 도와주는 도구

#### Test Code
- 특정 함수의 return 값이 어떻게 나오는지 확인하는 Test Code
- 특정 변수의 타입이 int가 맞는가?
- Unit Test, End to End Test

#### 배포
- Prod, Staging, Dev 서버에 코드 배포
- FTP로 파일 전송할 수도 있고, Docker Image를 Push하는 방법 등
- Node.js 등 다양한 언어 배포도 지원

#### 파이썬, 쉘, 스크립트 실행
- Github Repo에 저장된 스크립트를 일정 주기를 가지고 실행
- crontab의 대용
- 데이터 수집을 주기적으로 해야할 경우 활용할 수도 있음

#### Github Tag, Release 자동 설정
- Main 브랜치에 Merge 될 경우에 특정 작업 실행
- 기존 버전에서 버전 Up하기
- 새로운 브랜치 생성시 특정 작업 실행도 가능

#### 참고 사이트
* https://github.com/marketplace?type=actions
* https://github.com/sdras/awesome-actions

#### Github Action 제약 조건
- 하나의 Github Repository 당 Workflow는 최대 20개까지 등록할 수 있음
- Workflow에 존재하는 Job(실행)은 최대 6시간 실행할 수 있으며, 초과시 자동으로 중지됨
- 동시에 실행할 수 있는 Job 제한 존재

#### Github Action 사용 방식
1) 코드 작업
2) 코드 작업 후, Github Action으로 무엇을 할 것인지 생각
3) 사용할 Workflow 정의
4) Workflow 정의 후 정상 작동하는지 확인


## Github Action 사용할 배포



# Mask Classification Streamlit 배포하기

## Compute Engine에서 Streamlit 실행하기

## Github Action을 사용한 배포 자동화

