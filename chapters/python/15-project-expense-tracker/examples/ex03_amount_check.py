# file: examples/ex03_amount_check.py
print("12.50".replace(".", "", 1))
print("1.2.3".replace(".", "", 1))
for text in ["12.50", "30", "12,50", "twelve", "1.2.3", "-5"]:
    print(f"{text:>7}", text.replace(".", "", 1).isdigit())
