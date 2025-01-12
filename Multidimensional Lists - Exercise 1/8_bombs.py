def is_valid_idx(matrix, value):
    return 0 <= value < len(matrix)


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
bomb_indexes = [list(map(int, x.split(','))) for x in input().split()]

directions = [
    (-1, -1), (-1, 0), (-1, 1),  # up-left, up, up-right
    (0, -1), (0, 1),  # left, right
    (1, -1), (1, 0), (1, 1)  # down-left, down, down-right
]

for row, col in bomb_indexes:
    if matrix[row][col] > 0:
        bomb_strength = matrix[row][col]
        for d_row, d_col in directions:
            n_row, n_col = row + d_row, col + d_col
            if is_valid_idx(matrix, n_row) and is_valid_idx(matrix, n_col) and matrix[n_row][n_col] > 0:
                matrix[n_row][n_col] -= bomb_strength
        matrix[row][col] = 0

alive_cells = [cell for row in matrix for cell in row if cell > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(' '.join(map(str, row))) for row in matrix]



# def is_valid_index(idx, number):
#     return 0 <= idx < number


# def explosion(mtrx, rows, b_row, bomb_col):
#     bomb_strength = mtrx[b_row][bomb_col]
#     for explosion_row in range(b_row - 1, b_row + 2):
#         for explosion_col in range(bomb_col - 1, bomb_col + 2):
#             if is_valid_index(explosion_row, rows) and is_valid_index(explosion_col, rows):
#                 if mtrx[explosion_row][explosion_col] > 0:
#                     mtrx[explosion_row][explosion_col] -= bomb_strength
#     mtrx[b_row][bomb_col] = 0
#     return mtrx


# def check_for_alive_cells(mtrx):
#     alive_cells_number = len([col for row in mtrx for col in row if col > 0])
#     alive_cells_sum = sum([col for row in mtrx for col in row if col > 0])
#     return alive_cells_number, alive_cells_sum


# def print_matrix(mtrx, alive_cells_number, alive_cells_sum):
#     print(f"Alive cells: {alive_cells_number}\n"
#           f"Sum: {alive_cells_sum}")

#     [print(' '.join(map(str, element))) for element in mtrx]


# def main():
#     size = int(input())
#     matrix = [[int(x) for x in input().split()] for _ in range(size)]
#     bombs = input().split()

#     for bomb in bombs:
#         curr_bomb = bomb.split(",")
#         bomb_row, bomb_column = int(curr_bomb[0]), int(curr_bomb[1])
#         if matrix[bomb_row][bomb_column] > 0:
#             matrix = explosion(matrix, size, bomb_row, bomb_column)

#     alive_cells, sum_alive_cells = check_for_alive_cells(matrix)
#     print_matrix(matrix, alive_cells, sum_alive_cells)


# if __name__ == "__main__":
#     main()




# matrix_size = int(input())
# matrix = []

# for _ in range(matrix_size):
#     matrix.append([int(x) for x in input().split()])

# bombs = input().split()

# for bomb in bombs:
#     row, column = [int(x) for x in bomb.split(",")]
#     if matrix[row][column] > 0:
#         bomb_strength = matrix[row][column]
#         for explosion_row in range(row - 1, row + 2):
#             for explosion_col in range(column - 1, column + 2):
#                 if explosion_row in range(matrix_size) and explosion_col in range(matrix_size):
#                     if matrix[explosion_row][explosion_col] > 0:
#                         matrix[explosion_row][explosion_col] -= bomb_strength
#         matrix[row][column] = 0

# alives = []
# for row in matrix:
#     for col in row:
#         if col > 0:
#             alives.append(col)

# print(f"Alive cells: {len(alives)}")
# print(f"Sum: {sum(alives)}")

# for row in matrix:
#     print(" ".join(str(x) for x in row))



