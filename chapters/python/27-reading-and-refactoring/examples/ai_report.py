# file: examples/ai_report.py
from stock_final import chk

stock = {"Tea": 10, "Cake": 4}
print("Order more:", chk(stock, {"Cake": 2}))
