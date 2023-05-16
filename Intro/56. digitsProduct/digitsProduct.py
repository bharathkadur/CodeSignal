def solution(product):
    if product == 0:
        return 10  
    if product == 1:
        return 1   
    result = ""
    for digit in range(9, 1, -1):
        while product % digit == 0:
            result = str(digit) + result
            product //= digit
    if product != 1:
        return -1  
    return int(result) if result else -1
