# file: practice/solutions/task8.py
import math

def cakes_to_bake(slices, per_cake=8):
    """Return how many whole cakes give at least this many slices."""
    return math.ceil(slices / per_cake)

print(cakes_to_bake(20))
print(cakes_to_bake(16))
print(cakes_to_bake(1))
