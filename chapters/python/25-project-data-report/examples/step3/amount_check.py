# file: examples/step3/amount_check.py
from report_tools import parse_amount

for text in ["3.50", "four", "-2.00"]:
    try:
        print(f"{text!r} gives", parse_amount(text))
    except ValueError as error:
        print(f"{text!r} refused:", error)
