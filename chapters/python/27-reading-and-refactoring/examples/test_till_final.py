# file: examples/test_till_final.py
from till_final import order_total

ORDER = [("Tea", 3.5, 2), ("Cake", 4.25, 1)]


def test_normal_order():
    assert order_total(ORDER, False) == 12.38


def test_member_order():
    assert order_total(ORDER, True) == 11.14


def test_empty_order():
    assert order_total([], True) == 0.0
