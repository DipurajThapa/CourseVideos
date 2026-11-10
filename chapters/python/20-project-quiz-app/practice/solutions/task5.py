# file: practice/solutions/task5.py
def stars(points, total):
    """Return one star for each point and one dash for each miss."""
    return "*" * points + "-" * (total - points)


print(stars(3, 4))
print(stars(0, 4))
print(stars(4, 4))
