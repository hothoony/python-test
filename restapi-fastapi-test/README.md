# Simple FastAPI REST API

## 설치 방법

1. 가상환경 생성 및 활성화
```bash
python3 -m venv .venv

# 가상환경 활성화
source .venv/bin/activate
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

### Items API
- `GET /` : 환영 메시지 반환

### Items API
```bash
curl -X GET -i http://127.0.0.1:8000
curl -X POST -i http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"name": "Foo"}'
curl -X GET -i http://127.0.0.1:8000/items
curl -X GET -i http://127.0.0.1:8000/items/1
curl -X PUT -i http://127.0.0.1:8000/items/1 -H "Content-Type: application/json" -d '{"name": "Bar"}'
curl -X DELETE -i http://127.0.0.1:8000/items/1
```

### QnA API
- `POST /qna/questions` : 새 질문 생성
- `GET /qna/questions` : 모든 질문 조회
- `GET /qna/questions/{question_id}` : 특정 질문 조회
- `PUT /qna/questions/{question_id}` : 특정 질문 수정
- `DELETE /qna/questions/{question_id}` : 특정 질문 삭제
- `POST /qna/questions/{question_id}/answers` : 질문에 새 답변 생성
- `GET /qna/questions/{question_id}/answers` : 질문의 모든 답변 조회
- `GET /qna/answers/{answer_id}` : 특정 답변 조회
- `PUT /qna/answers/{answer_id}` : 특정 답변 수정
- `DELETE /qna/answers/{answer_id}` : 특정 답변 삭제


