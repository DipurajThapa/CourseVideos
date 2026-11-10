# file: examples/ai_share_missing_fixed.py
def share(total, people, tip_percent):
    return round(total * (1 + tip_percent / 100) / people, 2)

print("Table 4")
print(share(40.0, 4, 10))
