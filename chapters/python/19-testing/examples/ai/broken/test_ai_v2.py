# file: examples/ai/broken/test_ai_v2.py
from cafe_tools import with_tax, money, boxes_needed


def test_tax():
    assert with_tax(3.5) == 3.85


def test_two_items():
    total = with_tax(1.0) + with_tax(2.0)
    assert round(total, 2) == 3.3


def test_money():
    assert money(4) == "USD 4.00"


def test_full_boxes():
    assert boxes_needed(24) == 2


def test_part_box():
    assert boxes_needed(40) == 4


def test_zero():
    assert boxes_needed(0) == 0


def test_just_over():
    assert boxes_needed(13) == 2
