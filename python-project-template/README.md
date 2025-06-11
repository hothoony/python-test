## python 프로젝트 템플릿

## 가상환경 초기화
```shell
deactivate
rm -rf .venv
```

## 프로젝트 초기화
```shell
setup_python.sh
source .venv/bin/activate
```

### 설치된 패키지 목록 확인하기
```shell
pip list
```

### 프로젝트 실행하기
```shell
python3 src/my_app/main.py
```

### 테스트 실행하기
```shell
pytest
pytest -v
pytest -vs
pytest -vs tests/test_main.py::test_method01
pytest -vs tests/test_main.py::test_method02
```
