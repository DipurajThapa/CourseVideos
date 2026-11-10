# file: practice/solutions/task8.py
def can_seat(free_chairs, group):
    return group <= free_chairs


def ai_can_seat(free_chairs, group):
    return group < free_chairs


def fixed_can_seat(free_chairs, group):
    """The AI's version with <= put back: a full table still fits."""
    return group <= free_chairs


cases = [(4, 2), (4, 4), (4, 5), (0, 1)]
ai_results = []
fixed_results = []
for chairs, group in cases:
    old = can_seat(chairs, group)
    ai_results.append("pass" if ai_can_seat(chairs, group) == old else "FAIL")
    fixed_results.append("pass" if fixed_can_seat(chairs, group) == old else "FAIL")
print("AI:   ", ai_results)
print("Fixed:", fixed_results)
