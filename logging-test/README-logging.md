## 1. 표준 logging 모듈 사용
```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
```

## 2. 환경별 로깅 설정 분리
- `logging_config.py`
```python
import logging.config

def setup_logging(env="production"):
    if env == "development":
        config = {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "level": "DEBUG",
                },
            },
            "root": {
                "handlers": ["console"],
                "level": "DEBUG",
            },
        }
    else:
        config = {
            "version": 1,
            "formatters": {
                "json": {
                    "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                    "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
                }
            },
            "handlers": {
                "file": {
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "filename": "/var/log/myapp/app.log",
                    "when": "midnight",
                    "backupCount": 14,
                    "formatter": "json",
                }
            },
            "root": {
                "handlers": ["file"],
                "level": "INFO",
            },
        }

    logging.config.dictConfig(config)
```

## 3. 애플리케이션 전역에서 로거 사용
```python
import logging

logger = logging.getLogger(__name__)
```

## 4. 구조화 로깅
```python
logger.info("User login", extra={"user_id": 123, "ip": "127.0.0.1"})
```

## 5. 예외 로깅은 exc_info 포함
```python
try:
    risky_operation()
except Exception as e:
    logger.error("Unhandled exception occured", exc_info=True)
```

## 6. 의미 있는 로그 수준 구분
```python
DEBUG, INFO, WARNING, ERROR, CRITICAL
```

## 7. 민감 정보 제외
```python
def mask_sensitive_data(data):
    if 'password' in record.msg:
        record.msg = record.msg.replace('password', '******')
    return True
```

## 8. Request/Response 트레이싱
```python
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}")
        return response
```

## 9. 운영환경 로그 수집 연동
```python
; Elasticsearch, Logstash, Kibana
; JSON 포멧 구조화
```

## 10. 테스트 코드에서 로거 캡처 설정
```python
def test_example(caplog):
    with caplog.at_level(logging.INFO):
        my_function()
        assert "expected messgae" in caplog.text
```
