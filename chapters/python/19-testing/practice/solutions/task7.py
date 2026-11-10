# file: practice/solutions/task7.py
def seats_needed(guests, per_table=4):
    """Return how many tables are needed for the guests."""
    return (guests + per_table - 1) // per_table


def test_full_tables():
    assert seats_needed(8) == 2


def test_one_extra_guest():
    assert seats_needed(9) == 3


def test_no_guests():
    assert seats_needed(0) == 0
