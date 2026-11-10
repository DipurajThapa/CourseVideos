# file: examples/broken/test_cafe_tools.py
from cafe_tools import with_tax, money, boxes_needed


def test_tea_with_tax():
    assert with_tax(3.5) == 3.85


def test_money_has_two_decimals():
    assert money(4) == "4.00"


def test_boxes_for_40_biscuits():
    assert boxes_needed(40) == 4
