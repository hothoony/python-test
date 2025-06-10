# 변수 정의
PYTHON := python3
VENV := .venv
PIP := $(VENV)/bin/pip

# 타겟 정의
.PHONY: vars
vars: 
	@echo $(PYTHON)
	@echo $(VENV)
	@echo $(PIP)

# 타겟 정의
.PHONY: all
all: install venv test

# 타겟 정의
.PHONY: all2
all2: test venv install

# 타겟 정의
.PHONY: setup
setup: install venv

# 타겟 정의
.PHONY: install
install:
	@echo "install begin"
	@echo "install end"

# 타겟 정의
.PHONY: venv
venv: install
	@echo "venv begin"
	@echo "venv end"

# 타겟 정의
.PHONY: test
test: 
	@echo "test begin"
	@echo "test end"

# 타겟 정의
.PHONY: lint
lint: 
	@echo "lint begin"
	@echo "lint end"

# 타겟 정의
.PHONY: format
format: 
	@echo "format begin"
	@echo "format end"

# 타겟 정의 (@이 없으면 명령어가 출력된다)
.PHONY: run-script
run-script:
	echo "run-script begin"
	hostname
	date
	echo "run-script end"

# 타겟 정의 (@이 있으면 명령어가 출력되지 않는다)
.PHONY: run-script2
run-script2:
	@echo "run-script2 begin"
	@hostname
	@date
	@echo "run-script2 end"
