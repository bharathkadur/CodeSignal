def solution(statues):
    statues.sort()
    a = statues[0]
    b = statues[len(statues) - 1]
    c = []
    for i in range(a, b + 1):
        c.append(i)
    return len(c) - len(statues)
