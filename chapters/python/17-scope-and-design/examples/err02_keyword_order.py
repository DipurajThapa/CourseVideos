# file: examples/err02_keyword_order.py
def order_line(item, price, qty=1):
    return f"{qty} x {item:<6} {price * qty:>5.2f}"

print(order_line(item="Cake", 4.0))
