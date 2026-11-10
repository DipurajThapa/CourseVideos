# file: examples/ai/debug/test_percentage.py
from quiz_logic import percentage


def test_three_of_four():
    assert percentage(3, 4) == 75
