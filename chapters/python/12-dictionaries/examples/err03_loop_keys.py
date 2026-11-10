# file: examples/err03_loop_keys.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
total = 0
for price in menu:
    total += price
print(total)
