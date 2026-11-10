# file: examples/ex06_dataclass.py
from dataclasses import dataclass


@dataclass
class MenuItem:
    name: str
    price: float


tea = MenuItem("Tea", 3.5)
print(tea)
print(tea == MenuItem("Tea", 3.5))
print(tea == MenuItem("Tea", 3.0))
