# file: practice/solutions/task5.py
from pathlib import Path


def read_pins(path):
    pins = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        name, version = line.split("==")
        pins[name] = version
    return pins


laptop = read_pins("laptop_requirements.txt")
home = read_pins("home_requirements.txt")
for name, version in laptop.items():
    if home.get(name) != version:
        print(f"{name}: laptop {version}, home {home.get(name)}")
