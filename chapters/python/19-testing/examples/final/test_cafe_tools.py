# file: examples/final/test_cafe_tools.py
from cafe_tools import with_tax, money, boxes_needed


def test_tea_with_tax():
    assert with_tax(3.5) == 3.85


def test_two_items():
    total = with_tax(1.0) + with_tax(2.0)
    assert round(total, 2) == 3.3


def test_money_shows_usd():
    assert money(4) == "USD 4.00"


def test_boxes_full_and_part():
    assert boxes_needed(24) == 2
    assert boxes_needed(40) == 4


def test_boxes_edges():
    assert boxes_needed(0) == 0
    assert boxes_needed(12) == 1
    assert boxes_needed(13) == 2
