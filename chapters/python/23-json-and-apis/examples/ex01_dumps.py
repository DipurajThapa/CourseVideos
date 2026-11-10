# file: examples/ex01_dumps.py
import json

menu = {"item": "Tea", "price": 3.5, "vegan": True, "offer": None}
text = json.dumps(menu)
print(text)
print(type(text))
