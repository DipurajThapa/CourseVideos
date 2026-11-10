# file: examples/err01_no_prefix.py
from cafe_tools import with_tax


def tea_tax():
    assert with_tax(3.5) == 3.85
