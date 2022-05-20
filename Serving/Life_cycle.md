# 머신러닝 프로젝트 Flow

## 문제 정의의 중요성
* 특정 현상 파악 => 그 현상의 있는 문제를 정의
* 문제를 명확하게 정의해야 한다
* 현상 파악 -> 문제 정의 -> 프로젝트 설계 -> Action -> 추가 원인 분석


## 현상 파악

#### 현상 파악
* 어떤 일이 발생
* 어려움은 무엇인가
* 해당 일을 해결하면 좋은 것은 무엇인가
* 어떤 가설을 만들어 볼 수 있을까
* 어떤 데이터가 있을까

#### 구체적 문제 정의
* 무엇을 해결하고 싶은가
* 무엇을 알고 싶은가


## 프로젝트 설계

#### 프로젝트 설계
* 문제 정의 & 머신러닝 문제 타당성 확인
* 최적화할 Metric 설계, 목표 설정
* 제약 조건
* 데이터 수집, 레이블 확인
* 모델 개발
* 모델 예측 결과를 토대로 Error Analysis. 잘못된 라벨이 왜 생기는지 확인
* 다시 모델 학습, 많은 데이터 수집 등등

#### 머신러닝 타당성
* 패턴이 있고 복잡해야함
* 목적함수를 만들 수 있어야함 -> 노이즈를 패턴으로 학습하는 경우 존재, 지도 학습같은 경우 정답과 예측의 차이 정의 필요
* 데이터가 존재하거나 수집할 수 있어야함
* 사람이 반복적으로 실행해야함

#### 제약조건
* 일정, 예산, 관련된 사람
* 윤리적 이슈
* 기술적 제약 (인프라가 머신러닝 적용할 때 큰 제약일 수 있음)
* 성능 
  - Baseline : 새로 만든 모델을 무엇과 비교할 것인가 (기존 성능 or 간단한 회귀)
  - threshold : 확률값 몇 이상을 정답이라 할지
  - performance : 정확도 vs 속도
  - 해석 가능 여부 : 결과가 왜 발생했는지 해석할 필요가 있을까?
  - confidence measurement : False Negative가 있어도 괜찮은지? 오탐이 있으면 안되는지?

#### 베이스라인, 프로토타입
* 모델의 성능이 좋아졌다고 판단할 수 있는 Baseline이 필요
* 간단한 모델부터 시작
    - 최악의 성능을 가진 허수아비 보델로 시작
    - 초기에는 단순하게 사용자가 이전에 선택한 행동 제안할 수 있고 추천시스템에서 가장 많이 구매한것 추천할 수 있음
    - 유사한 문제를 해결하고 있는 SOTA 논문 파악


#### Metric Evaluation
* 앞에서 objective를 구해서 모델의 성능지표 확인
* 어떤 지표가 좋아질까 고민
* 작게는 RMSE, 크게는 비지니스 지표 (고객의 재방문율)
* 지표를 잘 정의해야 기존에 비해서 더 성과를 냈는지 파악 가능
* 개발 및 배포 중에 시스템의 성능은 어떻게 판단할까?
* 정답 레이블이 필요한 경우 사용자 반응에서 어떻게 레이블 추론할까?
* 모델 성능을 비지니스 Goal과 Objective를 어떻게 연결할까? 

#### Action
## 지표 결정

## Action(모델 개발 후 배포 & 모니터링)

## 추가 원인 분석



# 비지니스 모델

## 비지니스 모델 파악하기