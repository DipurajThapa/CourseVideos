# file: examples/err02_unset.py
answer = "four"
try:
    score = int(answer)
except ValueError:
    print("Not a whole number.")
print(score + 1)
