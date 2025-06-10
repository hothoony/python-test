# Makefile for Python project

# Variables
PYTHON = python3
PIP = pip3
PYTEST = python -m pytest
PYTHONPATH = ${PWD}/src:${PYTHONPATH}
VENV = .venv
ACTIVATE = . $(VENV)/bin/activate
PYTHON = $(VENV)/bin/python3

# Default target
.DEFAULT_GOAL := help

# Help system
.PHONY: help
help:  ## Display this help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Development

.PHONY: setup
setup:  ## Set up development environment
	@echo "Setting up development environment..."
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"
	$(PIP) install pre-commit
	pre-commit install
	@echo "\nDevelopment environment setup complete.\nRun 'source $(VENV)/bin/activate' to activate the virtual environment."

.PHONY: install
install:  ## Install the package in development mode
	$(PIP) install -e .

.PHONY: install-dev
install-dev:  ## Install development dependencies
	$(PIP) install -e ".[dev]"

##@ Code Quality

.PHONY: format
format:  ## Format code with black and isort
	black src tests
	isort src tests

.PHONY: lint
lint:  ## Lint code with flake8
	flake8 src tests

.PHONY: typecheck
typecheck:  ## Check type hints with mypy
	mypy src tests

.PHONY: check
check: lint typecheck  ## Run all code quality checks

##@ Testing

.PHONY: test
	test:  ## Run tests
	$(PYTEST) tests/ -v --cov=src --cov-report=term-missing --cov-report=xml:coverage.xml

.PHONY: test-cov
	test-cov:  ## Run tests with coverage report
	$(PYTEST) tests/ -v --cov=src --cov-report=html

##@ Build & Release

.PHONY: build
build:  ## Build package
	$(PYTHON) -m build

.PHONY: clean
clean:  ## Clean up build artifacts
	rm -rf build/ dist/ .pytest_cache/ .mypy_cache/ .coverage htmlcov/ *.egg-info/ .eggs/ __pycache__/ **/__pycache__/ .ipynb_checkpoints/
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name "*.egg-info" -exec rm -r {} +

##@ Documentation

.PHONY: docs
	docs:  ## Build documentation
	$(MAKE) -C docs html

##@ Pre-commit

.PHONY: pre-commit-run
pre-commit-run:  ## Run pre-commit on all files
	pre-commit run --all-files

##@ Virtual Environment

.PHONY: venv
venv:  ## Create virtual environment
	$(PYTHON) -m venv $(VENV)

.PHONY: activate
activate:  ## Activate virtual environment
	@echo "Run 'source $(VENV)/bin/activate' to activate the virtual environment."

##@ Docker

.PHONY: docker-build
docker-build:  ## Build Docker image
	docker build -t python-project-template .

.PHONY: docker-run
docker-run:  ## Run Docker container
	docker run -it --rm -p 8000:8000 python-project-template
