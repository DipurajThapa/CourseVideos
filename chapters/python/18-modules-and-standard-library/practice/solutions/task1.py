# file: practice/solutions/task1.py
import math

guests = 30
per_table = 4
print("Tables needed:", math.ceil(guests / per_table))
print("Full tables:", math.floor(guests / per_table))
