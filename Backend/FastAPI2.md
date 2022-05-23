# FastAPI 기본 지식
## Path Parameter
* 웹에서 GET Method 사용해 데이터를 전송할 수 있음
* 경로에 존재하지 않을 경우 404 Erro 발생
* Ex. ID가 402인 사용자 정보를 가져오고 싶은 경우 방식 -> /users?id=402

## Query Parameter
* API 뒤에 입력 데이터를 함께 제공하는 방식으로 사용
* Query String은 Key, Value의 쌍으로 이루어지며 &로 연결해 여러 데이터를 넘길 수 있음
* 데이터가 없는 경우 빈 리스트 나옴 -> 추가로 후처리 필요
* Ex. https://~~~~~~~~~ ?where=nex~~~~~ =광진구


## Optional Parameter

## Request Body

- 클라이언트에서 API에 데이터를 보낼 때, Request Body를 사용함
- 클라이언트 => API : Request Body
- API의 Response => 클라이언트 : Response Body
- Request Body에 데이터가 항상 포함되어야 하는 것은 아님
- Request Body에 데이터를 보내고 싶다면 POST Method를 사용
- (참고) GET Method는 URL, Request Header로 데이터 전달

## Response Body

## Form, File


# Pydantic
## Pydantic

## Pydantic Validation

## Pydantic Config
