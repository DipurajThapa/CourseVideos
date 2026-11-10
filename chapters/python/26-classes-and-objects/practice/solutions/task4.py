# file: practice/solutions/task4.py
class Basket:
    def __init__(self):
        self.prices = []

    def add(self, price):
        self.prices.append(price)

    def total(self):
        return round(sum(self.prices), 2)


basket = Basket()
for price in [2.5, 1.25, 3.0]:
    basket.add(price)
print(f"Items: {len(basket.prices)}")
print(f"Total: {basket.total():.2f}")
