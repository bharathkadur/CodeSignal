import re
def solution(inputString):
    pattern = r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}$'
    match = re.match(pattern, inputString)
    if match:
        return True
    else:
        return False
