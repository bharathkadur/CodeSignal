def solution(s1, s2):
    count = 0
    for i in s1:
        if i in s2:
            count= count + 1
            s2 = s2.replace(i,'',1)
    return count

