# file: practice/solutions/task7.py
from dataclasses import dataclass, field


@dataclass
class Order:
    customer: str
    prices: list = field(default_factory=list)

    def total(self):
        return round(sum(self.prices), 2)


@dataclass
class Table:
    number: int
    orders: list = field(default_factory=list)

    def total(self):
        return round(sum([order.total() for order in self.orders]), 2)


table = Table(4)
table.orders.append(Order("Lina", [3.5, 4.25]))
table.orders.append(Order("Omar", [2.75]))
for order in table.orders:
    print(f"{order.customer:<6}{order.total():>6.2f}")
print(f"Table {table.number}: {table.total():.2f}")
