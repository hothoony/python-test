## 맥 & 파이썬 개발환경 셋팅

### python3 설치
```bash
brew install python3
```

### vscode 플러그인 설치
```bash
Python
```

### pip 로 패키지 설치시 오류
```bash
$ pip install <패키지>
zsh: command not found: pip 
```

### 패키지 설치 방법 여러가지
```bash
pip3 install --upgrade pip

pip3 install <패키지>

pip3 --user install <패키지>

sudo python3 -m pip install <패키지>
```

### pip 버전 업그레이드
```bash
python3 -m pip install --upgrade pip
```

### 패키지 설치
```bash
# 패키지 설치 경로
# /Users/<USER_ID>/Library/Python/3.9/lib/python/site-packages

pip3 list
pip3 install pycryptodome
pip3 uninstall pycryptodome
```

## 파이썬 실행경로 확인
```python
import sys
print("sys.executable = " + sys.executable)
# sys.executable = /opt/homebrew/opt/python@3.12/bin/python3.12
# /Users/hothoony/Library/Python/3.9/lib/python/site-packages
```

## 모듈 로드되는지 확인
```bash
# OK
python3 -c "from Crypto.Cipher import AES; print('OK')"
/usr/bin/python3 -c "from Crypto.Cipher import AES; print('OK')"

# not OK
/opt/homebrew/bin/python3 -c "from Crypto.Cipher import AES; print('OK')"
```

### Homebrew Python 환경에 pycryptodome 을 설치
```bash
/opt/homebrew/bin/python3 -m pip list
/opt/homebrew/bin/python3 -m pip install pycryptodome
/opt/homebrew/bin/python3 -m pip uninstall pycryptodome
```

### 가상 환경 사용

```bash
# 가상 환경 생성
python3 -m venv aes256/myenv
python3 -m venv .venv

# 가상 환경 활성화
source aes256/myenv/bin/activate
source .venv
```

- ### 가상 환경에서 패키지 모듈 설치
  - 터미널 프롬프트 앞에 가상환경 이름이 표시된다 (.venv)
```bash
(.venv) ~$ python3 -m pip install pycryptodome
```
