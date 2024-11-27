# Simple FastAPI REST API

## 설치 방법

1. 가상환경 생성 및 활성화
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
```

2. 패키지 설치
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
```bash
pip install fastapi
pip install uvicorn
pip install pydantic
```
```bash
pip uninstall fastapi
```
```bash
pip list
```

## 서버 실행 방법

```bash
uvicorn app.main:app --reload
```

## API 엔드포인트

- `GET /` : 환영 메시지 반환
- `POST /items` : 새 아이템 생성
- `GET /items` : 모든 아이템 조회
- `GET /items/{item_id}` : 특정 아이템 조회
- `PUT /items/{item_id}` : 특정 아이템 수정
- `DELETE /items/{item_id}` : 특정 아이템 삭제

```bash
curl -X GET -i http://127.0.0.1:8000
curl -X POST -i http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"name": "Foo"}'
curl -X GET -i http://127.0.0.1:8000/items
curl -X GET -i http://127.0.0.1:8000/items/1
curl -X PUT -i http://127.0.0.1:8000/items/1 -H "Content-Type: application/json" -d '{"name": "Bar"}'
curl -X DELETE -i http://127.0.0.1:8000/items/1
```
