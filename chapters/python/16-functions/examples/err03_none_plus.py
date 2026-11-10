# file: examples/err03_none_plus.py
def tax_print(price):
    print(round(price * 1.1, 2))

bill = tax_print(3.5) + 1
print(bill)
