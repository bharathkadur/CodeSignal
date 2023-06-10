def solution(a):
    total_sum = sum(a)
    if total_sum % 3 != 0:
        return 0

    goal = total_sum // 3
    ways = 0
    count = 0
    cum_sum = 0

    for i in range(len(a) - 1):
        cum_sum += a[i]
        if cum_sum == 2 * goal:
            ways += count
        if cum_sum == goal:
            count += 1

    return ways
