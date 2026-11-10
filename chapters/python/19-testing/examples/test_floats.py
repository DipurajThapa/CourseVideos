# file: examples/test_floats.py
import pytest


def test_exact():
    total = 0.1 * 3
    assert total == 0.3


def test_rounded():
    total = 0.1 * 3
    assert round(total, 2) == 0.3


def test_approx():
    total = 0.1 * 3
    assert total == pytest.approx(0.3)
