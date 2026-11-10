# file: practice/solutions/task8.py
def count_correct(given, answers):
    """Return how many answers match."""
    points = 0
    for i in range(len(answers)):
        if given[i].strip().lower() == answers[i]:
            points += 1
    return points


assert count_correct(["yes", "no"], ["yes", "yes"]) == 1
assert count_correct(["no", "yes"], ["yes", "yes"]) == 1
assert count_correct([], []) == 0
print("All checks passed")
