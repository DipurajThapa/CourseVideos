# file: practice/solutions/task5.py
import pytest


def order_total(prices):
    return sum(prices)


def test_total_rounded():
    assert round(order_total([0.1, 0.2]), 2) == 0.3


def test_total_approx():
    assert order_total([1.1, 2.2]) == pytest.approx(3.3)
