# file: practice/solutions/task8.py
def member_price(price, is_member):
    """Return the price after a 10 percent member discount."""
    if is_member:
        return round(price * 0.9, 2)
    return price

print(member_price(4.0, True), member_price(4.0, True) == 3.6)
print(member_price(4.0, False), member_price(4.0, False) == 4.0)
print(member_price(2.75, True), member_price(2.75, True) == 2.48)
