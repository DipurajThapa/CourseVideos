# file: examples/ex02_trace.py
from till_old import f

o = [("Tea", 3.5, 2), ("Cake", 4.25, 1)]
t = 0
for x in o:
    t = t + x[1] * x[2]
    print(x[0], x[1], x[2], "t =", t)
print("Result:", f(o, False))
