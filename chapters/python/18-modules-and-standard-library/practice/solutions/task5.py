# file: practice/solutions/task5.py
from datetime import timedelta

starts = timedelta(hours=7, minutes=30)
ends = timedelta(hours=16)
shift = ends - starts
print("Shift:", shift)
print("Minutes:", shift.total_seconds() / 60)
