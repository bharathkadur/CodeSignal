def solution(candlesNumber, makeNew):
    totalCandlesBurned = 0
    leftovers = 0
    
    while candlesNumber > 0:
        totalCandlesBurned += candlesNumber
        leftovers += candlesNumber
        candlesNumber = leftovers // makeNew
        leftovers %= makeNew
    
    return totalCandlesBurned
