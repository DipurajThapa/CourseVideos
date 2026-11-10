# file: examples/err02_no_brackets.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


tea = MenuItem
print(tea.price)
