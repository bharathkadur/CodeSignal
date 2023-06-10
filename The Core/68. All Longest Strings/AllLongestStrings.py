def solution(inputArray):
    len1 = 0
    for i in inputArray:
        a = len(i)
        if a > len1:
            len1 = a
    b = []
    for i in inputArray:
        a = len(i)
        if a == len1:
            b.append(i)
    return b
