# 1.Move queens
def fill_matrix_and_take_pos(matrix, queens, size):
    for i in range(size):
        row = input().split()
        matrix.append(row)
        if "Q" in row:
            for j, col in enumerate(row):
                if col == "Q":
                    q_row, q_col = i, j
                    q_position = q_row, q_col
                    queens.append(q_position)
    return matrix, queens


def is_valid_index(idx, value):
    return 0 <= idx < value


def next_move(row, col, direction, directions):
    d_row, d_col = directions[direction][0], directions[direction][1]
    return row + d_row, col + d_col


def check_for_queen(r, c, matrix):
    return matrix[r][c] == 'Q'


def check_for_king(r, c, matrix):
    return matrix[r][c] == 'K'


def main():
    size = 8
    matrix = []
    queens = []
    matrix, queens = fill_matrix_and_take_pos(matrix, queens, size)
    queens_capture_king = []
    found_queen, found_king = None, None

    directions = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
        "top left diagonal": (-1, -1),
        "bottom left diagonal": (-1, 1),
        "top right diagonal": (1, -1),
        "bottom right diagonal": (1, 1)}

    for pos in queens:
        q_row, q_col = pos[0], pos[1]  # save the original coordinates for the output
        for direction in directions:
            row, col = q_row, q_col  # for update on next move
            for move in range(size):
                next_row, next_col = next_move(row, col, direction, directions)
                if is_valid_index(next_row, size) and is_valid_index(next_col, size):
                    found_queen = check_for_queen(next_row, next_col, matrix)
                    found_king = check_for_king(next_row, next_col, matrix)
                    if found_king:
                        queens_capture_king.append([q_row, q_col])
                        break
                if found_queen or not is_valid_index(next_row, size) or not is_valid_index(next_col, size):
                    break
                row, col = next_row, next_col

    if queens_capture_king:
        for q_row in queens_capture_king:
            print(f"[{q_row[0]}, {q_row[1]}]")
    else:
        print("The king is safe!")


if __name__ == '__main__':
    main()



# 2. move king
# def is_valid_index(idx, size):
#     return 0 <= idx < size
#
#
# def next_move(row, col, direction, directions):
#     d_row, d_col = directions[direction][0], directions[direction][1]
#     return row + d_row, col + d_col
#
#
# def main():
#     size = 8
#     matrix, queens_capture_kings = [], []
#     king_row, king_col = 0, 0
#
#     directions = {
#         "up": (0, -1),
#         "down": (0, 1),
#         "left": (-1, 0),
#         "right": (1, 0),
#         "top left diagonal": (-1, -1),
#         "bottom left diagonal": (-1, 1),
#         "top right diagonal": (1, -1),
#         "bottom right diagonal": (1, 1)}
#
#     for row in range(size):
#         matrix.append(input().split())
#         if "K" in matrix[row]:
#             king_row = row
#             king_col = matrix[row].index("K")
#
#     for direction in directions:
#         next_row, next_col = king_row, king_col
#         for move in range(size):
#             next_row, next_col = next_move(next_row, next_col, direction, directions)
#             if is_valid_index(next_row, size) and is_valid_index(next_col, size):
#                 if matrix[next_row][next_col] == "Q":
#                     queens_capture_kings.append([next_row, next_col])
#                     break
#             else:
#                 break
#
#     [print(row) for row in queens_capture_kings] if queens_capture_kings else print("The king is safe!")
#
#
#
# if __name__ == '__main__':
#     main()





###########################################################################################################################
# 3. move the queens - long way

# def is_valid_index(idx, value):
#     return 0 <= idx < value
#
#
# def check_for_queen(r, c, matrix):
#     return matrix[r][c] == 'Q'
#
#
# def take_queen_position(position, queens_capture_kings):
#     if position not in queens_capture_kings:
#         queens_capture_kings.append(position)
#     return queens_capture_kings
#
#
# def fill_matrix_and_take_pos(matrix, queens, size):
#     for i in range(size):
#         row = input().split()
#         matrix.append(row)
#         if "Q" in row:
#             for j, col in enumerate(row):
#                 if col == "Q":
#                     q_row, q_col = i, j
#                     q_position = q_row, q_col
#                     queens.append(q_position)
#
#     return matrix, queens
#
#
# def check_up(matrix, row, col, queens_capture_king, size):
#     for r in range(row - 1, -1, -1):
#         queen_on_spot = check_for_queen(r, col, matrix)
#         if queen_on_spot:
#             break
#         if matrix[r][col] == 'K':
#             position = row, col
#             queens_capture_kings = (
#                 take_queen_position(position, queens_capture_king))
#     return queens_capture_king
#
#
# def check_down(matrix, row, col, queens_capture_king, size):
#     for r in range(row + 1, size):
#         queen_on_spot = check_for_queen(r, col, matrix)
#         if queen_on_spot:
#             break
#         if matrix[r][col] == 'K':
#             position = row, col
#             queens_capture_kings = (
#                 take_queen_position(position, queens_capture_king))
#     return queens_capture_king
#
#
# def check_left(matrix, row, col, queens_capture_king, size):
#     for c in range(col - 1, -1, -1):
#         queen_on_spot = check_for_queen(row, c, matrix)
#         if queen_on_spot:
#             break
#         if matrix[row][c] == 'K':
#             position = row, col
#             queens_capture_kings = (
#                 take_queen_position(position, queens_capture_king))
#     return queens_capture_king
#
#
# def check_right(matrix, row, col, queens_capture_king, size):
#     for c in range(col + 1, size):
#         queen_on_spot = check_for_queen(row, c, matrix)
#         if queen_on_spot:
#             break
#         if matrix[row][c] == 'K':
#             position = row, col
#             queens_capture_kings = (
#                 take_queen_position(position, queens_capture_king))
#     return queens_capture_king
#
#
# def check_top_left(matrix, row, col, queens_capture_king, size):
#     idx = 1
#     for r in range(row - 1, -1, -1):
#         c = col - idx
#         if not is_valid_index(c, size):
#             break
#         queen_on_spot = check_for_queen(r, c, matrix)
#         if queen_on_spot:
#             break
#         if matrix[r][c] == 'K':
#             position = row, col
#             queens_capture_kings = (
#                 take_queen_position(position, queens_capture_king))
#         idx += 1
#     return queens_capture_king
#
#
# def check_bottom_left(matrix, row, col, queens_capture_king, size):
#     idx = 1
#     for r in range(row + 1, size):
#         c = col + idx
#         if not is_valid_index(c, size):
#             break
#         queen_on_spot = check_for_queen(r, c, matrix)
#         if queen_on_spot:
#             break
#         if matrix[r][c] == 'K':
#             position = row, col
#             queens_capture_kings = (
#                 take_queen_position(position, queens_capture_king))
#         idx += 1
#     return queens_capture_king
#
#
# def check_top_right(matrix, row, col, queens_capture_king, size):
#     idx = 1
#     for r in range(row + 1, size):
#         c = col - idx
#         if not is_valid_index(c, size):
#             break
#         queen_on_spot = check_for_queen(r, c, matrix)
#         if queen_on_spot:
#             break
#         if matrix[r][c] == 'K':
#             position = row, col
#             queens_capture_kings = (
#                 take_queen_position(position, queens_capture_king))
#         idx += 1
#     return queens_capture_king
#
#
# def check_bottom_right(matrix, row, col, queens_capture_king, size):
#     idx = 1
#     for r in range(row - 1, - 1, -1):
#         c = col + idx
#         if not is_valid_index(c, size):
#             break
#         queen_on_spot = check_for_queen(r, c, matrix)
#         if queen_on_spot:
#             break
#         if matrix[r][c] == 'K':
#             position = row, col
#             queens_capture_kings = (
#                 take_queen_position(position, queens_capture_king))
#         idx += 1
#     return queens_capture_king
#
#
# def main():
#     size = 8
#     matrix = []
#     queens = []
#     queens_capture_king = []
#     matrix, queens = fill_matrix_and_take_pos(matrix, queens, size)
#
#     for pos in queens:
#         row, col = pos[0], pos[1]
#         queens_capture_king = check_up(matrix, row, col, queens_capture_king, size)
#         queens_capture_king = check_down(matrix, row, col, queens_capture_king, size)
#         queens_capture_king = check_left(matrix, row, col, queens_capture_king, size)
#         queens_capture_king = check_right(matrix, row, col, queens_capture_king, size)
#         queens_capture_king = check_top_left(matrix, row, col, queens_capture_king, size)
#         queens_capture_king = check_bottom_left(matrix, row, col, queens_capture_king, size)
#         queens_capture_king = check_top_right(matrix, row, col, queens_capture_king, size)
#         queens_capture_king = check_bottom_right(matrix, row, col, queens_capture_king, size)
#
#     if queens_capture_king:
#         for row in queens_capture_king:
#             print(f"[{row[0]}, {row[1]}]")
#     else:
#         print("The king is safe!")
#
#
# if __name__ == '__main__':
#     main()
