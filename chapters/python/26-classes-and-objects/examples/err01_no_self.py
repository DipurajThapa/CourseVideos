# file: examples/err01_no_self.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def with_tax():
        return round(self.price * 1.1, 2)


tea = MenuItem("Tea", 3.5)
print(tea.with_tax())
