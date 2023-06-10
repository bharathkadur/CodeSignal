def solution(startTag):
    j = ""
    for i in startTag:
        if i == " ":
            break
        elif i == "<":
            pass
        elif i == ">":
            break
        else:
            j += i
    j = "</" + j + ">"
    return j
