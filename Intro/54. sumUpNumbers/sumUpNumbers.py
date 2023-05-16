import re

def solution(inputString):
    numbers = re.findall(r'\d+', inputString)
    b = 0
    for num in numbers:
        b += int(num)
    return b
