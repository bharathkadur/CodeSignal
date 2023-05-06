def solution(matrix):
    total_sum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                for i in range(row, len(matrix)):
                    matrix[i][col] = -1
            elif matrix[row][col] >= 1:
                if matrix[row - 1][col] != -1:
                    total_sum += matrix[row][col]
    return total_sum
