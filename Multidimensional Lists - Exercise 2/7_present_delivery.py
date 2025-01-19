def is_valid_index(value, max_value):
    return 0 <= value < max_value


directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
}

presents, rows = int(input()), int(input())
matrix, santa, nice_kid, naughty_kid, cookie, empty = [], 'S', 'V', 'X', 'C', '-'
s_row, s_col = 0, 0
kids_for_present = 0

for idx in range(rows):
    row = input().split()
    matrix.append(row)
    if santa in row:
        s_row, s_col = idx, row.index(santa)
    if nice_kid in row:
        kids_for_present += row.count(nice_kid)

count_nice_kids = kids_for_present

while True:
    if presents == 0:
        break

    command = input()
    if command == 'Christmas morning':
        break

    direction = command
    d_row, d_col = directions[direction][0], directions[direction][1]
    next_row, next_col = s_row + d_row, s_col + d_col

    if is_valid_index(next_row, rows) and is_valid_index(next_col, rows):
        if matrix[next_row][next_col] == nice_kid:
            presents -= 1
            kids_for_present -= 1

        elif matrix[next_row][next_col] == cookie:
            for d in directions.values():
                if presents == 0:
                    break
                new_row, new_col = next_row + d[0], next_col + d[1]
                if matrix[new_row][new_col] == nice_kid or matrix[new_row][new_col] == naughty_kid:
                    if matrix[new_row][new_col] == nice_kid:
                        presents -= 1
                        kids_for_present -= 1
                    else:  # naughty kid
                        presents -= 1
                    matrix[new_row][new_col] = empty

        matrix[s_row][s_col] = empty
        s_row, s_col = next_row, next_col
        matrix[s_row][s_col] = santa

if presents == 0 and kids_for_present > 0:
    print('Santa ran out of presents!')

for r in matrix:
    print(' '.join(r))

if presents >= 0 and kids_for_present == 0:
    print(f'Good job, Santa! {count_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {kids_for_present} nice kid/s.')



##################################################################################################################################################################################################################
# def is_valid_index(matrix, idx):
#     return 0 <= idx < len(matrix)


# def next_move(matrix, curr_row, curr_col, line):
#     all_directions = {"up": [curr_row - 1, curr_col],
#                       "down": [curr_row + 1, curr_col],
#                       "right": [curr_row, curr_col + 1],
#                       "left": [curr_row, curr_col - 1]}

#     new_row, new_col = all_directions[line][0], all_directions[line][1]
#     if is_valid_index(matrix, new_row) \
#             and is_valid_index(matrix, new_col):
#         return new_row, new_col

#     return None, None


# def fill_the_matrix_and_take_positions(n, s_row, s_col):
#     matrix = []
#     nice_kids = 0
#     for r in range(n):
#         row = input().split()
#         matrix.append(row)
#         if "S" in row:
#             s_row = r
#             s_col = row.index("S")
#         if "V" in row:
#             nice_kids += row.count("V")
#     return matrix, s_row, s_col, nice_kids


# def cookies_time(matrix, presents_, nice_kids, new_row, new_col):
#     surrounding_houses = [
#         [new_row - 1, new_col],
#         [new_row + 1, new_col],
#         [new_row, new_col - 1],
#         [new_row, new_col + 1]
#     ]

#     for house in surrounding_houses:
#         if presents_ == 0:
#             break
#         h_row, h_col = house
#         if matrix[h_row][h_col] == "X":
#             presents_ -= 1
#         elif matrix[h_row][h_col] == "V":
#             presents_ -= 1
#             nice_kids -= 1

#         matrix[h_row][h_col] = "S_C"  # Check where Santa eat cookie
#         matrix[h_row][h_col] = "-"

#     return matrix, presents_, nice_kids


# def print_result(neighbourhood, nice_kids_left, nice_kids_count, presents):
#     if nice_kids_left > 0 and presents == 0:
#         print("Santa ran out of presents!")
#     [print(" ".join(element)) for element in neighbourhood]

#     print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.") \
#         if nice_kids_left == 0 else print(f"No presents for {nice_kids_left} nice kid/s.")


# def main():
#     presents = int(input())
#     size = int(input())
#     santa_row, santa_col = 0, 0
#     neighbourhood, santa_row, santa_col, nice_kids_count = (
#         fill_the_matrix_and_take_positions(size, santa_row, santa_col))
#     nice_kids_left = nice_kids_count

#     while True:
#         if presents == 0:
#             break
#         command = input()
#         if command == "Christmas morning":
#             break

#         direction = command
#         next_row, next_col = next_move(neighbourhood, santa_row, santa_col, direction)

#         if next_row is not None and next_col is not None:
#             if neighbourhood[next_row][next_col] == "V":
#                 presents -= 1
#                 nice_kids_left -= 1

#             elif neighbourhood[next_row][next_col] == "C":
#                 neighbourhood, presents, nice_kids_left = (
#                     cookies_time(neighbourhood, presents, nice_kids_left, next_row, next_col))

#             neighbourhood[santa_row][santa_col] = "-"
#             santa_row, santa_col = next_row, next_col
#             neighbourhood[santa_row][santa_col] = "S"  # check where is Santa

#     print_result(neighbourhood, nice_kids_left, nice_kids_count, presents)


# if __name__ == '__main__':
#     main()



####################################################################################################################################################################################################
# def is_valid_index(matrix, idx):
#     return 0 <= idx < len(matrix)


# def next_move(matrix, curr_row, curr_col, line):
#     if line == "up" and is_valid_index(matrix, curr_row - 1):
#         return curr_row - 1, curr_col
#     elif line == "down" and is_valid_index(matrix, curr_row + 1):
#         return curr_row + 1, curr_col
#     elif line == "right" and is_valid_index(matrix, curr_col + 1):
#         return curr_row, curr_col + 1
#     elif line == "left" and is_valid_index(matrix, curr_col - 1):
#         return curr_row, curr_col - 1
#     return None, None


# def fill_the_matrix_and_take_positions(n, s_row, s_col):
#     matrix = []
#     nice_kids = 0
#     for r in range(n):
#         row = input().split()
#         matrix.append(row)
#         if "S" in row:
#             s_row = r
#             s_col = row.index("S")
#         if "V" in row:
#             nice_kids += row.count("V")
#     return matrix, s_row, s_col, nice_kids


# def main():
#     presents = int(input())
#     size = int(input())
#     santa_row, santa_col = 0, 0
#     neighbourhood, santa_row, santa_col, nice_kids_count = (
#         fill_the_matrix_and_take_positions(size, santa_row, santa_col))
#     nice_kids_left = nice_kids_count

#     while True:
#         if presents == 0:
#             break
#         command = input()
#         if command == "Christmas morning":
#             break

#         direction = command
#         next_row, next_col = next_move(neighbourhood, santa_row, santa_col, direction)

#         if next_row is not None and next_col is not None:
#             if neighbourhood[next_row][next_col] == "V":
#                 presents -= 1
#                 nice_kids_left -= 1

#             elif neighbourhood[next_row][next_col] == "C":
#                 surrounding_houses = [
#                     [next_row - 1, next_col],
#                     [next_row + 1, next_col],
#                     [next_row, next_col - 1],
#                     [next_row, next_col + 1]
#                 ]
#                 for house in surrounding_houses:
#                     if presents == 0:
#                         break
#                     h_row, h_col = house
#                     if neighbourhood[h_row][h_col] == "X":
#                         presents -= 1
#                     elif neighbourhood[h_row][h_col] == "V":
#                         presents -= 1
#                         nice_kids_left -= 1
#                     neighbourhood[h_row][h_col] = "-"

#             neighbourhood[santa_row][santa_col] = "-"
#             santa_row, santa_col = next_row, next_col
#             neighbourhood[santa_row][santa_col] = "S"  # check where is Santa

#     if nice_kids_left > 0 and presents == 0:
#         print("Santa ran out of presents!")
#     [print(" ".join(element)) for element in neighbourhood]
#     if nice_kids_left == 0:
#         print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")
#     else:
#         print(f"No presents for {nice_kids_left} nice kid/s.")


# if __name__ == '__main__':
#     main()
