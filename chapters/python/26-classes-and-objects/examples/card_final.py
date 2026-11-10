# file: examples/card_final.py
class LoyaltyCard:
    def __init__(self, customer, stamps=0):
        self.customer = customer
        self.stamps = stamps
        self.history = []

    def add_stamp(self, drink="Tea"):
        self.stamps += 1
        self.history.append(drink)

    def free_teas(self):
        return self.stamps // 10

    def card_line(self):
        return f"{self.customer}: {self.stamps} stamps"
