# file: practice/solutions/task3.py
def with_tip(total):
    return round(total * 1.15, 2)

bill = with_tip(20.0)
print(bill)
print(bill + 5)
