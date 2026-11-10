# file: examples/test_till_old.py
from till_old import f

ORDER = [("Tea", 3.5, 2), ("Cake", 4.25, 1)]


def test_normal_order():
    assert f(ORDER, False) == 12.38


def test_member_order():
    assert f(ORDER, True) == 11.14


def test_empty_order():
    assert f([], True) == 0.0
