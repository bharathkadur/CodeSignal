def solution(arr):
    if len(arr) % 2 == 0:
        a = []
        for i in range(0, int(len(arr)/2 - 1)):
            a.append(arr[i])
        b = int(len(arr)/2)
        c = arr[b] + arr[b-1]
        a.append(c)
        for i in range(b+1, len(arr)):
            a.append(arr[i])
        return a
    else:
        return arr
