def is_valid_index(value, max_value):
    return 0 <= value < max_value


directions = [
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
]

rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]

knight_row, knight_col = 0, 0
removed_knights = 0

while True:
    max_possible_attacks = 0
    for row in range(rows):
        for col in range(rows):
            if matrix[row][col] == 'K':
                possible_attacks = 0
                for direction in directions:
                    d_row, d_col = direction[0], direction[1]
                    k_row, k_col = row + d_row, col + d_col
                    if is_valid_index(k_row, rows) and is_valid_index(k_col, rows):
                        if matrix[k_row][k_col] == 'K':
                            possible_attacks += 1

                if possible_attacks > max_possible_attacks:
                    max_possible_attacks = possible_attacks
                    knight_row, knight_col = row, col

    if max_possible_attacks == 0:
        break

    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)



########################################################################################################################
# directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
# rows, knight_row, knight_col, removed_knights = int(input()), 0, 0, 0
# matrix = [[x for x in input()] for _ in range(rows)]
# while True:
#     max_possible_attacks = 0
#     for row in range(rows):
#         for col in range(rows):
#             if matrix[row][col] == 'K':
#                 possible_attacks = 0
#                 for d_row, d_col in directions:
#                     if 0 <= d_row + row < rows and 0 <= d_col + col < rows and matrix[row + d_row][col + d_col] == 'K':
#                         possible_attacks += 1
#                 if possible_attacks > max_possible_attacks:
#                     max_possible_attacks, knight_row, knight_col = possible_attacks, row, col
#     if max_possible_attacks == 0:break
#     removed_knights, matrix[knight_row][knight_col] = removed_knights + 1, "0"
# print(removed_knights)



########################################################################################################################
# def is_valid_index(idx, number):
#     return 0 <= idx < number
# 
# 
# def check_possible_attacks(mtrx, rol, col, size):
#     moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
#     result = 0
#     for dr, dc in moves:
#         next_row, next_col = rol + dr, col + dc
#         if (is_valid_index(next_row, size) and
#                 is_valid_index(next_col, size) and mtrx[next_row][next_col] == "K"):
#             result += 1
#     return result
# 
# 
# size = int(input())
# matrix = [list(input()) for _ in range(size)]
# 
# removed_knights_number = 0
# knight_row, knight_column = 0, 0
# 
# while True:
#     max_possible_attack = 0
#     for row in range(size):
#         for column in range(size):
#             if matrix[row][column] == "K":
#                 attack = check_possible_attacks(matrix, row, column, size)
#                 if attack > max_possible_attack:
#                     max_possible_attack = attack
#                     knight_row, knight_column = row, column
# 
#     if max_possible_attack == 0:
#         break
# 
#     matrix[knight_row][knight_column] = "0"
#     removed_knights_number += 1
# 
# print(removed_knights_number)




########################################################################################################################
# def is_valid_index(idx, number):
#     return 0 <= idx < number
#
#
# def check_possible_attacks(mtrx, r, col, num_of_rows):
#     result = 0
#     if is_valid_index(r - 1, num_of_rows) and is_valid_index(col - 2, num_of_rows) and mtrx[r - 1][col - 2] == "K":
#         result += 1
#     if is_valid_index(r - 2, num_of_rows) and is_valid_index(col - 1, num_of_rows) and mtrx[r - 2][col - 1] == "K":
#         result += 1
#     if is_valid_index(r - 2, num_of_rows) and is_valid_index(col + 1, num_of_rows) and mtrx[r - 2][col + 1] == "K":
#         result += 1
#     if is_valid_index(r - 1, num_of_rows) and is_valid_index(col + 2, num_of_rows) and mtrx[r - 1][col + 2] == "K":
#         result += 1
#     if is_valid_index(r + 1, num_of_rows) and is_valid_index(col + 2, num_of_rows) and mtrx[r + 1][col + 2] == "K":
#         result += 1
#     if is_valid_index(r + 2, num_of_rows) and is_valid_index(col + 1, num_of_rows) and mtrx[r + 2][col + 1] == "K":
#         result += 1
#     if is_valid_index(r + 2, num_of_rows) and is_valid_index(col - 1, num_of_rows) and mtrx[r + 2][col - 1] == "K":
#         result += 1
#     if is_valid_index(r + 1, num_of_rows) and is_valid_index(col - 2, num_of_rows) and mtrx[r + 1][col - 2] == "K":
#         result += 1
#
#     return result
#
#
# size = int(input())
# matrix = [list(input()) for _ in range(size)]
#
# removed_knights_number = 0
# knight_row, knight_column = 0, 0
#
# while True:
#     max_possible_attack = 0
#     for row in range(size):
#         for column in range(size):
#             if matrix[row][column] == "K":
#                 attack = check_possible_attacks(matrix, row, column, size)
#                 if attack > max_possible_attack:
#                     max_possible_attack = attack
#                     knight_row, knight_column = row, column
#
#     if max_possible_attack == 0:
#         break
#
#     matrix[knight_row][knight_column] = "0"
#     removed_knights_number += 1
#
# print(removed_knights_number)
