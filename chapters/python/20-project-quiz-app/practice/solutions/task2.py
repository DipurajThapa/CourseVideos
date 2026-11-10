# file: practice/solutions/task2.py
def same_price(given, correct):
    """Return True if two prices are the same number."""
    return float(given) == float(correct)


print(same_price("3.5", "3.50"))
print(same_price("3.50", "3.05"))
