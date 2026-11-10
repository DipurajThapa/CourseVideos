# file: examples/ai_record_fixed.py
def record_sale(price, sales):
    sales.append(price)
    return sales

monday = record_sale(3.5, [])
monday = record_sale(4.0, monday)
tuesday = record_sale(4.25, [])
print("Monday:", monday)
print("Tuesday:", tuesday)
