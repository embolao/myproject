import pytest


def f():
    """docstring for f"""
    return 3


def test_function():
    """docstring for test_function"""
    assert f() == 3


def func1():
    """docstring for func1"""
    raise ValueError("Exception func1 raised")


def test_case():
    """docstring for test_case"""
    with pytest.raises(Exception) as excinfo:
        func1()
    print(str(excinfo))
