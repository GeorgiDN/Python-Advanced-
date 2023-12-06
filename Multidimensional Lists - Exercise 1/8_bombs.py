matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

for bomb in bombs:
    row, column = [int(x) for x in bomb.split(",")]
    if matrix[row][column] > 0:
        bomb_strength = matrix[row][column]
        for explosion_row in range(row - 1, row + 2):
            for explosion_col in range(column - 1, column + 2):
                if explosion_row in range(matrix_size) and explosion_col in range(matrix_size):
                    if matrix[explosion_row][explosion_col] > 0:
                        matrix[explosion_row][explosion_col] -= bomb_strength
        matrix[row][column] = 0

alives = []
for row in matrix:
    for col in row:
        if col > 0:
            alives.append(col)

print(f"Alive cells: {len(alives)}")
print(f"Sum: {sum(alives)}")

for row in matrix:
    print(" ".join(str(x) for x in row))





#
# def explosion(bomb_row, bomb_column):
#     bomb_strength = matrix[bomb_row][bomb_column]
#     for explosion_row in range(bomb_row - 1, bomb_row + 2):
#         for explosion_col in range(bomb_column - 1, bomb_column + 2):
#             if explosion_row in range(matrix_size) and explosion_col in range(matrix_size):
#                 if matrix[explosion_row][explosion_col] > 0:
#                     matrix[explosion_row][explosion_col] -= bomb_strength
#     matrix[bomb_row][bomb_column] = 0


# matrix_size = int(input())
# matrix = []

# for _ in range(matrix_size):
#     matrix.append([int(x) for x in input().split()])

# bombs = input().split()

# for bomb in bombs:
#     row, column = [int(x) for x in bomb.split(",")]
#     if matrix[row][column] > 0:
#         explosion(row, column)

# alive_cells = []
# for row in matrix:
#     for col in row:
#         if col > 0:
#             alive_cells.append(col)

# print(f"Alive cells: {len(alive_cells)}")
# print(f"Sum: {sum(alive_cells)}")

# for row in matrix:
#     print(" ".join(str(x) for x in row))
  
