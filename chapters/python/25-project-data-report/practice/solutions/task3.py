# file: practice/solutions/task3.py
def money(amount, currency):
    """Return an amount as text, such as EUR 7.50."""
    return f"{currency} {amount:.2f}"


settings = {"currency": "EUR", "tax_rate": 0.1}
print(money(7.5, settings["currency"]))
print(money(12, settings["currency"]))
