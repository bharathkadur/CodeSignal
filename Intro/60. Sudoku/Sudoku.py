def is_valid(numbers):
    seen = set()
    for num in numbers:
        if num in seen or num < 1 or num > 9:
            return False
        seen.add(num)
    return True

def get_subgrid(grid, start_row, start_col):
    subgrid = []
    for i in range(3):
        for j in range(3):
            subgrid.append(grid[start_row + i][start_col + j])
    return subgrid

def solution(grid):
    for row in grid:
        if not is_valid(row):
            return False

    for col in range(9):
        column = [grid[i][col] for i in range(9)]
        if not is_valid(column):
            return False

    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            subgrid = get_subgrid(grid, start_row, start_col)
            if not is_valid(subgrid):
                return False

    return True
