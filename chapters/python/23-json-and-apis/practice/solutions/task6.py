# file: practice/solutions/task6.py
import json


def load_json(path):
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"No file called {path}")
    except json.JSONDecodeError as error:
        print(f"{path} is not valid JSON: {error.msg}")
    return None


for path in ["good.json", "missing.json", "broken.json"]:
    print(path, "->", load_json(path))
