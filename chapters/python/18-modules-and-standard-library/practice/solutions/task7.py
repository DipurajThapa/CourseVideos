# file: practice/solutions/task7.py
import math

needed = {"biscuits": 40, "cups": 75, "napkins": 130}
per_box = {"biscuits": 12, "cups": 50, "napkins": 100}
for item, amount in needed.items():
    boxes = math.ceil(amount / per_box[item])
    print(f"{item:<9} {amount:>4} -> {boxes} boxes")
