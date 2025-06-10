"""
불린 모듈 테스트
"""
import pytest


def test_try():
    try:
        print('try')
    except:
        print('except')
    finally:
        print('finally')
    assert True is True

def test_try2():
    try:
        print('try')
    except:
        print('except')
    finally:
        print('finally')
    assert True is True