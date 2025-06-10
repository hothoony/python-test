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

# 커버리지 리포트 포함
pytest --cov=my_package

# 자세한 출력과 함께 테스트 실행
pytest -v
```
