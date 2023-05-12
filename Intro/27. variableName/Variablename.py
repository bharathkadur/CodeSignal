def solution(name):
    if name[0].isdigit() or name[0] == " ":
        return False
    for i in range(0, len(name)):
        if not(name[i].isalpha() or name[i].isdigit() or name[i] == "_"):
            return False
    return True
