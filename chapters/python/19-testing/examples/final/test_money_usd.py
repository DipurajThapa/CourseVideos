# file: examples/final/test_money_usd.py
from cafe_tools import money


def test_money_shows_usd():
    assert money(4) == "USD 4.00"
