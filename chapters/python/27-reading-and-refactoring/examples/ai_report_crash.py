# file: examples/ai_report_crash.py
from stock_v2 import chk

stock = {"Tea": 10, "Cake": 4}
print("Order more:", chk(stock, {"Cake": 2}))
