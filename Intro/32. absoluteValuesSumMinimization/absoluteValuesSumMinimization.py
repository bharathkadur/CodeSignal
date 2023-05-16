def solution(a):
    min_number = 0
    min_sum = 2147483648
    for i in a:
        Sum = 0
        for j in a:
            Sum += abs(j-i)
        if Sum < min_sum:
            min_sum = Sum
            min_number = i
    return min_number
