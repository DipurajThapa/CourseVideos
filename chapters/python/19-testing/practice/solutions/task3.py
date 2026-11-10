# file: practice/solutions/task3.py
def minutes_to_hours(minutes):
    return minutes / 60


def test_two_hours():
    assert minutes_to_hours(120) == 2


def test_half_hour():
    assert minutes_to_hours(30) == 0.5
