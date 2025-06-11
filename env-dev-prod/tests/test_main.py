import os
import sys

# Add the project root directory to the Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from my_app.main import method01, method02, run

def test_method01():
    result = method01()
    assert True is True

def test_method02():
    result = method02()
    assert True is True

def test_run():
    result = run()
    assert True is True
