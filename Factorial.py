def fact(a):
    res = 1
    for i in range(0, a):
        res = res * (a - i)
    return res


