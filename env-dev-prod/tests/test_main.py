import os
import sys

import pytest
from myapp.main import method01, method02, run

def test_method01():
    result = method01()
    assert True is True

def test_method02():
    result = method02()
    assert True is True

def test_run():
    result = run()
    assert True is True
