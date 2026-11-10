# file: examples/err02_dump_no_file.py
import json

order = {"drink": "Tea", "cups": 2}
text = json.dump(order)
print(text)
