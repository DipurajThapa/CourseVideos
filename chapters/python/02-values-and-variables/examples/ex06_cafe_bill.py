# file: examples/ex06_cafe_bill.py
customer = "Asha"
tea_price = 3.5
sandwich_price = 6
tea_count = 2
is_member = True
member_discount = 0.1

tea_total = tea_price * tea_count
bill = tea_total + sandwich_price
discount = bill * member_discount
to_pay = bill - discount

print("Customer:", customer)
print("Teas:", tea_count, "x", tea_price, "=", tea_total)
print("Sandwich:", sandwich_price)
print("Bill:", bill)
print("Member:", is_member)
print("Discount:", discount)
print("To pay:", to_pay)
