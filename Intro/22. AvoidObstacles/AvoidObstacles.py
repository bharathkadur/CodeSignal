def solution(inputArray):
    inputArray.sort()
    jd = 1
    o_hit = True
    while(o_hit): 
        o_hit = False
        jd += 1
        for i in range(0, len(inputArray)):
            if inputArray[i] % jd == 0:
                o_hit = True
                break
    return jd 

