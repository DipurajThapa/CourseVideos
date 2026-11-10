# file: practice/solutions/task1.py
def g(p, n):
    r = 0
    for i in range(n):
        r = r + p
    return r


print(g(3.5, 2))
print(g(4.25, 0))
