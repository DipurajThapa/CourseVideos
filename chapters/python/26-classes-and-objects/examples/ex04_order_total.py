# file: examples/ex04_order_total.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return round(sum([item.price for item in self.items]), 2)


order = Order("Lina")
order.add(MenuItem("Tea", 3.5))
print(order.total())
order.add(MenuItem("Cake", 4.25))
print(order.total())
