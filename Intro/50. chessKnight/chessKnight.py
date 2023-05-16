def solution(cell):
    # Convert the position to coordinates
    x = ord(cell[0]) - ord('a') + 1
    y = int(cell[1])

    # Define the possible moves
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]

    # Count the number of valid moves
    count = 0
    for move in moves:
        new_x = x + move[0]
        new_y = y + move[1]
        if 1 <= new_x <= 8 and 1 <= new_y <= 8:
            count += 1

    return count
