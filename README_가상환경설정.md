### 작업 폴더 만들기
```shell
mkdir mybatis-xml-ddl-generate
cd mybatis-xml-ddl-generate
```

### 파이썬 설치 
```shell
python3 --version
```

### 가상환경 생성 및 활성화
```shell
python3 -m venv .venv
source .venv/bin/activate
```

### pip 업그레이드 (선택사항)
```shell
pip install --upgrade pip
```

### 라이브러리 설치 (pip 는 가상환경이 활성화된 경우 해당 환경에 설치됨)
```shell
pip install sqlparse
```

### 라이브러리 설치 확인
```shell
pip list
```

### 의존성 파일 생성
```shell
pip freeze > requirements.txt
```

### python 스크립트 만들기
```shell
touch mybatis_xml_ddl_generate.py
```

### python 스크립트 실행
```shell
python3 mybatis_xml_ddl_generate.py
```

### 가상환경 비활성화
```shell
deactivate
```
