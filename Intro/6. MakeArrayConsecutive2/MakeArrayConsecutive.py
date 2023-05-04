def solution(statues):
    statues.sort()
    count = 0
    for i in range(len(statues)-1):
        if statues[i+1] - statues[i] != 0 and 1:
            count = count + statues[i+1] - statues[i] - 1
    return count
    
