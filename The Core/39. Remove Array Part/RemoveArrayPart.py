def solution(inputArray, l, r):
    a = []
    for i in range(0,l):
        a.append(inputArray[i])
    for j in range(r+1, len(inputArray)):
        a.append(inputArray[j])
    return a
