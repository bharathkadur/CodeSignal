def solution(noun):
    i = noun[0].upper()
    for j in range(1, len(noun)):
        i += noun[j].lower()
    return i
