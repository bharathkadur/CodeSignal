def solution(grid):
    if len(grid) != 9:
        return False
    for i in range(len(grid)):
        if len(grid[i]) != 9:
            return False
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for k in range(j + 1, len(grid[i])):
                if grid[i][j].isnumeric() and grid[i][k].isnumeric() and grid[i][j] == grid[i][k]:
                    return False
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[j][i].isnumeric():
                for k in range(j+1, len(grid)):
                    if grid[k][i].isnumeric() and grid[j][i] == grid[k][i]:
                        return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            subgrid = [x for x in subgrid if x.isnumeric()]
            if len(subgrid) != len(set(subgrid)):
                return False
    
    return True
