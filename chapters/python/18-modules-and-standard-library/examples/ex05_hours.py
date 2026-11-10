# file: examples/ex05_hours.py
from datetime import timedelta

opens = timedelta(hours=8)
open_for = timedelta(hours=9, minutes=30)
closes = opens + open_for
print("Closes at", closes)
print("Minutes open:", open_for.total_seconds() / 60)
