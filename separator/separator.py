def separator(ls):
    e = [i for i in ls if i % 2 == 0]
    o = [i for i in ls if i % 2 == 1]
    return (e, o)
    