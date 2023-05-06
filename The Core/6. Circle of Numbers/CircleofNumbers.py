def solution(n, firstNumber):
    x = firstNumber % n
    return (n/2 + x) % n
