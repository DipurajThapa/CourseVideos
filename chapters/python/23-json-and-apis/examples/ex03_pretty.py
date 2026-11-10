# file: examples/ex03_pretty.py
import json

order = {"drink": "Café au lait", "sizes": ["small", "large"]}
print(json.dumps(order))
print(json.dumps(order, ensure_ascii=False))
print(json.dumps(order, indent=2, ensure_ascii=False))
