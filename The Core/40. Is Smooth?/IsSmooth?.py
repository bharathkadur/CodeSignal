def solution(arr):
    if arr[0] == arr[len(arr) - 1]:
        if len(arr) % 2 == 0:
            a = int(len(arr) / 2)
            b = (arr[a] + arr[a-1])
            if b == arr[0]:
                return True
            else:
                return False
        else:
            a = int(len(arr)) // 2
            b = arr[a]
            if b == arr[0]:
                return True
            else:
                return False
    else:
        return False
