def solution(s):
    a = []
    count = 0
    for i in s:
        if i not in a:
            count = count + 1
            a.append(i)      
    return count
