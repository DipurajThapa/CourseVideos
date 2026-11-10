# file: examples/ex02_pins.py
lines = ["requests==2.32.3", "tabulate", "pytest>=8"]
for line in lines:
    if "==" in line:
        print(f"{line:<18} pinned")
    else:
        print(f"{line:<18} not pinned")
