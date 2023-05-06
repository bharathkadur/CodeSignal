def solution(picture):
    for i in range(len(picture)):
        a = '*' + picture[i] + '*'
        picture[i] = a
    b=''
    for i in range(0,len(picture[0])):
        b=b+'*'
    picture.insert(0,b)
    picture.append(b)
    return(picture)
    

