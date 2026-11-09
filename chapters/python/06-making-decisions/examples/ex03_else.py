# file: examples/ex03_else.py
bill = float(input("Bill total: "))
people = int(input("Number of people: "))
if people > 0:
    share = bill / people
    print(f"Each pays: {share:.2f}")
else:
    print("People must be 1 or more.")
print("Done.")
