def solution(inputArray, k):
    if k > len(inputArray):
        return 0
    window_sum = sum(inputArray[:k]) 
    max_sum = window_sum
    for i in range(k, len(inputArray)):
        window_sum += inputArray[i] - inputArray[i - k] 
        max_sum = max(max_sum, window_sum) 

    return max_sum
