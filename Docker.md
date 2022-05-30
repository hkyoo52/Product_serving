## 가상화란
* Local 환경과 서버 환경이 다를 수 있음
* 서버가 많으면 한개 서버에서 업데이트 할 경우 나머지도 업데이트 필요

## Docker
#### Docker Image
* 컨테이너 실행할 때 사용할 수 있는 "템플릿"
* Only Reald

### Docker Container
* Docker Image를 활용해 실행된 인스턴스
* Write 가능
안

## Docker 용어
```python
docker pull mysql:8 : mysql:8이라는 이미지 다운해라
docker images : 다운 받은 이미지 확인
docker run --name mysql-tutorial -e MYSQL_ROOT_PASSWORD=1234 -d -p 3306:3306 mysql:8 : 이름 : mysql-tutorial, 비밀번호:1234, -d : 백그라운드 모드(docker 꺼도 작동 됨), -p : 포트 번호
docker ps : mysql 실행
docker ps -a : 실행 멈춘 컨테이너
docker exec -it "컨테이너 이름" /bin/bash : 컨테이너에 들어감 -> 잘 실행하고 있는지 확인 가능
mysql -u root -p : mysql 쉘 화면 보임
docker stop "컨테이너 이름" : 실행중인 
docker rm "컨테이너 이름" : 멈춘 컨테이너 삭제



```
