# file: examples/err03_attribute_typo.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


tea = MenuItem("Tea", 3.5)
print(tea.prcie)
