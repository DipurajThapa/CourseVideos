# file: examples/ai_explain_check.py
from stock_old import chk

stock = {"Tea": 10, "Cake": 4, "Scone": 5}
order = {"Tea": 2, "Cake": 2, "Scone": 2}
print(chk(stock, order))
for item in order:
    print(item, "left:", stock[item] - order[item])
