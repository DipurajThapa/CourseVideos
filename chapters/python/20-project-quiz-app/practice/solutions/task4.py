# file: practice/solutions/task4.py
def grade(percent):
    """Return a word for the score."""
    if percent == 100:
        return "Expert"
    elif percent >= 75:
        return "Ready"
    elif percent >= 50:
        return "Almost"
    else:
        return "Practise again"


for percent in [100, 80, 50, 40]:
    print(percent, grade(percent))
