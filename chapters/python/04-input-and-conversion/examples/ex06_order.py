# file: examples/ex06_order.py
customer = input("Your name: ")
tea_count = int(input("How many teas? "))
sandwich_count = int(input("How many sandwiches? "))
tea_price = 3.5
sandwich_price = 6

name = customer.strip().title()
tea_total = tea_price * tea_count
sandwich_total = sandwich_price * sandwich_count
to_pay = tea_total + sandwich_total
tea_label = f"Tea x {tea_count}"
sandwich_label = f"Sandwich x {sandwich_count}"
line = "-" * 24

print(f"{' CORNER CAFE ':=^24}")
print(f"Customer: {name}")
print(line)
print(f"{tea_label:<16}{tea_total:>8.2f}")
print(f"{sandwich_label:<16}{sandwich_total:>8.2f}")
print(line)
print(f"{'TO PAY':<16}{to_pay:>8.2f}")
