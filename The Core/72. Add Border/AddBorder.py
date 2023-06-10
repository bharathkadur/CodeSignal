def solution(picture):
    for i in range(0, len(picture)):
        picture[i] = "*" + picture[i] +"*"
        a = len(picture[i])
    b = ""
    for i in range(0,a):
        b += "*"
    picture.insert(0, b)
    picture.append(b)
    return picture
        

