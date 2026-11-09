# file: examples/ex03_order_code.py
code = "CAFE-1024-T4"
hyphens = 0
for character in code:
    print(character, end=" ")
    if character == "-":
        hyphens += 1
print()
print(f"{len(code)} characters, {hyphens} hyphens")
