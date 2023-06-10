def solution(coins, price):
    i = -1
    numCoins = 0
    while price>0 and abs(i)<=len(coins):
        if price >= coins[i]:
            price -= coins[i]
            numCoins += 1
        else:
            i -= 1
    
    return numCoins
