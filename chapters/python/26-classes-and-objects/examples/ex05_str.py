# file: examples/ex05_str.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.price:.2f})"


tea = MenuItem("Tea", 3.5)
print(tea)
print(f"Today: {tea}")
