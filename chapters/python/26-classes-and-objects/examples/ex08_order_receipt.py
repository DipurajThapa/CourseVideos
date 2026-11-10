# file: examples/ex08_order_receipt.py
from dataclasses import dataclass, field


@dataclass
class MenuItem:
    name: str
    price: float


@dataclass
class Order:
    customer: str
    items: list = field(default_factory=list)

    def add(self, item):
        self.items.append(item)

    def total(self):
        return round(sum([item.price for item in self.items]), 2)


order = Order("Lina")
order.add(MenuItem("Tea", 3.5))
order.add(MenuItem("Cake", 4.25))
order.add(MenuItem("Tea", 3.5))
print(f"Order for {order.customer}")
for item in order.items:
    print(f"{item.name:<8}{item.price:>6.2f}")
print(f"{'Total':<8}{order.total():>6.2f}")
