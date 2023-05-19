def solution(k):
    c = 0
    d = 0
    for i in range(1,k+1):
        if i % 2 == 0:
            c = c + i * i
        else:
            d = d + i * i
    return c - d
