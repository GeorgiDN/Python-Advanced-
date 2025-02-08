def is_valid_index(idx, value):
    return 0 <= idx < value


def fill_matrix_and_takes_pos(pl_row, pl_col, rows, player):
    matrix = []
    for idx in range(rows):
        row = list(input())
        matrix.append(row)
        if player in row:
            pl_row = idx
            pl_col = row.index(player)

    return matrix, pl_row, pl_col


def next_move(pl_row, pl_col, direction, rows):
    moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    d_row, d_col = moves[direction][0], moves[direction][1]
    next_row = (pl_row + d_row) if is_valid_index(pl_row + d_row, rows) else None
    next_col = (pl_col + d_col) if is_valid_index(pl_col + d_col, rows) else None
    return next_row, next_col


def main():
    rows = int(input())
    pl_row, pl_col = 0, 0
    player, empty, _exit, monster, portion = 'P', '-', 'X', 'M', 'H'
    max_health = 100
    traveler_health = 100
    matrix, pl_row, pl_col = (
        fill_matrix_and_takes_pos(pl_row, pl_col, rows, player))
    exit_found = False

    while True:
        if traveler_health == 0:
            print('Player is dead. Maze over!')
            break
        elif exit_found:
            print('Player escaped the maze. Danger passed!')
            break

        direction = input()

        next_row, next_col = next_move(pl_row, pl_col, direction, rows)

        if next_row is None or next_col is None:
            continue

        if matrix[next_row][next_col] == monster:
            traveler_health = max(traveler_health - 40, 0)

        if matrix[next_row][next_col] == portion:
            traveler_health = min(traveler_health + 15, max_health)

        if matrix[next_row][next_col] == _exit:
            exit_found = True

        matrix[pl_row][pl_col] = empty
        pl_row, pl_col = next_row, next_col
        matrix[pl_row][pl_col] = player

    print(f"Player's health: {traveler_health} units")

    for row in matrix:
        print(''.join(row))


if __name__ == '__main__':
    main()


###################################################################################
# def is_valid_index(idx, size):
#     return 0 <= idx < size


# def next_move(rows, row, col, direction):
#     moves = {
#         "up": (-1, 0),
#         "down": (1, 0),
#         "left": (0, -1),
#         "right": (0, 1)
#     }

#     d_row, d_col = moves[direction]
#     row = (row + d_row)
#     col = (col + d_col)
#     if is_valid_index(row, rows) and is_valid_index(col, rows):
#         return row, col
#     return None, None


# def fill_the_matrix_and_take_positions(rows, t_row, t_col):
#     matrix = []
#     for idx in range(rows):
#         row = list(input())
#         matrix.append(row)
#         if "P" in row:
#             t_row = idx
#             t_col = row.index("P")
#     return matrix, t_row, t_col


# def print_result(matrix, traveler_dead, left_maze, t_health):
#     print("Player is dead. Maze over!") \
#         if traveler_dead else print("Player escaped the maze. Danger passed!")

#     print(f"Player's health: {t_health} units")
#     [print("".join(element)) for element in matrix]


# def main():
#     rows = int(input())
#     MAX_HEALTH = 100
#     traveler_health = MAX_HEALTH
#     traveler_is_dead = False
#     traveler_left_maze = False
#     traveler_row, traveler_col = 0, 0
#     maze, traveler_row, traveler_col, = (
#         fill_the_matrix_and_take_positions(rows, traveler_row, traveler_col))

#     while True:
#         if traveler_is_dead or traveler_left_maze:
#             break

#         command = input()
#         next_row, next_col = next_move(rows, traveler_row, traveler_col, command)
#         if next_row is None or next_col is None:
#             continue

#         elif maze[next_row][next_col] == "X":
#             traveler_left_maze = True

#         elif maze[next_row][next_col] == "M":
#             traveler_health -= 40
#             if traveler_health <= 0:
#                 traveler_health = 0
#                 traveler_is_dead = True

#         elif maze[next_row][next_col] == "H":
#             traveler_health = min(traveler_health + 15, MAX_HEALTH)

#         maze[traveler_row][traveler_col] = "-"
#         traveler_row, traveler_col = next_row, next_col
#         maze[traveler_row][traveler_col] = "P"

#     print_result(maze, traveler_is_dead, traveler_left_maze, traveler_health)


# if __name__ == '__main__':
#     main()
    
