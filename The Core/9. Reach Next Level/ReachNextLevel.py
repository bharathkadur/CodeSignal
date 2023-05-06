def solution(experience, threshold, reward):
    a = experience + reward
    if a >= threshold:
        return True
    return False
