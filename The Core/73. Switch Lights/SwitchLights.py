def solution(a):
    for i in range(0,len(a)):
        if a[i]==1:
            for j in range(0,i+1):
                if a[j] == 1:
                    a[j] = 0
                else:
                    a[j] = 1
    
    return a
