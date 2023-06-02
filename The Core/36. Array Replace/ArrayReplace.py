def solution(inputArray, elemToReplace, substitutionElem):
    for i in range(0, len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray
