# file: examples/ai_secret_flawed.py
import random
random.seed(1)
lowest = 20
highest = 1
for draw in range(10000):
    secret = random.randrange(1, 20)
    if secret < lowest:
        lowest = secret
    if secret > highest:
        highest = secret
print("Lowest:", lowest)
print("Highest:", highest)
