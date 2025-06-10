# 변수 정의
PYTHON := python3
VENV := .venv
PIP := $(VENV)/bin/pip
PYTEST := $(VENV)/bin/pytest
BLACK := $(VENV)/bin/black
FLAKE8 := $(VENV)/bin/flake8

# 기본 타겟
.PHONY: all
all: install format lint test
	@echo "All tasks completed!"

# 가상환경 생성
.PHONY: venv
venv:
	@echo "Creating virtual environment..."
	@$(PYTHON) -m venv $(VENV)
	# @source ./$(VENV)/bin/activate
	@echo "Virtual environment created!"

# 의존성 설치
.PHONY: install
install: venv
	@echo "Installing dependencies..."
	@$(PIP) install --upgrade pip
	@$(PIP) install pytest black flake8
	# @$(PIP) install -r requirements.txt
	@echo "Dependencies installed!"

# 코드 포맷팅
.PHONY: format
format: install
	@echo "Formatting code..."
	@$(BLACK) src/ tests/
	@echo "Formatting completed!"

# 린팅
.PHONY: lint
lint: install
	@echo "Linting code..."
	@$(FLAKE8) src/ tests/
	@echo "Linting completed!"

# 테스트 실행
.PHONY: test
test: install
	@echo "Running tests..."
	@$(PYTEST) tests/
	@echo "Tests completed!"

# 정리
.PHONY: clean
clean:
	@echo "Cleaning up..."
	@rm -rf $(VENV)
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "Cleanup completed!"

.PHONY: setup
setup: 
	@mkdir -p src tests
	@touch src/__init__.py tests/__init__.py
	@touch src/main.py tests/test_main.py
	@touch .gitignore .env
	@touch README.md
	@echo "Setup completed!"
