# file: examples/ai/broken/test_mine.py
from cafe_tools import boxes_needed


def test_full_boxes():
    assert boxes_needed(24) == 2


def test_part_box():
    assert boxes_needed(40) == 4
