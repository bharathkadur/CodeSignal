def solution(n):
    degree = 0

    while n >= 10:
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        n = digit_sum
        degree += 1

    return degree
