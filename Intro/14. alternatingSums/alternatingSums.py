def solution(a):
    c1 = 0
    c2 = 0
    for i in range(len(a)):
        if i % 2 == 0:
            c1 = c1 + a[i]
        else:
            c2 = c2 + a[i]
    b = [c1, c2]
    return b
            

