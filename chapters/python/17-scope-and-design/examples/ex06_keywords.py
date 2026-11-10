# file: examples/ex06_keywords.py
def order_line(item, price, qty=1):
    return f"{qty} x {item:<6} {price * qty:>5.2f}"

print(order_line("Tea", 3.5))
print(order_line("Cake", 4.0, qty=2))
print(order_line(price=2.75, item="Scone"))
