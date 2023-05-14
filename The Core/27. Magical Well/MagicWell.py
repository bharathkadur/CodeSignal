def solution(a, b, n):
    count = 0
    for i in range(0,n):
        count = count + (a * b)
        a = a+1
        b = b+1
    return count
        

