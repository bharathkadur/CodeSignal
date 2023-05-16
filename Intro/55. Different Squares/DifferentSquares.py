def solution(matrix):
    count = 0
    squares = set()
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows - 1):
        for j in range(cols - 1):
            square = tuple(matrix[i][j:j+2] + matrix[i+1][j:j+2])
            if square not in squares:
                squares.add(square)
                count += 1
    
    return count
