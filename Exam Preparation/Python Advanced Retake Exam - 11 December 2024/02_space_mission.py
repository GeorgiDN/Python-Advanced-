def is_valid_index(rows, idx):
    return 0 <= idx < rows


rows = int(input())
grid = []
s_row, s_col = 0, 0
meteorite, planet_b, resources, empty = 'M', 'P', 'R', '.'
units, max_units = 100, 100

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(rows):
    row = input().split()
    grid.append(row)
    if 'S' in row:
        s_row, s_col = i, row.index('S')

while True:
    if units == 0:
        print('Mission failed! The spaceship was stranded in space.')
        grid[s_row][s_col] = 'S'
        break

    command = input()

    next_row, next_col = s_row + moves[command][0], s_col + moves[command][1]
    units -= 5

    if not is_valid_index(rows, next_row) or not is_valid_index(rows, next_col):
        grid[s_row][s_col] = 'S'
        print('Mission failed! The spaceship was lost in space.')
        break

    elif grid[next_row][next_col] == meteorite:
        units -= 5

    elif grid[next_row][next_col] == resources:
        units = min(units + 10, max_units)

    elif grid[next_row][next_col] == planet_b:
        print(f'Mission accomplished! The spaceship reached Planet B with {units} resources left.')
        break

    if not grid[s_row][s_col] == resources:
        grid[s_row][s_col] = empty
    if not grid[next_row][next_col] == resources:
        grid[next_row][next_col] = empty
    s_row, s_col = next_row, next_col

for row in grid:
    print(' '.join(row))



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
