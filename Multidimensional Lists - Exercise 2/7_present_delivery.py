def is_valid_index(matrix, idx):
    return 0 <= idx < len(matrix)


def next_move(matrix, curr_row, curr_col, line):
    all_directions = {"up": [curr_row - 1, curr_col],
                      "down": [curr_row + 1, curr_col],
                      "right": [curr_row, curr_col + 1],
                      "left": [curr_row, curr_col - 1]}

    new_row, new_col = all_directions[line][0], all_directions[line][1]
    if is_valid_index(matrix, new_row) \
            and is_valid_index(matrix, new_col):
        return new_row, new_col

    return None, None


def fill_the_matrix_and_take_positions(n, s_row, s_col):
    matrix = []
    nice_kids = 0
    for r in range(n):
        row = input().split()
        matrix.append(row)
        if "S" in row:
            s_row = r
            s_col = row.index("S")
        if "V" in row:
            nice_kids += row.count("V")
    return matrix, s_row, s_col, nice_kids


def cookies_time(matrix, presents_, nice_kids, new_row, new_col):
    surrounding_houses = [
        [new_row - 1, new_col],
        [new_row + 1, new_col],
        [new_row, new_col - 1],
        [new_row, new_col + 1]
    ]

    for house in surrounding_houses:
        if presents_ == 0:
            break
        h_row, h_col = house
        if matrix[h_row][h_col] == "X":
            presents_ -= 1
        elif matrix[h_row][h_col] == "V":
            presents_ -= 1
            nice_kids -= 1

        matrix[h_row][h_col] = "S_C"  # Check where Santa eat cookie
        matrix[h_row][h_col] = "-"

    return matrix, presents_, nice_kids


def print_result(neighbourhood, nice_kids_left, nice_kids_count, presents):
    if nice_kids_left > 0 and presents == 0:
        print("Santa ran out of presents!")
    [print(" ".join(element)) for element in neighbourhood]

    print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.") \
        if nice_kids_left == 0 else print(f"No presents for {nice_kids_left} nice kid/s.")


def main():
    presents = int(input())
    size = int(input())
    santa_row, santa_col = 0, 0
    neighbourhood, santa_row, santa_col, nice_kids_count = (
        fill_the_matrix_and_take_positions(size, santa_row, santa_col))
    nice_kids_left = nice_kids_count

    while True:
        if presents == 0:
            break
        command = input()
        if command == "Christmas morning":
            break

        direction = command
        next_row, next_col = next_move(neighbourhood, santa_row, santa_col, direction)

        if next_row is not None and next_col is not None:
            if neighbourhood[next_row][next_col] == "V":
                presents -= 1
                nice_kids_left -= 1

            elif neighbourhood[next_row][next_col] == "C":
                neighbourhood, presents, nice_kids_left = (
                    cookies_time(neighbourhood, presents, nice_kids_left, next_row, next_col))

            neighbourhood[santa_row][santa_col] = "-"
            santa_row, santa_col = next_row, next_col
            neighbourhood[santa_row][santa_col] = "S"  # check where is Santa

    print_result(neighbourhood, nice_kids_left, nice_kids_count, presents)


if __name__ == '__main__':
    main()




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
