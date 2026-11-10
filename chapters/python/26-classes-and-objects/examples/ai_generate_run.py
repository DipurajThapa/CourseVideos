# file: examples/ai_generate_run.py
from card_ai import LoyaltyCard

card = LoyaltyCard("Lina")
for cup in range(25):
    card.add_stamp()
print(card.stamps, card.free_teas)
