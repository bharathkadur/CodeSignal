def solution(inputArray):
    n = len(inputArray)
    inc = [0] * n
    for i in range(1, n):
        if inputArray[i] <= inputArray[i-1]:
            diff = inputArray[i-1] - inputArray[i] + 1
            inc[i] = diff
            inputArray[i] += diff
    return sum(inc)
