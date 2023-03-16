from math import ceil


def calculator(n, m, li):
    ls = []
    for i in range(0, n, m):
        ls.append(sum(li[i:i+m]))
    return sum([ls[i]*((-1)**i) for i in range(len(ls))])
        