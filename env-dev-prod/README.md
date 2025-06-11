## python 프로젝트 템플릿

## 가상환경 초기화
```shell
deactivate
rm -rf .venv
```

## 프로젝트 초기화
```shell
setup_python.sh
source ./.venv/bin/activate
```

### 설치된 패키지 목록 확인하기
```shell
pip list
```

### 프로젝트 실행하기
```shell
ENV=dev python3 src/my_app/main.py     # 개발 환경 실행
ENV=prod python3 src/my_app/main.py    # 운영 환경 실행
```

### 테스트 실행하기
```shell
pytest
pytest -v
pytest -vs
```
