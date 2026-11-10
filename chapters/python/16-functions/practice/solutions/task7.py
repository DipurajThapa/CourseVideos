# file: practice/solutions/task7.py
def average(values):
    """Return the average of a list, or 0.0 for an empty list."""
    if len(values) == 0:
        return 0.0
    return round(sum(values) / len(values), 2)

def report(day, sales):
    print(f"{day}: average sale {average(sales):.2f}")

report("Monday", [3.5, 4.0, 2.75])
report("Sunday", [])
