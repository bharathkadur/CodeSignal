def solution(upSpeed, downSpeed, desiredHeight):
    days = 0
    height = 0
    while(height <= desiredHeight):
        height = height + upSpeed
        days= days + 1
        if height >= desiredHeight:
            return days
        height = height - downSpeed
        
    return days

