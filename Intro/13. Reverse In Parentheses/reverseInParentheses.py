def solution(inputString):
    stack = []
    current_str = ''
    for c in inputString:
        if c == '(':
            stack.append(current_str)
            current_str = ''
        elif c == ')':
            current_str = stack.pop() + current_str[::-1]
        else:
            current_str += c
    return current_str
