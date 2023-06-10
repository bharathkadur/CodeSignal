def solution(votes, k):
    a = max(votes)
    c = 0
    if k == 0:
        s = 0
        for i in votes:
            if i == a:
                s += 1
        if s > 1:
            return 0
        return 1
    for i in votes:
        if i + k > a:
            c += 1
    return c
