# file: practice/solutions/task5.py
class Drink:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def __str__(self):
        return f"{self.size} {self.name}: {self.price:.2f}"


print(Drink("Latte", "Large", 4.2))
print(Drink("Tea", "Small", 2.5))
