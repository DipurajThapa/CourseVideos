# file: examples/card_debug.py
class LoyaltyCard:
    def __init__(self, customer, stamps=0):
        self.customer = customer
        self.stamps = stamps

    def add_stamp(self):
        self.stamps += 1

    def free_teas(self):
        return self.stamps // 10

    def card_line():
        return f"{self.customer}: {self.stamps} stamps"
