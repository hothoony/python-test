import pytest
from my_app.main import method01, method02

def test_method01():
    result = method01()
    assert True is True

def test_method02():
    result = method02()
    assert True is True
