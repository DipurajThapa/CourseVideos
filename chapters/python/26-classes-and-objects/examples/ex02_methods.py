# file: examples/ex02_methods.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def with_tax(self):
        return round(self.price * 1.1, 2)

    def label(self):
        return f"{self.name}: {self.with_tax():.2f}"


tea = MenuItem("Tea", 3.5)
print(tea.with_tax())
print(tea.label())
