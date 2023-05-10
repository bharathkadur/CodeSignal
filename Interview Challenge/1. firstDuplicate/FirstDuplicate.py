def solution(a):
    b = set()
    c = {}
    for i, x in enumerate(a):
        if x not in b:
            b.add(x)
        else:
            if x not in c:
                c[x] = i
    if c:
        min_key = min(c, key=c.get)
        return min_key
    else:
        return -1
