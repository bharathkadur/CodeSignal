def solution(number, width):
    a = len(str(number))
    if width == a:
        return str(number)
    elif width < a:
        b = str(number)
        s = ""
        for i in range(a - 1, a - width - 1, -1):
            s = b[i] + s
        return s
    else:
        b = str(number)
        while len(b) != width:
            b = "0" + b
        return b
