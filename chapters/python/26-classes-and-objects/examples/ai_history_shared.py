# file: examples/ai_history_shared.py
from card_shared import LoyaltyCard

lina = LoyaltyCard("Lina")
omar = LoyaltyCard("Omar")
lina.add_stamp("Latte")
print(lina.customer, lina.history)
print(omar.customer, omar.history)
