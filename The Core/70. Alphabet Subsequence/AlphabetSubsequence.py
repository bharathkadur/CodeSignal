def solution(s):
    char_set = set()
    for char in s:
            if char in char_set:
                return False
            char_set.add(char)

    sorted_string = ''.join(sorted(s))
    if s == sorted_string:
        return True
    else:
        return False
