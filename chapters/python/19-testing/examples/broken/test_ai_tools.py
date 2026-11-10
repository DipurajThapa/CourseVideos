# file: examples/broken/test_ai_tools.py
from cafe_tools import with_tax, boxes_needed


def test_tax():
    assert with_tax(3.5) == 3.85


def test_boxes():
    result = boxes_needed(24)
    assert result == 2


def test_zero():
    boxes_needed(0)
