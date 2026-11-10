# file: examples/ex07_list_field.py
from dataclasses import dataclass, field


@dataclass
class Order:
    customer: str
    items: list = field(default_factory=list)


lina = Order("Lina")
omar = Order("Omar")
lina.items.append("Tea")
print(lina)
print(omar)
