# file: practice/solutions/task6.py
from dataclasses import dataclass


@dataclass
class Drink:
    name: str
    size: str
    price: float


usual = Drink("Latte", "Large", 4.2)
today = Drink("Latte", "Large", 4.2)
print(usual)
print(usual == today)
print(usual == Drink("Latte", "Small", 3.6))
