# 백엔드 프로그래밍

## Server 구성 Use Case
- 앱/웹 서비스의 서버가 존재
- 머신러닝 서비스의 서버가 존재
- 서비스 서버에서 머신러닝 서버에 예측 요청하며 통신함(혹은 서비스 서버의 한 프로세스로 실행)

## Server의 형태
* 모놀리식 아키텍처 : 하나의 큰 서버 -> 모두 하나에서 처리
* 마이크로서비스 아키텍처 : 개별 서버로 구성, 서로 통신


## REST API
* REST API : 정보를 주고 받음, HTTP 규칙 따름
  * HTTP : 정보를 주고 받을 때 지켜야 하는 통신 프로토콜 
  * 클라이언트 : 요청하는 플랫폼 Ex. 브라우저, 웹, 앱, python 등등
  * Resource : Unique한 id를 가지는 리소스, URI
  * Method : 서버 요청을 보내기 위한 방식 : GET, POST, PUT, PATCH, DELETE

## HTTP Method
* GET : 정보를 요청하기 위해 사용(Read)
* POST : 정보를 입력하기 위해 사용(Create)
* PUT : 정보를 업데이트하기 위해 사용(Update)
* PATCH : 정보를 업데이트하기 위해 사용(Update)
* DELETE : 정보를 삭제하기 위해 사용(Delete)

* URI vs URL
  * URL : 인터넷 상 자원의 위치
  * URI : 인터넷 상의 자원을 식별하기 위한 문자열 구성


* GET
  - 어떤 정보를 가져와서 조회하기 위해 사용되는 방식
  - URL에 변수(데이터)를 포함시켜 요청함
  - 데이터를 Header(헤더)에 포함하여 전송함
  - URL에 데이터가 노출되어 보안에 취약
  - 캐싱할 수 있음

* POST
  - 데이터를 서버로 제출해 추가 또는 수정하기 위해 사용하는 방식
  - URL에 변수(데이터)를 노출하지 않고 요청
  - 데이터를 Body(바디)에 포함
  - URL에 데이터가 노출되지 않아 기본 보안은 되어 있음
  - 캐싱할 수 없음(다만 그 안에 아키텍처로 캐싱할 수 있음)

![image](https://user-images.githubusercontent.com/63588046/169751035-a9857038-7af2-4f79-be60-d531aa77e72d.png)



## Header와 Body

- Http 통신은 Request 하고, Response를 받을 때 정보를 패킷(Packet)에 저장
- Packet 구조 : Header / Body
- Header : 보내는 주소, 받는 주소, 시간
- Body : 실제 전달하려는 내용


## Status Code
* 1xx(정보) : 요청을 받았고, 프로세스를 계속 진행함
* 2xx(성공) : 요청을 성공적으로 받았고, 실행함
* 3xx(리다이렉션) : 요청 완료를 위한 추가 작업이 필요
* 4xx(클라이언트 오류) : 요청 문법이 잘못되었거나 요청을 처리할 수 없음
* 5xx(서버 오류) 서버가 요청에 대해 실패함



## 동기와 비동기

- 동기(Sync) : 서버에서 요청을 보냈을 때, 응답이 돌아와야 다음 동작을 수행할 수 있음. A 작업이 모두 완료될 때까지 B 작업은 대기해야 함
- 비동기(Async) : 요청을 보낼 때 응답 상태와 상관없이 다음 동작을 수행함. A작업과 B 작업이 동시에 실행됨


## IP
- 네트워크에 연결된 특정 PC의 주소를 나타내는 체계
- Internet Protocol의 줄임말, 인터넷상에서 사용하는 주소체계
- 4덩이의 숫자로 구성된 IP 주소 체계를IPv4라고 함
- 각 덩어리마다 0~255로 나타낼 수 있음. 2^32 = 43억개의 IP 주소를 표현할 수 있음
- 몇가지는 용도가 정해짐
- localhost, 127.0.0.1 : 현재 사용 중인 Local PC
- 0.0.0.0, 255.255.255.255 : broadcast address, 로컬 네트워크에 접속된 모든 장치와 소통하는 주소
- 개인 PC 보급으로 누구나 PC를 사용해 IPv4로 할당할 수 있는 한계점 진입, IPv6이 나옴


## Port
- IP 주소 뒤에 나오는 숫자
- PC에 접속할 수 있는 통로(채널)
- 사용 중인 포트는 중복할 수 없음
- Jupyter Notebook은 8888
- Port는 0 ~ 65535까지 존재
- 그 중 0~1024는 통신을 위한 규약에 정해짐
- 22 : SSH
- 80 : HTTP
- 443 : HTTPS


# FastAPI

## FastAPI 소개 & 특징
* 간결한 문법
* Flask 비슷한 구조
* 성능도 좋음


## FastAPI vs Flask
* 간결한 문법, 비동기 지원
* 부족한 라이브러리



## Poetry
- Dependency Resolver로 복잡한 의존성들의 버전 충돌을 방지
- Virtualenv를 생성해서 격리된 환경에서 빠르게 개발이 가능해짐
- 기존 파이썬 패키지 관리 도구에서 지원하지 않는 Build, Publish가 가능
- pyproject.toml을 기준으로 여러 툴들의 config를 명시적으로 관리
- 새로 만든 프로젝트라면 poetry를 사용해보고, virtualenv 등과 비교하는 것을 추천


## Swagger

## Simple Web Server
