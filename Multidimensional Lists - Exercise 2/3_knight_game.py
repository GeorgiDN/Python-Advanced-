def is_valid_index(idx, number):
    return 0 <= idx < number


def check_possible_attacks(mtrx, rol, col, num_of_rows):
    moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    result = 0
    for dr, dc in moves:
        next_row, next_col = rol + dr, col + dc
        if (is_valid_index(next_row, num_of_rows) and
                is_valid_index(next_col, num_of_rows) and mtrx[next_row][next_col] == "K"):
            result += 1
    return result


size = int(input())
matrix = [list(input()) for _ in range(size)]

removed_knights_number = 0
knight_row, knight_column = 0, 0

while True:
    max_possible_attack = 0
    for row in range(size):
        for column in range(size):
            if matrix[row][column] == "K":
                attack = check_possible_attacks(matrix, row, column, size)
                if attack > max_possible_attack:
                    max_possible_attack = attack
                    knight_row, knight_column = row, column

    if max_possible_attack == 0:
        break

    matrix[knight_row][knight_column] = "0"
    removed_knights_number += 1

print(removed_knights_number)





# def is_valid_index(idx, number):
#     return 0 <= idx < number


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

#     return result


# size = int(input())
# matrix = [list(input()) for _ in range(size)]

# removed_knights_number = 0
# knight_row, knight_column = 0, 0

# while True:
#     max_possible_attack = 0
#     for row in range(size):
#         for column in range(size):
#             if matrix[row][column] == "K":
#                 attack = check_possible_attacks(matrix, row, column, size)
#                 if attack > max_possible_attack:
#                     max_possible_attack = attack
#                     knight_row, knight_column = row, column

#     if max_possible_attack == 0:
#         break

#     matrix[knight_row][knight_column] = "0"
#     removed_knights_number += 1

# print(removed_knights_number)
