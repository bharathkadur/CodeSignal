def solution(n):
    x = n.split(".")
    if len(x) != 4:
        return False
    for i in x:
        if not i.isdigit():
            return False
        num = int(i)
        if num < 0 or num > 255 or (len(i) > 1 and i[0] == '0'):
            return False
    return True
