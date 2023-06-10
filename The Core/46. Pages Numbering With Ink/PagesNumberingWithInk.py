def solution(current, numberOfDigits):
    
    while numberOfDigits>=0:
        numberOfDigits -= int(math.ceil(math.log(current+1,10)))
        current += 1
    
    return (current-2)
