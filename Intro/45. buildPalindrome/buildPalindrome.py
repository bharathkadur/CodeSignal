def solution(st):
    if st == st[::-1]:  
        return st
    index = 0
    subStr = st[index:]
    while subStr != subStr[::-1]: 
        index += 1
        subStr = st[index:]
    return st + st[index - 1::-1]
