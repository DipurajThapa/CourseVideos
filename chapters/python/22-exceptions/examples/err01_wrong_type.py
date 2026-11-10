# file: examples/err01_wrong_type.py
answer = "four"
try:
    score = int(answer)
except TypeError:
    print("Please type a whole number.")
