def solution(n, l, r):
    count = 0
    while l <= r:
        if l + r == n:
            count += 1
            l += 1
            r -= 1
        elif l + r < n:
            l += 1
        else:
            r -= 1
    return count
