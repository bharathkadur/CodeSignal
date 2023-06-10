def solution(a0):
    a = []
    a.append(a0)
    
    index = 2
    temp = 0
    while a0:
        temp += pow((a0%10),2)
        a0 //= 10
    
    while temp not in a:
        index += 1
        a.append(temp)
        a0 = temp
        temp = 0
        while a0:
            temp += pow((a0%10),2)
            a0 //= 10
    
    return index
