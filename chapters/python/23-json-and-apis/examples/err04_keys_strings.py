# file: examples/err04_keys_strings.py
import json

tables = {1: "Asha", 2: "Omar"}
back = json.loads(json.dumps(tables))
print(back)
print(back[1])
