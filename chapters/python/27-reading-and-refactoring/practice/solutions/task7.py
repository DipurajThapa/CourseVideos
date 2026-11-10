# file: practice/solutions/task7.py
def s(l):
    t = 0
    for x in l:
        if x > 0:
            t = t + x
    return round(t, 2)


def day_sales(amounts):
    """Add up the positive amounts, rounded to 2 places."""
    total = sum(amount for amount in amounts if amount > 0)
    return round(total, 2)


cases = [[3.5, 4.25], [], [2.75, -1, 3.85], [0, 0.1, 0.2]]
for case in cases:
    print(s(case), day_sales(case), s(case) == day_sales(case))
