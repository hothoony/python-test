# Simple FastAPI REST API

간단한 FastAPI를 이용한 REST API 프로젝트입니다.

## 설치 방법

1. 가상환경 생성 및 활성화
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
```

2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

## 실행 방법

다음 명령어로 서버를 실행합니다:
```bash
uvicorn main:app --reload
```

서버가 실행되면 다음 URL에서 API를 테스트할 수 있습니다:
- API 문서: http://localhost:8000/docs
- 대체 API 문서: http://localhost:8000/redoc

## API 엔드포인트

- GET /: 환영 메시지 반환
- GET /items: 모든 아이템 조회
- GET /items/{item_id}: 특정 아이템 조회
- POST /items: 새 아이템 생성
- PUT /items/{item_id}: 특정 아이템 수정
- DELETE /items/{item_id}: 특정 아이템 삭제
