def solution(inputString):
    odd_chars = set()
    for char in inputString:
        if char in odd_chars:
            odd_chars.remove(char)
        else:
            odd_chars.add(char)
    return len(odd_chars) <= 1
