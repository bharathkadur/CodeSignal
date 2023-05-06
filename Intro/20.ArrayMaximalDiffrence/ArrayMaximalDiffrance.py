def solution(inputArray):
    max1 = 0
    for i in range(len(inputArray)-1):
        if abs(inputArray[i] - inputArray[i+1]) > max1:
            max1 = abs(inputArray[i] - inputArray[i+1])
    return max1 
