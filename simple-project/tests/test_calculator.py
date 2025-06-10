"""
계산기 모듈 테스트
"""
import pytest
from my_package.calculator import add, subtract, multiply, divide


def test_add():
    """덧셈 테스트"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """뺄셈 테스트"""
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0


def test_multiply():
    """곱셈 테스트"""
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0


def test_divide():
    """나눗셈 테스트"""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(0, 1) == 0


def test_divide_by_zero():
    """0으로 나누기 예외 테스트"""
    with pytest.raises(ValueError):
        divide(1, 0)
