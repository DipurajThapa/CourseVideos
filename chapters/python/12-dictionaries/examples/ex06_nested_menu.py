# file: examples/ex06_nested_menu.py
menu = {
    "tea": {"price": 3.5, "vegan": True},
    "cake": {"price": 4.25, "vegan": False},
    "scone": {"price": 2.75, "vegan": True},
}
print(menu["cake"]["price"])
for name, info in menu.items():
    if info["vegan"]:
        print(f"{name} is vegan, {info['price']:.2f}")
