# file: practice/solutions/task5.py
def hours_text(minutes):
    """Return minutes as text in hours and minutes."""
    return f"{minutes // 60} h {minutes % 60} min"

print(hours_text(135))
print(hours_text(60))
print(hours_text(45))
