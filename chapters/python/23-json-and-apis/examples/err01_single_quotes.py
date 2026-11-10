# file: examples/err01_single_quotes.py
import json

text = "{'item': 'Tea', 'price': 3.5}"
data = json.loads(text)
print(data["item"])
