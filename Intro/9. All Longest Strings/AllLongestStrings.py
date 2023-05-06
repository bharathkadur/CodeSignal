def solution(inputArray):
    b = []
    d = []
    for i in range(len(inputArray)):
        b.append(len(inputArray[i]))
    for i  in range(len(b)):
        if b[i] == max(b):
            d.append(inputArray[i])
    return(d)
            
