# file: practice/solutions/task6.py
menu = {
    "tea": {"price": 3.5, "vegan": True},
    "cake": {"price": 4.25, "vegan": False},
    "salad": {"price": 7.0, "vegan": True},
}
print("Vegan choices:")
for name, info in menu.items():
    if info["vegan"]:
        print(f"- {name} ({info['price']:.2f})")
