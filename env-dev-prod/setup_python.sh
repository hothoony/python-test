#!/bin/bash

python3 --version

# # 가상환경 비활성화
# deactivate
# rm -rf .venv

# 가상환경 생성
python3 -m venv .venv
# 가상환경 활성화
source .venv/bin/activate

# PYTHONPATH 설정
# export PYTHONPATH=$PYTHONPATH:$(pwd)

# python3가 사용하는 pip 패키지의 버전을 최신 버전으로 업그레이드
# python3 -m pip install --upgrade pip

# 패키지 설치
python3 -m pip install pytest black flake8 mypy
python3 -m pip install python-dotenv
python3 -m pip install loguru

# 현재 디렉토리의 패키지를 개발 모드로 설치
# 디렉토리 안에 setup.py 또는 pyproject.toml이 있어야 함
# pytest 로 테스트를 실행하기 위해 필요
python3 -m pip install -e .

# 설치된 패키지 확인
python3 -m pip list

# 테스트 실행
# pytest
# pytest -v
# pytest -vs
