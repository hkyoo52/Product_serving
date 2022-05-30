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


## 저장된 데이터 활용 방식
# Logging in Python
## Python Logging Module
## Logger
## Handler
## Formatter
## Logging Flow
# Online Serving Logging(BigQuery)
## BigQuery 데이터 구조
## BigQuery 데이터세트 만들기
## BigQuery 테이블 만들기
## BigQuery로 실시간 로그 데이터 수집하기
