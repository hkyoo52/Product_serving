# Logging Basics
## 로그란?
* 컴퓨터에 접속한 기록, 특정 행동을 한 경우 남는 것 

## 데이터의 종류
* 데이터베이스 데이터
* 사용자 행동 데이터 - 무엇을 클릭하고 등등
* 인프라 데이터(Metric) - 백엔드 잘 작동하는지, Request 수, Response 수, DB 부하


## 데이터 적재 방식
* RDB(SQL) 저장 - 웹,앱 서비스 사용
  - 관계형 데이터베이스
  - 행/열 이루어짐
  - 비지니스 연관된 중요한 정보
  - 영구적으로 저장해야하는 경우
* DB(NoSQL) 저장 : Elasticsearch, Logstash, Fluent 활용하려고
  - 읽기 쓰기가 빠름
  - key-value 구조
* Object Storage 저장 : Cloud, csv, json 저장 -> 별도에 Data Warehouse에 옮겨야함
* Data Warehouse 저장 : 데이터 분석시 활용하는 곳임
  - 여러 공간에 저장된 데이터 한곳으로 저장

# Logging in Python
## Python Logging Module
#### Log level
![image](https://user-images.githubusercontent.com/63588046/171140418-bc2b5087-7ae3-4b58-8a1e-decfbe2a9fa2.png)

#### print vs logging
* print문은 console에서만 출력
* logging은 파이썬이 다룰 수 있는 모든 포맷에 output 출력
* logging은 반드시 config 설정해야함

```python
import logging.config

# config 설정
logger_config = {
        'version':1,
        'disable_existing_loggers':True,
        'formatters':{
            'simple': {'format':'% ~ ~ '},
         'handlers': {~ ~ ~},                # 여기까지 기본 config
         
         'loggers':{'example':{                  # logger 이름
                        'level':'INFO",          # logger level
                        'handlers':['console']   
                   }
            }
}
         
                

logger = logging.getLogger("example")
logger.info('hello world')

```

## Logger
- 로그를 생성하는 Method 제공(logger.info() 등)
- 로그 Level과 Logger에 적용된 Filter를 기반으로 처리해야 하는 로그인지 판단
- Handler에게 LogRecord 인스턴스 전달

## Handler
- Logger에서 만들어진 Log를 적절한 위치로 전송(파일 저장 또는 Console 출력 등)
- Level과 Formatter를 각각 설정해서 필터링 할 수 있음
- StreamHandler, FileHandler, HTTPHandler 등

## Formatter
- 최종적으로 Log에 출력될 Formatting 설정
- 시간, Logger 이름, 심각도, Output, 함수 이름, Line 정보, 메시지 등 다양한 정보 제공

## Logging Flow
![image](https://user-images.githubusercontent.com/63588046/171143781-b0279077-9956-4335-a950-07c24895b583.png)


# Online Serving Logging(BigQuery)

## BigQuery 데이터 구조
## BigQuery 데이터세트 만들기
## BigQuery 테이블 만들기
## BigQuery로 실시간 로그 데이터 수집하기
