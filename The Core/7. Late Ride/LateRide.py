def solution(n):
    hours = n // 60
    minutes = n % 60
    sum1 = 0
    for i in str(hours): 
        sum1 += int(i)
    for i in str(minutes): 
        sum1 += int(i)
    return sum1
