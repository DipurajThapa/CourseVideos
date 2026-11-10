# file: practice/solutions/price_tools.py
def discount(price, percent):
    """Return the price after a discount, rounded to cents."""
    return round(price * (100 - percent) / 100, 2)

if __name__ == "__main__":
    print(discount(10, 10) == 9.0)
