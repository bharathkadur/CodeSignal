def solution(names):
    file_count = {}
    result = []
    
    for name in names:
        if name in file_count:
            count = file_count[name]
            new_name = f"{name}({count})"
            while new_name in file_count:
                count += 1
                new_name = f"{name}({count})"
            file_count[name] = count + 1
            file_count[new_name] = 1
            result.append(new_name)
        else:
            file_count[name] = 1
            result.append(name)
    
    return result
