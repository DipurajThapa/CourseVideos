# file: examples/ex07_bad_json.py
import json

texts = ['{"item": "Tea"}', "{'item': 'Tea'}", ""]
for text in texts:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        print("Not valid JSON:", error.msg)
    else:
        print("Loaded:", data["item"])
