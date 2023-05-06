def solution(min1, min2_10, min11, s):
    a = 0
    minutes = 0
    while s >= a:
        minutes += 1
        if minutes == 1:
            a += min1
        elif 2 <= minutes <= 10:
            a += min2_10
        else:
            a += min11
    return minutes - 1
