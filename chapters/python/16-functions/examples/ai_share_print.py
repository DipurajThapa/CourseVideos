# file: examples/ai_share_print.py
def share(total, people, tip_percent):
    each = total * (1 + tip_percent / 100) / people
    print(round(each, 2))

print(f"Each pays {share(40.0, 4, 10):.2f}")
