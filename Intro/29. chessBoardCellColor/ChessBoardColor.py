def solution(cell1, cell2):
    row1, col1 = ord(cell1[0]) - ord('A') + 1, int(cell1[1])
    row2, col2 = ord(cell2[0]) - ord('A') + 1, int(cell2[1])

    sum1 = row1 + col1
    sum2 = row2 + col2
   
    is_even1 = sum1 % 2 == 0
    is_even2 = sum2 % 2 == 0
    
    return is_even1 == is_even2
