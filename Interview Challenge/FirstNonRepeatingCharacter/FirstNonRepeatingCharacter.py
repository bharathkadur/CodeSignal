def solution(s):
    count = {}
    seen = set()
    for char in s:
        if char in count:
            count[char] += 1
            seen.add(char)
        else:
            count[char] = 1
    for char in s:
        if count[char] == 1 and char not in seen:
            return char
    return "_"
