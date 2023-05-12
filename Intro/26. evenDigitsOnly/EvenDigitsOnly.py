def solution(a):
    while a > 0:
        b = a % 10
        if b % 2 != 0:
            return False
        a = a - b
        a = a/10
    return True
