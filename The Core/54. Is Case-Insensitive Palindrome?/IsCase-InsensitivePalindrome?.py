def solution(inputString):
    inputString = inputString.lower()
    size = len(inputString)
    temp = 1
    for i in range(size//2):
        if inputString[i] == inputString[-i-1]:
            temp *= 1
        else:
            temp *= 0

    if temp == 0:
        return False
    else:
        return True
