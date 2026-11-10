# file: examples/card_ai.py
class LoyaltyCard:
    def __init__(self, customer, stamps=0):
        self.customer = customer
        self.stamps = stamps
        self.free_teas = 0

    def add_stamp(self):
        self.stamps += 1
        if self.stamps == 10:
            self.free_teas += 1
