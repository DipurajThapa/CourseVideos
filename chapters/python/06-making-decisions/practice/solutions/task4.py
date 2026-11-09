# file: practice/solutions/task4.py
hour = int(input("Hour (0 to 23): "))
if hour >= 8 and hour < 18:
    print("The Corner Cafe is open.")
else:
    print("Sorry, the Corner Cafe is closed.")
