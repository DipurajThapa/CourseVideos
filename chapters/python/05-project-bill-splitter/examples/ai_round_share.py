# file: examples/ai_round_share.py
total = 43.07
people = 4
share = round(total / people, 2)
print(f"Each pays: {share:.2f}")
print(f"Shares added up: {share * people:.2f}")
