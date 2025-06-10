#!/bin/bash

python3 --version

python3 -m venv .venv
source .venv/bin/activate

pip install pytest black flake8
pip install dotenv
pip install loguru
pip install sqlparse

pip list

# mkdir src/ tests/
# touch src/__init__.py tests/__init__.py
# touch src/main.py tests/test_main.py
# touch requirements.txt
# touch .gitignore .env README.md
