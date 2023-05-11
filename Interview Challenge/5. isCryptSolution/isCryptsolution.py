def solution(crypt, solution):
    d = {}
    a = []
    for i in range(len(solution)):
        d[solution[i][0]] = solution[i][1]

    for i in range(len(crypt)):
        if len(crypt[i]) > 1 and d[crypt[i][0]] == '0':
            return False
        b = ""
        for j in range(len(crypt[i])):
            b = b + d[crypt[i][j]]
        a.append(int(b))

    if a[0] + a[1] == a[2]:
        return True
    else:
        return False
