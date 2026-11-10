# file: practice/solutions/task4.py
def free_teas(cups):
    """Return how many free teas a customer has earned: one for every 10 cups."""
    return cups // 10


def test_no_cups():
    assert free_teas(0) == 0


def test_one_short():
    assert free_teas(9) == 0


def test_exactly_ten():
    assert free_teas(10) == 1


def test_many_cups():
    assert free_teas(25) == 2
