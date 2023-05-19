def solution(param1, param2):
    if param1 > param2:
        a = str(param1)
        b = str(param2)
    else:
        a = str(param2)
        b = str(param1)
    c = len(a) - len(b)
    j = 0
    p = ""
    for i in range(c, len(a)):
        d = int(a[i]) + int(b[j])
        j += 1
        if d == 10:
            p += str(0)
        elif d > 10:
            p += str(d % 10)
        else:
            p += str(d)
    for i in range(0, c):
        p = a[i] + p
    return int(p)
