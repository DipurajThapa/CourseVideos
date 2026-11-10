# file: examples/test_loyalty.py
from card_final import LoyaltyCard


def stamped(cups, start=0):
    card = LoyaltyCard("Test", start)
    for cup in range(cups):
        card.add_stamp()
    return card


def test_no_stamps():
    assert stamped(0).free_teas() == 0


def test_nine_stamps():
    assert stamped(9).free_teas() == 0


def test_ten_stamps():
    assert stamped(10).free_teas() == 1


def test_25_stamps():
    assert stamped(25).free_teas() == 2


def test_old_card():
    assert stamped(0, start=12).free_teas() == 1


def test_each_card_has_its_own_history():
    lina = LoyaltyCard("Lina")
    omar = LoyaltyCard("Omar")
    lina.add_stamp("Latte")
    assert omar.history == []
