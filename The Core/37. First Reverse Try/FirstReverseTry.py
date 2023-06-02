def solution(arr):
    a = len(arr)
    if a == 0 or a == 1:
        return arr
    else:
        j = len(arr) - 1
        arr[0], arr[j] = arr[j], arr[0]
    return arr
    
    
