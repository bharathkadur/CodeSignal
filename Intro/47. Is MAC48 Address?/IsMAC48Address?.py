import re

def solution(inputString):
    pattern = r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}$'
    return bool(re.match(pattern, inputString))

