
### if else
```python
if a > b:
    print('a 가 더 크다')
elif a < b:
    print('b 가 더 크다')
else:
    print('a 와 b 는 같다')
```

### 주석
```python
# line comment

# multi line comment
# multi line comment
# multi line comment
```

### 변수 타입 확인
```python
print(type("abc"))      # <class 'str'>
print(type(123))        # <class 'int'>
print(type(True))       # <class 'bool'>
print(type(False))      # <class 'bool'>
print(type({}))         # <class 'dict'>
print(type([]))         # <class 'list'>
print(type([{}, {}]))   # <class 'list'>
```

### dictionary
```python
dict1 = {
    "first": "hue",
    "last": "jackman",
    "year": 2024,
}
```

### Type Hinting
```python
name: str = "paul"
age: int = 20
height: float = 3.2
isSuccess: bool = True

def sum(a: int, b:int) -> int:
    return a + b
```

### import
```python
from common.util1 import *
from common.util2 import minus
```

### 문자열과 변수를 같이 출력
```python
print(f"sum = {sum(5, 3)}")
```
