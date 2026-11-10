# file: examples/ex04_print_not_return.py
def tax_print(price):
    print(round(price * 1.1, 2))

result = tax_print(3.5)
print("result is", result)
