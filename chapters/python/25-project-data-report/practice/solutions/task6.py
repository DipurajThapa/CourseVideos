# file: practice/solutions/task6.py
import json
from pathlib import Path


def load_settings(path):
    """Return the settings, or raise ValueError with a clear message."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"missing settings file {path.name}")


try:
    settings = load_settings(Path("shop.json"))
except ValueError as error:
    print("Stopped:", error)
else:
    print(settings)
