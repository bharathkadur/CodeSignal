def solution(n):
    matrix = [[0] * n for _ in range(n)]  # Initialize the square matrix with zeros
    num = 1  # Start from 1
    top_row, bottom_row = 0, n - 1
    left_col, right_col = 0, n - 1

    while num <= n * n:
        # Traverse top row from left to right
        for i in range(left_col, right_col + 1):
            matrix[top_row][i] = num
            num += 1
        top_row += 1

        # Traverse right column from top to bottom
        for i in range(top_row, bottom_row + 1):
            matrix[i][right_col] = num
            num += 1
        right_col -= 1

        # Traverse bottom row from right to left
        for i in range(right_col, left_col - 1, -1):
            matrix[bottom_row][i] = num
            num += 1
        bottom_row -= 1

        # Traverse left column from bottom to top
        for i in range(bottom_row, top_row - 1, -1):
            matrix[i][left_col] = num
            num += 1
        left_col += 1

    return matrix
