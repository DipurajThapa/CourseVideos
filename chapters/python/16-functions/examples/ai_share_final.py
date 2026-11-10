# file: examples/ai_share_final.py
def share(total, people, tip_percent):
    """Return one share with the tip, rounded to cents."""
    return round(total * (1 + tip_percent / 100) / people, 2)

s1 = share(40.0, 4, 10)
s2 = share(43.07, 4, 0)
s3 = share(10.0, 3, 0)
print(s1, s1 == 11.0)
print(s2, s2 == 10.77)
print(s3, s3 == 3.33)
print(f"Table 4: each pays {s1:.2f}")
