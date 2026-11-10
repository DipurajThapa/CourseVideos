# file: examples/broken/test_edges.py
from cafe_tools import boxes_needed


def test_no_biscuits():
    assert boxes_needed(0) == 0


def test_exactly_one_box():
    assert boxes_needed(12) == 1


def test_one_more_than_a_box():
    assert boxes_needed(13) == 2
