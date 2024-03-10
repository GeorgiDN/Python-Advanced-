def fill_the_matrix_and_find_bunny(mtrx_size, b_row, b_col):
    matrix = []
    for row in range(mtrx_size):
        curr_row = [x if x in ["X", "B"] else int(x) for x in input().split()]
        matrix.append(curr_row)
        if "B" in curr_row:
            b_row = row
            b_col = curr_row.index("B")
    return matrix, b_row, b_col


def check_up(matrix, b_row, b_col):
    bunny_positions = []
    number_of_egs = 0
    for i in range(b_row - 1, -1, -1):
        current_egg = matrix[i][b_col]
        if current_egg == "X":
            break
        number_of_egs += current_egg
        bunny_positions.append([i, b_col])

    return bunny_positions, number_of_egs


def check_down(matrix, b_row, b_col, mtrx_size):
    bunny_positions = []
    number_of_egs = 0
    for i in range(b_row + 1, mtrx_size):
        current_egg = matrix[i][b_col]
        if current_egg == "X":
            break
        number_of_egs += current_egg
        bunny_positions.append([i, b_col])

    return bunny_positions, number_of_egs


def check_left(matrix, b_row, b_col):
    bunny_positions = []
    number_of_egs = 0
    for i in range(b_col - 1, -1, -1):
        current_egg = matrix[b_row][i]
        if current_egg == "X":
            break
        number_of_egs += current_egg
        bunny_positions.append([b_row, i])

    return bunny_positions, number_of_egs


def check_right(matrix, b_row, b_col, mtrx_size):
    bunny_positions = []
    number_of_egs = 0
    for i in range(b_col + 1, mtrx_size):
        current_egg = matrix[b_row][i]
        if current_egg == "X":
            break
        number_of_egs += current_egg
        bunny_positions.append([b_row, i])

    return bunny_positions, number_of_egs


size = int(input())
bunny_row, bunny_column = 0, 0
field, bunny_row, bunny_column = fill_the_matrix_and_find_bunny(size, bunny_row, bunny_column)
best_direction = ''
best_path = []
max_number_of_eggs = 0
directions = ["up", "down", "left", "right"]

current_path = []
collected_eggs = 0


for direction in directions:
    if direction == "up":
        current_path, collected_eggs = check_up(field, bunny_row, bunny_column)
    elif direction == "down":
        current_path, collected_eggs = check_down(field, bunny_row, bunny_column, size)
    elif direction == "left":
        current_path, collected_eggs = check_left(field, bunny_row, bunny_column)
    elif direction == "right":
        current_path, collected_eggs = check_right(field, bunny_row, bunny_column, size)

    if collected_eggs >= max_number_of_eggs:
        max_number_of_eggs = collected_eggs
        best_path = current_path
        best_direction = direction

print(best_direction)
for r in best_path:
    print(r)
# [print(r) for r in best_path]
print(max_number_of_eggs)
