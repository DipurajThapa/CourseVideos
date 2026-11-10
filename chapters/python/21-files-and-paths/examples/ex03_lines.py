# file: examples/ex03_lines.py
with open("menu.txt", encoding="utf-8") as file:
    for line in file:
        name = line.strip()
        print(f"- {name} ({len(name)} letters)")
