# file: examples/ex03_use_tools.py
import cafe_tools

price = cafe_tools.with_tax(4.0)
print(price)
print(cafe_tools.money(price))
