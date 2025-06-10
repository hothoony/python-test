"""
계산기 모듈 테스트
"""
import pytest
from my_package.calculator import divide


def test_divide_by_zero():
    """0으로 나누기 예외 테스트"""
    with pytest.raises(ValueError):
        divide(1, 0)
