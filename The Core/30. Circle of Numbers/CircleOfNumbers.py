def solution(n, firstNumber):
    a = n/2
    b = firstNumber + a
    if b < n:
        return b
    else:
        return b - n

