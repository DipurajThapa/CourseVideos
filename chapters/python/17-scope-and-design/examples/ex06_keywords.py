# file: examples/ex06_keywords.py
def order_line(item, price, qty=1):
    cost = price * qty
    return f"{qty} x {item:<6} {cost:>5.2f}"

print(order_line("Tea", 3.5))
print(order_line("Cake", 4.0, qty=2))
print(order_line(price=2.75, item="Scone"))
