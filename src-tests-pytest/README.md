## 개요
- 운영 소스코드를 `src/` 에 위치
- 테스트 코드를 `tests/` 에 위치
- `pytest` 로 테스트 실행

### 가상환경 활성화
```shell
source .venv/bin/activate
```

### 테스트 의존성 설치
```shell
pip install -r requirements-dev.txt
```

### 개발 모드로 패키지 설치 (pytest 실행을 위해 필요)
```shell
pip install -e .
```

### 테스트 실행
```shell
# 모든 테스트 실행
pytest

# 특정 테스트 파일만 실행
pytest tests/boolean/test_boolean.py
pytest tests/boolean/test_boolean_fail.py
pytest tests/my_package/test_calculator_add.py
pytest tests/my_package/test_calculator.py
pytest tests/my_package/test_calculator_error.py

# 특정 패키지만 실행
pytest tests/boolean
pytest tests/my_package

# 테스트 파일 중 특정 함수만 실행
pytest -v tests/boolean/test_try_catch.py::test_try
pytest -v tests/boolean/test_try_catch.py::test_try2

# 커버리지 리포트 포함
pytest --cov=my_package

# 자세한 출력과 함께 테스트 실행
pytest -v
```

## 테스트 실행 -v 옵션
- `-v` 옵션 사용시
```shell
# pytest -v tests/boolean/test_try_catch.py
tests/boolean/test_try_catch.py::test_try PASSED
tests/boolean/test_try_catch.py::test_try2 PASSED
```
- `-v` 옵션 미사용시
```shell
# pytest tests/boolean/test_try_catch.py
tests/boolean/test_try_catch.py ..
```
