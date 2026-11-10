# file: examples/till_old.py
def f(a, b):
    t = 0
    for x in a:
        t = t + x[1] * x[2]
    if b:
        t = t - t * 0.1
    t2 = t * 1.1
    return round(t2, 2)


if __name__ == "__main__":
    o = [("Tea", 3.5, 2), ("Cake", 4.25, 1)]
    print(f(o, False))
    print(f(o, True))
    print(f([], True))
