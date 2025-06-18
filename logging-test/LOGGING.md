# Python Logging 가이드

이 문서는 프로젝트의 로깅 시스템을 사용하는 방법에 대한 가이드입니다.

## 목차
1. [로깅 개요](#로깅-개요)
2. [로깅 레벨](#로깅-레벨)
3. [로거 사용법](#로거-사용법)
4. [고급 기능](#고급-기능)
5. [환경별 설정](#환경별-설정)
6. [성능 고려사항](#성능-고려사항)

## 로깅 개요

이 프로젝트는 Python의 표준 `logging` 모듈을 기반으로 한 고급 로깅 시스템을 사용합니다. 주요 기능은 다음과 같습니다:

- 환경별(개발/운영) 로깅 설정 자동화
- 민감 정보 자동 마스킹
- 로그 로테이션 및 압축
- JSON 포맷 로깅 (운영 환경)
- 구조화된 로깅 지원

## 로깅 레벨

로깅 레벨은 다음과 같이 사용합니다:

| 레벨    | 사용 시나리오 |
|---------|--------------|
| DEBUG   | 개발 중 디버깅 목적의 상세 정보 |
| INFO    | 일반적인 애플리케이션 이벤트 |
| WARNING | 예상치 못한 상황이나 복구 가능한 문제 |
| ERROR   | 특정 기능이 실패했지만 애플리케이션은 계속 실행 가능 |
| CRITICAL| 애플리케이션을 중단시킬 수 있는 심각한 오류 |

## 로거 사용법

### 기본 사용법

```python
import logging

# 모듈별 로거 생성
logger = logging.getLogger(__name__)


# 로그 메시지 기록
try:
    # 비즈니스 로직
    logger.debug("디버그 정보")
    logger.info("정보성 메시지")
    
    # 구조화된 로깅
    logger.info("사용자 로그인", extra={
        'data': {
            'user_id': 123,
            'ip': '192.168.1.1',
            'action': 'login'
        }
    })
    
except Exception as e:
    # 예외 로깅
    logger.error("작업 실패", exc_info=True, extra={
        'data': {
            'error': str(e),
            'context': 'user_login'
        }
    })
    raise
```

### 권장 로깅 패턴

1. **컨텍스트 제공**:
   ```python
   # 나쁜 예
   logger.error("파일을 찾을 수 없음")
   
   # 좋은 예
   logger.error("구성 파일을 찾을 수 없음", extra={
       'data': {
           'file_path': '/path/to/config.yaml',
           'context': 'load_config'
       }
   })
   ```

2. **예외 로깅**:
   ```python
   try:
       # 코드
   except ValueError as e:
       logger.error("유효하지 않은 값", exc_info=True, extra={
           'data': {
               'error': str(e),
               'input_value': value
           }
       })
       raise
   ```

3. **성능 측정**:
   ```python
   import time
   from contextlib import contextmanager
   
   @contextmanager
   def timer(name):
       start_time = time.time()
       try:
           yield
       finally:
           elapsed = (time.time() - start_time) * 1000  # 밀리초 단위
           logger.info("작업 완료", extra={
               'data': {
                   'operation': name,
                   'duration_ms': elapsed
               }
           })
   
   # 사용 예
   with timer("데이터베이스 쿼리"):
       # 데이터베이스 작업
       pass
   ```

## 고급 기능

### 1. 구조화된 로깅

`extra` 파라미터를 사용하여 구조화된 데이터를 로그에 포함시킬 수 있습니다.

```python
logger.info("결제 처리 완료", extra={
    'data': {
        'transaction_id': 'tx_12345',
        'amount': 10000,
        'currency': 'KRW',
        'user_id': 42,
        'status': 'completed'
    }
})
```

### 2. 민감 정보 마스킹

다음과 같은 필드 이름은 자동으로 마스킹됩니다:
- password, secret, api_key, token, access_key 등

```python
# 다음과 같이 로깅하면
logger.info("데이터베이스 연결", extra={
    'data': {
        'db_host': 'localhost',
        'db_user': 'admin',
        'db_password': 's3cr3t'  # 자동으로 마스킹됨
    }
})

# 로그 출력 예:
# {"timestamp": "...", "level": "INFO", "message": "데이터베이스 연결", "data": {"db_host": "localhost", "db_user": "admin", "db_password": "***MASKED***"}}
```

### 3. 컨텍스트 관리

`LoggerAdapter`를 사용하여 로그 레코드에 컨텍스트를 추가할 수 있습니다.

```python
import logging
from functools import partial

# 컨텍스트 관리자
class RequestContext:
    def __init__(self, logger, context):
        self.logger = logger
        self.context = context
    
    def __enter__(self):
        self.old_makeRecord = self.logger.makeRecord
        def makeRecord(name, level, fn, lno, msg, args, exc_info, func=None, extra=None, **kwargs):
            if extra is None:
                extra = {}
            extra.update(self.context)
            return self.old_makeRecord(name, level, fn, lno, msg, args, exc_info, func, extra, **kwargs)
        self.logger.makeRecord = makeRecord
        return self.logger
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.makeRecord = self.old_makeRecord

# 사용 예
logger = logging.getLogger(__name__)


with RequestContext(logger, {'request_id': 'req_123', 'user_id': 42}):
    logger.info("요청 처리 중")  # 자동으로 request_id와 user_id가 로그에 포함됨
```

## 환경별 설정

### 개발 환경
- 로그 레벨: DEBUG
- 포맷: 사람이 읽기 쉬운 텍스트
- 출력: 콘솔

### 운영 환경
- 로그 레벨: INFO (기본값)
- 포맷: JSON
- 출력: 파일 (10MB 단위 로테이션, 최대 5개 파일 보관)
- **일별 로테이션**: 매일 자정에 새로운 로그 파일 생성
- **보관 기간**: 최근 30일치 로그 파일 보관
- **파일명 형식**: `app.log.2023-06-18`과 같이 날짜가 자동으로 추가됨

### 환경 변수

| 변수명 | 기본값 | 설명 |
|--------|--------|------|
| `LOG_LEVEL` | `DEBUG` (개발), `INFO` (운영) | 로그 레벨 설정 |
| `LOG_DIR` | `./logs` | 로그 파일 저장 디렉토리 (자동 생성됨) |
| `ENABLE_FILE_LOGGING` | `true` | 파일 로깅 활성화 여부 |
| `SKIP_LOGGING_INIT` | `false` | 로깅 초기화 건너뛰기 |

## 성능 고려사항

1. **문자열 포맷팅**: f-string 대신 % 포맷팅이나 `logger`의 파라미터화된 메시지 사용
   ```python
   # 나쁜 예 (항상 문자열 연산 발생)
   logger.debug(f"User {user_id} did {action}")
   
   # 좋은 예 (로그 레벨이 DEBUG보다 낮을 때는 문자열 연산이 발생하지 않음)
   logger.debug("User %s did %s", user_id, action)
   ```

2. **비용이 많이 드는 연산**: 로그 레벨 체크 후에만 수행
   ```python
   if logger.isEnabledFor(logging.DEBUG):
       # 비용이 많이 드는 디버그 정보 생성
       debug_info = generate_expensive_debug_info()
       logger.debug("디버그 정보: %s", debug_info)
   ```

3. **예외 로깅**: `exc_info` 파라미터 사용
   ```python
   try:
       # 코드
   except Exception as e:
       logger.error("오류 발생", exc_info=True)  # 스택 트레이스 포함
   ```

## 문제 해결

### 로그가 보이지 않는 경우
1. 로그 레벨이 너무 높게 설정되어 있지 않은지 확인
2. 로거 계층 구조 확인 (부모 로거에서 핸들러가 비활성화되어 있을 수 있음)
3. `logging.basicConfig()`가 다른 곳에서 호출되지 않았는지 확인

### 로그 파일이 생성되지 않는 경우
1. `LOG_DIR` 디렉토리에 쓰기 권한이 있는지 확인
2. `ENABLE_FILE_LOGGING` 환경 변수가 `true`로 설정되어 있는지 확인

## 참고 자료

- [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
- [The Hitchhiker's Guide to Python - Logging](https://docs.python-guide.org/writing/logging/)
- [12 Factor Apps - Logs](https://12factor.net/logs)
