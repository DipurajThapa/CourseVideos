# file: practice/solutions/task3.py
coins = 100
days = 0
while coins > 10:
    coins = coins // 2
    days += 1
print(f"After {days} days: {coins} coins")
