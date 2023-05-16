def solution(deposit, rate, threshold):
    count = 0
    amount  = deposit
    while(amount < threshold):
        a = (amount * rate * 1) / 100
        amount = amount + a
        count = count + 1
    return count 
        
    

