# file: examples/ex07_receipt.py
customer = "  asha  "
tea_price = 3.5
tea_count = 2
sandwich_price = 6
member_discount = 0.1

tea_total = tea_price * tea_count
bill = tea_total + sandwich_price
discount = bill * member_discount
to_pay = bill - discount
name = customer.strip().title()
tea_label = f"Tea x {tea_count}"
line = "-" * 24

print(f"{' CORNER CAFE ':=^24}")
print(f"Customer: {name}")
print(line)
print(f"{tea_label:<16}{tea_total:>8.2f}")
print(f"{'Sandwich':<16}{sandwich_price:>8.2f}")
print(f"{'Member discount':<16}{-discount:>8.2f}")
print(line)
print(f"{'TO PAY':<16}{to_pay:>8.2f}")
