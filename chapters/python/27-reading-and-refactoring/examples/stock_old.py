# file: examples/stock_old.py
def chk(s, o):
    r = []
    for k in o:
        if s[k] - o[k] < 3:
            r.append(k)
    return r
