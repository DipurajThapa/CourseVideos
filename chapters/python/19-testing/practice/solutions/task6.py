# file: practice/solutions/task6.py
def loyalty_level(points):
    """Return Gold from 100 points, Silver from 50, otherwise Bronze."""
    if points >= 100:
        return "Gold"
    elif points >= 50:
        return "Silver"
    else:
        return "Bronze"


def test_gold_at_100():
    assert loyalty_level(100) == "Gold"


def test_silver_at_50():
    assert loyalty_level(50) == "Silver"


def test_bronze_at_49():
    assert loyalty_level(49) == "Bronze"
