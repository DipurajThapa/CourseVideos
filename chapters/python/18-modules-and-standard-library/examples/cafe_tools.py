# file: examples/cafe_tools.py
"""Small tools for the Corner Cafe programs."""

def with_tax(price, rate=1.1):
    """Return the price with tax, rounded to cents."""
    return round(price * rate, 2)

def money(amount):
    """Return an amount as text with two decimal places."""
    return f"{amount:.2f}"

if __name__ == "__main__":
    print("Checking cafe_tools")
    print(with_tax(3.5) == 3.85)
    print(money(4) == "4.00")
