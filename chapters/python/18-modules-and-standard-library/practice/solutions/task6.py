# file: practice/solutions/task6.py
import random

random.seed(3)
drinks = ["Tea", "Coffee", "Juice"]
for day in ["Monday", "Tuesday", "Wednesday"]:
    print(day, random.choice(drinks))
