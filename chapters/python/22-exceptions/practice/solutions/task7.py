# file: practice/solutions/task7.py
import pytest


def order_total(quantity, price):
    if quantity < 1:
        raise ValueError(f"quantity must be at least 1, not {quantity}")
    return quantity * price


def test_two_teas():
    assert order_total(2, 3.5) == 7.0


def test_zero_is_refused():
    with pytest.raises(ValueError):
        order_total(0, 3.5)


def test_negative_is_refused():
    with pytest.raises(ValueError):
        order_total(-1, 3.5)
