# file: examples/ai_mine.py
class LoyaltyCard:
    def __init__(self, customer, stamps=0):
        self.customer = customer
        self.stamps = stamps

    def add_stamp(self):
        self.stamps += 1


card = LoyaltyCard("Lina")
card.add_stamp()
card.add_stamp()
print(card.customer, card.stamps)
