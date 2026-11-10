# file: examples/test_errors.py
import pytest
from cafe_tools import with_tax


def test_tea_price():
    assert with_tax(3.5) == 3.85


def test_negative_price_is_refused():
    with pytest.raises(ValueError):
        with_tax(-1)
