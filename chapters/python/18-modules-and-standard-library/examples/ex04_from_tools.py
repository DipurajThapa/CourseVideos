# file: examples/ex04_from_tools.py
from cafe_tools import with_tax, money

for price in [3.5, 4.0, 2.75]:
    print(money(with_tax(price)))
