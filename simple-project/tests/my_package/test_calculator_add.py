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
