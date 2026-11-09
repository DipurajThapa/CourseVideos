# file: examples/ex02_ask_again.py
people = int(input("Number of people: "))
while people < 1:
    print("Please type 1 or more.")
    people = int(input("Number of people: "))
print(f"Table for {people}, please follow me.")
