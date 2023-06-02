def solution(value):
    digit = 1
    if value < 10:
        return value
    if value%pow(10,digit)>=5:
        value += pow(10,digit)
    value -= (value%pow(10,digit))
    digit += 1
    
    while value>pow(10,digit):
        if (value%pow(10,digit)) >= 5*pow(10,digit-1):
            value += pow(10,digit)
        if value>=pow(10,digit):
            value -= (value%pow(10,digit))
        digit += 1
        
    return value
