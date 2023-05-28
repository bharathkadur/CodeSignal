def solution(commands):
    n = 4  # Assuming there are 4 students
    directions = [0] * n  # Initialize directions of students
    same_direction_count = 0

    for command in commands:
        for i in range(n):
            if i == 1:  # Assuming the second student can't tell left from right
                if command == 'L':
                    directions[i] = (directions[i] + 1) % 4
                elif command == 'R':
                    directions[i] = (directions[i] - 1) % 4
                elif command == 'A':
                    directions[i] = (directions[i] + 2) % 4
            else:
                if command == 'L':
                    directions[i] = (directions[i] - 1) % 4
                elif command == 'R':
                    directions[i] = (directions[i] + 1) % 4
                elif command == 'A':
                    directions[i] = (directions[i] + 2) % 4

        if len(set(directions)) == 1:
            same_direction_count += 1

    return same_direction_count
