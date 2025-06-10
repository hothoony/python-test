#!/bin/bash

python3 --version

# # 가상환경 비활성화
# deactivate
# rm -rf .venv

# 가상환경 생성
python3 -m venv .venv
# 가상환경 활성화
source ./.venv/bin/activate

# 라이브러리 설치
pip install pytest black flake8 mypy
pip install python-dotenv
pip install loguru

# 현재 디렉토리의 패키지를 개발 모드로 설치
# 디렉토리 안에 setup.py 또는 pyproject.toml이 있어야 함
# pytest 로 테스트를 실행하기 위해 필요
pip install -e .

# 설치된 라이브러리 확인
pip list

# mkdir src/
# touch src/main.py src/__init__.py
# mkdir tests/
# touch tests/test_main.py tests/__init__.py
# touch .gitignore .env README.md
# touch requirements.txt
