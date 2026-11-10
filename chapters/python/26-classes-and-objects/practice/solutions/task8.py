# file: practice/solutions/task8.py
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.prices = []

    def add(self, price):
        self.prices.append(price)

    def total(self):
        return round(sum(self.prices), 2)


order = Order("Lina")
order.add(3.5)
print(order.total())
order.add(4.25)
print(order.total())
