# file: examples/err02_missing_import.py
from cafe_tools import with_tax


def test_boxes():
    assert boxes_needed(40) == 4
