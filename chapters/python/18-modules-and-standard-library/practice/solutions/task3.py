# file: practice/solutions/task3.py
from pathlib import Path

menu = Path("menus") / "winter_menu.txt"
print(menu.name)
print(menu.stem)
print(menu.suffix)
