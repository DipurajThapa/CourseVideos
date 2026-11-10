# file: examples/card_shared.py
class LoyaltyCard:
    history = []

    def __init__(self, customer, stamps=0):
        self.customer = customer
        self.stamps = stamps

    def add_stamp(self, drink="Tea"):
        self.stamps += 1
        self.history.append(drink)
