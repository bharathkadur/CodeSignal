def solution(score1, score2):
    mini = min(score1, score2)
    maxi = max(score1, score2)

    if maxi == 6 and mini < 5:
        return True
    elif maxi == 7 and (mini == 5 or mini == 6):
        return True

    return False
