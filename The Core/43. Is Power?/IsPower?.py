def solution(n):
    for a in range(0,int(pow(n,.5))+1):
        for b in range(0,int(math.log(n,2))+1):
            if pow(a,b) == n:
                return True
    
    return False
