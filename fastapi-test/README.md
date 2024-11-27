# Simple FastAPI REST API

## 설치 방법

1. 가상환경 생성 및 활성화
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
```

2. 패키지 설치
```bash
pip install -r requirements.txt
```

## 서버 실행 방법

```bash
uvicorn main:app --reload
```

## API 엔드포인트

- `GET /` : 환영 메시지 반환
- `POST /items` : 새 아이템 생성
- `GET /items` : 모든 아이템 조회
- `GET /items/{item_id}` : 특정 아이템 조회
- `PUT /items/{item_id}` : 특정 아이템 수정
- `DELETE /items/{item_id}` : 특정 아이템 삭제
