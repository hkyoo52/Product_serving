# Linux
## Linux
* 서버에서 사용하는 OS

## Linux 알아야 할 이유
* MAC, Window를 서버로 사용하면 유료 (Linux는 무료)
* 안정성, 신뢰성
* 쉘 커맨드, 쉘 스크림트

## CLI, GUI
* CLI : 터미널
* GUI : 데스크탑

## 대표적인 Linux 배포판
* Debian 
* Ubuntu
* Prdhat
* CentOS


## Linux, Shell Script 학습 가이드
* 자주 사용하는 쉘 커맨드, 쉘 스크립트 위주 학습
* 필요한 코드가 있는 경우 검색해서 찾기
* 해당 코드에서 나오는 새로운 커맨드 학습
* 왜 이렇게 되는가? 생각하며 배경지식 필요한 경우 Linux, OS 학습


# Shell Command

## 쉘의 종류
* 쉘 : 사용자가 문자를 입력해 컴퓨터에 명령할 수 있도록 하는 프로그램
* 터미널/콘솔 : 쉘을 실행하기 위해 문자 입력을 받아 컴퓨터에 전달, 프로그램 출력을 화면에 작성
* sh : 최초의 쉘
* bash : Linux 표준 쉘
* zsh : Mac, OS 기본 쉘


## 쉘을 사용하는 경우
* 서버에서 접속해서 사용
* Linux의 내장 기능 활용
* 데이터 전처리
* Docker 사용
* Jupyter Notebook의 Cell 앞에 ! 붙이면 쉘 커맨드 사용됨
* 터미널에서 python3, jupyternotebook 사용
* Test Code 실행
* 배포 파이프라인 실행


## 기본 쉘 커맨드
```python
man python           # 기본적인 설명 나옴   q 쓰면 나옴
mkdir '폴더 이름'     # 폴더 생성
ls                   # 들어있는 폴더 확인
pwd                  # 현재 경로를 절대 경로로 보여줌
cd                   # 폴더 이동
echo                 # 터미널에 텍스트 출력
cp                   # 파일이나 폴더 복사
mv                   # 파일이나 폴더 이동
cat                  # 특정 파일 내용 출력
clear                # command 창 깨끗하게 해줌
history              # 지금까지 첬던 명령어 실행
export               # export water = "물" , 커미널 끄면 변수 사라짐, 환경변수에 저장하고 싶으면 bashrc에 저장
alias                # 기본 명령어를 간단히 줄임  -> alias ll2 = 'ls-l' 하면 ll2입력시 ls-l로 작동됨

head -n 3 vi-test.sh # test.sh에 앞에 3줄 출력
sort                 # 정렬 (sort -r : 내림차순)
uniq                 # 중복된 행이 연속으로 있는경우 제거 (cat fruits.txt | uniq)
grep                 # -i : 대소문자 구분 없이 찾기, -w : 정확히 그 단어만 찾기, -v : 특정 패턴 제외한 결과 출력, -E : 정규 표현식 사용 
(대표적인 정규 표현식 : ^단어 : 단어로 시작하는 것 찾기, 단어$ : 단어로 끝나는 것 찾기, .: 하나의 문자 매칭
cut                  # 파일에서 특정 필드 추출
> : 덮어쓰기
>> : 맨 아래에 추가히기


# 파일 생성
vi vi-test.sh        # 파일 생성 (test.sh 파일 생성)
i                    # insert 모드 변경
echo 'hi'            # hi라고 문서에 쓰기
esc
:wq                  # 저장하고 나가기

# 쉘 스크립트 실행
bash vi-test.sh

# 관리자권한 실행
sudo



```



## Redirect & Pipe

####특정 단어 찾기
```python
ls | grep "vi"  : "vi"가 들어있는 폴더 찾기
grep "vi" : 특정 단어 찾기
ls | grep "vi" > output.txt : 결과를 output.txt에 저장
history | grep "echo" : 최근 입력한 커맨드 중에서 echo가 들어간 명령어 찾기
```

## 서버에서 자주 사용하는 쉘 커맨드 -curl
* request 테스트할 수 있는 명령어
* curl -X localhost:5000/ {data}
* curl 외에 httpie 등도 있음(더 가독성 있게 출력)
* df : 현재 사용중인 디스크 용량 (df-h : 사람이 읽기 쉬운 형태로 출력)
* scp : ssh를 이용해 네트워크로 연결된 호스트 간 파일을 주고 받는 명령어 (-r : 재귀적 복사, -P : ssh 포트 지정, -i : SSH 설정을 활용해 실행)
* nohup : 터미널 종료 후에도 계속 작업 유지하도록 실행
* chmod : 파일 권한 변경


## 쉘 스크립트
* .sh 파일 생성, 그 안에 쉘 커맨드 추가
* 파이썬처럼 if, while, case 문이 존재, 작성시 bash name.sh로 실행 가능
