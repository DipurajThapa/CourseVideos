# file: examples/ai_share_noround.py
def share(total, people, tip_percent):
    return total * (1 + tip_percent / 100) / people

print(share(40.0, 4, 10), share(40.0, 4, 10) == 11.0)
print(share(43.07, 4, 0), share(43.07, 4, 0) == 10.77)
print(share(10.0, 3, 0), share(10.0, 3, 0) == 3.33)
