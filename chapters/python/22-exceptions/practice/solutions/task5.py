# file: practice/solutions/task5.py
def order_total(quantity, price):
    if quantity < 1:
        raise ValueError(f"quantity must be at least 1, not {quantity}")
    return quantity * price


for quantity in [2, 0]:
    try:
        print(f"Total: {order_total(quantity, 3.5):.2f}")
    except ValueError as error:
        print(f"Order refused: {error}")
