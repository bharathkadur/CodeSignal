def solution(n):
    count = 0
    for i in range(1, n):
        Sum1 = 0
        for j in range(i, n):
            Sum1 += j
            if Sum1 == n:
                count += 1
                break
            elif Sum1 > n:
                break
    return count
