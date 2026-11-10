# file: examples/ai_vegan_cases.py
cases = {
    "Normal": [("Tea", 3.5, True), ("Scone", 2.75, False)],
    "No vegan": [("Scone", 2.75, False)],
    "Same price": [("Tea", 3.5, True), ("Mint", 3.5, True)],
}
for case, menu in cases.items():
    loop = []
    for name, price, vegan in menu:
        if vegan:
            loop.append(round(price * 1.1, 2))
    ai = [round(price * 1.1, 2) for name, price, vegan in menu]
    print(case, "->", ai, "pass" if ai == loop else "FAIL")
