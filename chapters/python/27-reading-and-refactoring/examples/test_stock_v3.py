# file: examples/test_stock_v3.py
from stock_v3 import low_stock as chk

STOCK = {"Tea": 10, "Cake": 4, "Scone": 5}


def test_plenty_left():
    assert chk(STOCK, {"Tea": 2}) == []


def test_exactly_three_left():
    assert chk(STOCK, {"Scone": 2}) == []


def test_two_left():
    assert chk(STOCK, {"Cake": 2}) == ["Cake"]


def test_keeps_order_of_the_order():
    order = {"Scone": 3, "Cake": 3}
    assert chk(STOCK, order) == ["Scone", "Cake"]


def test_empty_order():
    assert chk(STOCK, {}) == []
