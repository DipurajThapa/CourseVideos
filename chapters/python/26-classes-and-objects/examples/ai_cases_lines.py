# file: examples/ai_cases_lines.py
from card_lines import LoyaltyCard

cases = [("No stamps", 0, 0, 0), ("Nine stamps", 0, 9, 0),
         ("Ten stamps", 0, 10, 1), ("25 stamps", 0, 25, 2),
         ("Old card, 12", 12, 0, 1)]
for name, start, cups, expected in cases:
    card = LoyaltyCard("Test", start)
    for cup in range(cups):
        card.add_stamp()
    got = card.free_teas()
    result = "pass" if got == expected else "FAIL"
    print(f"{name}: expected {expected}, got {got} {result}")
print(LoyaltyCard("Omar", 12).card_line())
