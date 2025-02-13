def is_valid_index(idx, value):
    return 0 <= idx < value


def fill_matrix_and_takes_pos(pl_row, pl_col, rows, player):
    matrix = []
    for idx in range(rows):
        row = input().split()
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


def decrease_units(units_left, decrease_sum):
    units_left -= decrease_sum
    return units_left


def refuel(units_left, refuel_sum, max_units):
    units_left = min(units_left + refuel_sum, max_units)
    return units_left


def main():
    rows = int(input())
    pl_row, pl_col = 0, 0
    player, empty, meteorite, planet_b, resources = 'S', '.', 'M', 'P', 'R'
    matrix, pl_row, pl_col = (
        fill_matrix_and_takes_pos(pl_row, pl_col, rows, player))
    refuel_sum, decrease_sum = 10, 5
    max_units = 100
    units_left = 100
    matrix[pl_row][pl_col] = empty

    while True:

        if units_left == 0:
            matrix[pl_row][pl_col] = player
            print('Mission failed! The spaceship was stranded in space.')
            break

        direction = input()

        next_row, next_col = next_move(pl_row, pl_col, direction, rows)
        units_left = decrease_units(units_left, decrease_sum)

        if next_row is None or next_col is None:
            matrix[pl_row][pl_col] = player
            print('Mission failed! The spaceship was lost in space.')
            break

        if matrix[next_row][next_col] == resources:
            units_left = refuel(units_left, refuel_sum, max_units)

        if matrix[next_row][next_col] == meteorite:
            units_left = decrease_units(units_left, decrease_sum)

        if matrix[next_row][next_col] == planet_b:
            print(f'Mission accomplished! The spaceship reached Planet B with {units_left} resources left.')
            break

        if matrix[next_row][next_col] != resources:
            matrix[next_row][next_col] = empty
        pl_row, pl_col = next_row, next_col

    for row in matrix:
        print(' '.join(row))


if __name__ == '__main__':
    main()



##########################################################################################################
# def is_valid_index(idx, value):
#     return 0 <= idx < value
#
#
# def fill_matrix_and_takes_pos(pl_row, pl_col, rows, player):
#     matrix = []
#     for idx in range(rows):
#         row = input().split()
#         matrix.append(row)
#         if player in row:
#             pl_row = idx
#             pl_col = row.index(player)
#
#     return matrix, pl_row, pl_col
#
#
# def next_move(pl_row, pl_col, direction, rows):
#     moves = {
#         'up': (-1, 0),
#         'down': (1, 0),
#         'left': (0, -1),
#         'right': (0, 1)
#     }
#     d_row, d_col = moves[direction][0], moves[direction][1]
#     next_row = (pl_row + d_row) if is_valid_index(pl_row + d_row, rows) else None
#     next_col = (pl_col + d_col) if is_valid_index(pl_col + d_col, rows) else None
#
#     return next_row, next_col
#
#
# def main():
#     rows = int(input())
#     pl_row, pl_col = 0, 0
#     player, empty, meteorite, planet_b, resources_station = 'S', '.', 'M', 'P', 'R'
#     max_resources = 100
#     resources_units = 100
#     refuel_sum = 10
#
#     matrix, pl_row, pl_col = (
#         fill_matrix_and_takes_pos(pl_row, pl_col, rows, player))
#
#     while True:
#
#         if resources_units < 5:
#             print('Mission failed! The spaceship was stranded in space.')
#             matrix[pl_row][pl_col] = player
#             break
#
#         direction = input()
#
#         next_row, next_col = next_move(pl_row, pl_col, direction, rows)
#         resources_units -= 5
#
#         if next_row is None or next_col is None:
#             print('Mission failed! The spaceship was lost in space.')
#             matrix[pl_row][pl_col] = player
#             break
#
#         elif matrix[next_row][next_col] == resources_station:  # R
#             resources_units = min(resources_units + refuel_sum, max_resources)
#             pl_row, pl_col = next_row, next_col
#             continue
#
#         elif matrix[next_row][next_col] == meteorite:
#             resources_units -= 5
#
#         elif matrix[next_row][next_col] == planet_b:
#             print(f'Mission accomplished! The spaceship reached Planet B with {resources_units} resources left.')
#             break
#
#         if matrix[pl_row][pl_col] != resources_station:
#             matrix[pl_row][pl_col] = empty
#         pl_row, pl_col = next_row, next_col
#         matrix[pl_row][pl_col] = empty
#
#     for row in matrix:
#         print(' '.join(row))
#
#
# if __name__ == '__main__':
#     main()


#####################################################################################################################
# def is_valid_index(rows, idx):
#     return 0 <= idx < rows
#
#
# rows = int(input())
# grid = []
# s_row, s_col = 0, 0
# meteorite, planet_b, resources, empty = 'M', 'P', 'R', '.'
# units, max_units = 100, 100
#
# moves = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1)
# }
#
# for i in range(rows):
#     row = input().split()
#     grid.append(row)
#     if 'S' in row:
#         s_row, s_col = i, row.index('S')
#
# while True:
#     if units == 0:
#         print('Mission failed! The spaceship was stranded in space.')
#         grid[s_row][s_col] = 'S'
#         break
#
#     command = input()
#
#     next_row, next_col = s_row + moves[command][0], s_col + moves[command][1]
#     units -= 5
#
#     if not is_valid_index(rows, next_row) or not is_valid_index(rows, next_col):
#         grid[s_row][s_col] = 'S'
#         print('Mission failed! The spaceship was lost in space.')
#         break
#
#     elif grid[next_row][next_col] == meteorite:
#         units -= 5
#
#     elif grid[next_row][next_col] == resources:
#         units = min(units + 10, max_units)
#
#     elif grid[next_row][next_col] == planet_b:
#         print(f'Mission accomplished! The spaceship reached Planet B with {units} resources left.')
#         break
#
#     if not grid[s_row][s_col] == resources:
#         grid[s_row][s_col] = empty
#     if not grid[next_row][next_col] == resources:
#         grid[next_row][next_col] = empty
#     s_row, s_col = next_row, next_col
#
# for row in grid:
#     print(' '.join(row))


############################################################################################################################
# rows, meteorite, planet_b, resources, empty, recourses_units, max_units = int(input()), 'M', 'P', 'R', '.', 100, 100
# moves, grid = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}, [input().split() for _ in range(rows)]
# s_row, s_col = next((i, row.index('S')) for i, row in enumerate(grid) if 'S' in row)
# while True:
#     if recourses_units == 0:
#         print('Mission failed! The spaceship was stranded in space.')
#         grid[s_row][s_col] = 'S'
#         break
#     command = input()
#     next_row, next_col = s_row + moves[command][0], s_col + moves[command][1]
#     recourses_units -= 5
#     if not 0 <= next_row < rows or not 0 <= next_col < rows:
#         grid[s_row][s_col] = 'S'
#         print('Mission failed! The spaceship was lost in space.')
#         break
#     elif grid[next_row][next_col] == meteorite:recourses_units -= 5
#     elif grid[next_row][next_col] == resources:recourses_units = min(recourses_units + 10, max_units)
#     elif grid[next_row][next_col] == planet_b:
#         print(f'Mission accomplished! The spaceship reached Planet B with {recourses_units} resources left.')
#         break
#     if not grid[s_row][s_col] == resources:grid[s_row][s_col] = empty
#     if not grid[next_row][next_col] == resources:grid[next_row][next_col] = empty
#     s_row, s_col = next_row, next_col
# [print(' '.join(row)) for row in grid]
