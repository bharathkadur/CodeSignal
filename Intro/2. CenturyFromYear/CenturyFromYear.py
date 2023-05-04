def solution(year):
    if (year <= 0):
        return None
    elif(year <= 100):
        return 1
    elif(year % 100 == 0):
        return (year // 100)
    else:
        return year // 100 + 1
    
        

