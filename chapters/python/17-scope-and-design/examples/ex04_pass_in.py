# file: examples/ex04_pass_in.py
def add_sale(count):
    return count + 1

sales_count = 0
sales_count = add_sale(sales_count)
sales_count = add_sale(sales_count)
print(sales_count)
