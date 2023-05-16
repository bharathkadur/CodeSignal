def solution(inputString):
    long_prefix = ""
    cur_prefix = ""
    
    for i in inputString:
        if i.isdigit():
            cur_prefix += i
        else:
            break
        
        if len(cur_prefix) > len(long_prefix):
            long_prefix = cur_prefix
    
    return long_prefix
