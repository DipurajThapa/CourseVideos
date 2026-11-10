# file: practice/solutions/task3.py
import json

values = json.loads('[1, 2.5, "3", true, null]')
for value in values:
    print(value, type(value))
