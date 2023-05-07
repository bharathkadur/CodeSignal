def solution(a, b):
    if b<a:
        return True
    
    if (b-a)%2 ==0:
        return False
    else:
        return True

