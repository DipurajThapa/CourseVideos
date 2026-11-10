# file: practice/solutions/task5.py
def receipt_line(item, price, qty=1, currency="USD"):
    return f"{qty} x {item:<8} {currency} {price * qty:>5.2f}"

print(receipt_line("Tea", 3.5))
print(receipt_line("Cake", 4.0, qty=2))
print(receipt_line("Scone", 2.75, currency="EUR"))
print(receipt_line(price=1.5, item="Biscuit", qty=3))
