# file: examples/ai_share_final.py
def share(total, people, tip_percent):
    """Return one share with the tip, rounded to cents."""
    return round(total * (1 + tip_percent / 100) / people, 2)

print(f"Table 4: each pays {share(40.0, 4, 10):.2f}")
print(f"Table 7: each pays {share(43.07, 4, 0):.2f}")
