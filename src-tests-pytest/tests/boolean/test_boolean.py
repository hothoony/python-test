"""
불린 모듈 테스트
"""
import pytest


def test_boolean():
    """불린 테스트"""
    assert True is True
    assert False is False
    assert True is not False
    assert False is not True
