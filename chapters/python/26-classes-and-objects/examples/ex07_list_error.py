# file: examples/ex07_list_error.py
from dataclasses import dataclass


@dataclass
class Order:
    customer: str
    items: list = []
