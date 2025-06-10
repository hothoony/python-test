### 가상환경 활성화
```shell
# Linux/macOS
source .venv/bin/activate
```

### 테스트 의존성 설치
```shell
pip install -r requirements-dev.txt
```

### 개발 모드로 패키지 설치
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

# 특정 패키지만 실행
pytest tests/boolean
pytest tests/my_package

# 커버리지 리포트 포함
pytest --cov=my_package

# 자세한 출력과 함께 테스트 실행
pytest -v
```
