#!/bin/bash

python3 --version

# # 가상환경 비활성화
# deactivate
# rm -rf .venv

# 가상환경 설정 및 활성화
python3 -m venv .venv && source ./.venv/bin/activate

# 라이브러리 설치
pip install pytest black flake8
pip install dotenv
pip install loguru

# mkdir src/
# touch src/main.py src/__init__.py
# mkdir tests/
# touch tests/test_main.py tests/__init__.py
# touch .gitignore .env README.md
# touch requirements.txt
