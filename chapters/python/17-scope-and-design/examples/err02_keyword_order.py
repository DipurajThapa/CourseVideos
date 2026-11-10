# file: examples/err02_keyword_order.py
def order_line(item, price, qty=1):
    cost = price * qty
    return f"{qty} x {item:<6} {cost:>5.2f}"

print(order_line(item="Cake", 4.0))
