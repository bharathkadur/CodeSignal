def solution(legs):
    maxCat = legs//4
    output = []
    for i in range(0,maxCat+1):
        people = (legs-i*4)//2
        output.insert(0,people)
        
    return output
