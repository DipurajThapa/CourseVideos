# file: practice/solutions/task8.py
import pytest


def tip(total, percent=10):
    """Return the tip for a bill."""
    return total * percent / 100


def test_ten_percent():
    assert tip(40) == 4


def test_custom_percent():
    assert tip(20, 15) == 3


def test_decimal_bill():
    assert tip(12.3) == pytest.approx(1.23)
