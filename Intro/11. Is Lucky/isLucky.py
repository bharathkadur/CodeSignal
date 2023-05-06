def solution(n):
    n = str(n)
    b = int(len(n)/2)
    c = n[:b]
    d = n[b:]
    c1,c2 = 0, 0
    for i in c:
        c1 = c1 + int(i)
    for i in d:
        c2 = c2 + int(i)
    if c1 == c2:
        return True
    else:
        return False
        

