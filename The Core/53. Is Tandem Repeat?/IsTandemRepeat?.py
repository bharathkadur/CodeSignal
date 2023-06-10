def solution(inputString):
    size = len(inputString)
    if inputString[0:size//2] == inputString[size//2:]:
        return True
    else:
        return False
