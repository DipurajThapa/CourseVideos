# file: examples/ex02_else_finally.py
from pathlib import Path


def load(name):
    try:
        text = Path(name).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"{name}: no scores yet")
    else:
        print(text, end="")
    finally:
        print(f"{name}: done")


load("week.csv")
load("month.csv")
