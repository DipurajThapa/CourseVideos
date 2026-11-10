# file: examples/test_errors_missing.py
import pytest


def with_tax(price):
    return round(price * 1.1, 2)


def test_negative_price_is_refused():
    with pytest.raises(ValueError):
        with_tax(-1)
