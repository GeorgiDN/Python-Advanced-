def is_valid_index(n_size, idx):
    return 0 <= idx < n_size


def next_move(n_size, curr_row, curr_col, line):
    all_directions = {"up": [curr_row - 1, curr_col],
                      "down": [curr_row + 1, curr_col],
                      "right": [curr_row, curr_col + 1],
                      "left": [curr_row, curr_col - 1]}

    new_row, new_col = all_directions[line][0], all_directions[line][1]
    if is_valid_index(n_size, new_row) \
            and is_valid_index(n_size, new_col):
        return new_row, new_col
    return None, None


def fill_the_matrix_and_take_positions(n, t_row, t_col):
    matrix = []
    for r in range(n):
        row = list(input())
        matrix.append(row)
        if "P" in row:
            t_row = r
            t_col = row.index("P")
    return matrix, t_row, t_col


def print_result(matrix, traveler_dead, left_maze, t_health):
    print("Player is dead. Maze over!") \
        if traveler_dead else print("Player escaped the maze. Danger passed!")

    print(f"Player's health: {t_health} units")
    [print("".join(element)) for element in matrix]


def main():
    size = int(input())
    MAX_HEALTH = 100
    traveler_health = MAX_HEALTH
    traveler_is_dead = False
    traveler_left_maze = False
    traveler_row, traveler_col = 0, 0
    maze, traveler_row, traveler_col, = (
        fill_the_matrix_and_take_positions(size, traveler_row, traveler_col))

    while True:
        if traveler_is_dead or traveler_left_maze:
            break

        command = input()
        next_row, next_col = next_move(size, traveler_row, traveler_col, command)
        if next_row is None or next_col is None:
            continue

        elif maze[next_row][next_col] == "X":
            traveler_left_maze = True

        elif maze[next_row][next_col] == "M":
            traveler_health -= 40
            if traveler_health <= 0:
                traveler_health = 0
                traveler_is_dead = True

        elif maze[next_row][next_col] == "H":
            traveler_health = min(traveler_health + 15, MAX_HEALTH)

        maze[traveler_row][traveler_col] = "-"
        traveler_row, traveler_col = next_row, next_col
        maze[traveler_row][traveler_col] = "P"  #  where is Traveler

    print_result(maze, traveler_is_dead, traveler_left_maze, traveler_health)


if __name__ == '__main__':
    main()
