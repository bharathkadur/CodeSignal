def solution(inputArray):
    c = 0
    for i in inputArray:
        if i == 0:
            break
        else:
            c += i
    return c
