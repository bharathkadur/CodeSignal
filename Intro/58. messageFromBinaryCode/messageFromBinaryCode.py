def solution(code):
    result = ""
    for i in range(0, len(code), 8):
        binary = code[i:i+8]
        decimal = int(binary, 2)
        character = chr(decimal)
        result += character
    return result
