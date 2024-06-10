def is_valid_index(idx, size):
    return 0 <= idx < size


def next_move(rows, cols, row, col, direction):
    all_directions = {"up": [row - 1, col],
                      "down": [row + 1, col],
                      "right": [row, col + 1],
                      "left": [row, col - 1]}

    new_row, new_col = all_directions[direction][0], all_directions[direction][1]
    if is_valid_index(new_row, rows) \
            and is_valid_index(new_col, cols):
        return new_row, new_col
    return None, None


def fill_the_matrix_and_take_positions(rows, m_row, m_col, cheese_count):
    field = []
    for r in range(rows):
        row = list(input())
        field.append(row)
        if "M" in row:
            m_row = r
            m_col = row.index("M")
        if 'C' in row:
            cheese_count += row.count("C")

    return field, m_row, m_col, cheese_count


def out_of_boundaries_check(next_row, next_col):
    return next_row is None or next_col is None


def mark_past_moves_in_the_field(field, next_row, next_col, mouse_row, mouse_col):
    field[mouse_row][mouse_col] = "*"
    mouse_row, mouse_col = next_row, next_col
    field[mouse_row][mouse_col] = "M"
    return field, next_row, next_col, mouse_row, mouse_col


def cheese_check(field, cheese_count, next_row, next_col, mouse_row, mouse_col):
    if field[next_row][next_col] == "C":
        cheese_count -= 1
        mark_past_moves_in_the_field(field, next_row, next_col, mouse_row, mouse_col)

    return field, cheese_count, next_row, next_col, mouse_row, mouse_col


def trap_check(field, is_trapped, next_row, next_col, mouse_row, mouse_col):
    if field[next_row][next_col] == "T":
        is_trapped = True
        mark_past_moves_in_the_field(field, next_row, next_col, mouse_row, mouse_col)
        print("Mouse is trapped!")

    return field, is_trapped, next_row, next_col, mouse_row, mouse_col


def main():
    mouse_row, mouse_col = 0, 0
    cheese_count = 0
    rows, cols = [int(x) for x in input().split(',')]
    field, mouse_row, mouse_col, cheese_count = (
        fill_the_matrix_and_take_positions(rows, mouse_row, mouse_col, cheese_count))

    out_of_field = False
    is_trapped = False

    while True:
        direction = input()
        if direction == 'danger':
            print("Mouse will come back later!")
            break

        next_row, next_col = next_move(rows, cols, mouse_row, mouse_col, direction)
        out_of_field = out_of_boundaries_check(next_row, next_col)
        if out_of_field:
            field[mouse_row][mouse_col] = "M"
            print("No more cheese for tonight!")
            break

        if field[next_row][next_col] == "@":
            continue

        field, cheese_count, next_row, next_col, mouse_row, mouse_col = (
            cheese_check(field, cheese_count, next_row, next_col, mouse_row, mouse_col))

        if cheese_count <= 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

        field, is_trapped, next_row, next_col, mouse_row, mouse_col = (
            trap_check(field, is_trapped, next_row, next_col, mouse_row, mouse_col))

        if is_trapped:
            break

        field, next_row, next_col, mouse_row, mouse_col = (
            mark_past_moves_in_the_field(field, next_row, next_col, mouse_row, mouse_col))

    for r in field:
        print(''.join(r))


if __name__ == '__main__':
    main()










# def is_valid_index(idx, size):
#     return 0 <= idx < size
# 
# 
# def next_move(rows, cols, row, col, direction):
#     all_directions = {"up": [row - 1, col],
#                       "down": [row + 1, col],
#                       "right": [row, col + 1],
#                       "left": [row, col - 1]}
# 
#     new_row, new_col = all_directions[direction][0], all_directions[direction][1]
#     if is_valid_index(new_row, rows) \
#             and is_valid_index(new_col, cols):
#         return new_row, new_col
#     return None, None
# 
# 
# def fill_the_matrix_and_take_positions(rows, m_row, m_col, cheese_count):
#     field = []
#     for r in range(rows):
#         row = list(input())
#         field.append(row)
#         if "M" in row:
#             m_row = r
#             m_col = row.index("M")
#         if 'C' in row:
#             cheese_count += row.count("C")
# 
#     return field, m_row, m_col, cheese_count
# 
# 
# def check_out_of_boundaries(next_row, next_col):
#     return next_row is None or next_col is None
# 
# 
# def main():
#     field = []
#     mouse_row, mouse_col = 0, 0
#     cheese_count = 0
#     rows, cols = [int(x) for x in input().split(',')]
#     field, mouse_row, mouse_col, cheese_count = fill_the_matrix_and_take_positions(rows, mouse_row, mouse_col, cheese_count)
#     out_of_field = False
#     start_row, start_col = mouse_row, mouse_col
# 
# 
#     while True:
#         direction = input()
#         if direction == 'danger':
#             print("Mouse will come back later!")
#             break
# 
#         next_row, next_col = next_move(rows, cols, mouse_row, mouse_col, direction)
#         out_of_field = check_out_of_boundaries(next_row, next_col)
#         if out_of_field:
#             field[mouse_row][mouse_col] = "M"
#             print("No more cheese for tonight!")
#             break
# 
#         if field[next_row][next_col] == "@":
#             continue
# 
#         if field[next_row][next_col] == "C":
#             cheese_count -= 1
#             field[mouse_row][mouse_col] = "*"
#             mouse_row, mouse_col = next_row, next_col
#             field[mouse_row][mouse_col] = "M"
#             if cheese_count <= 0:
#                 print("Happy mouse! All the cheese is eaten, good night!")
#                 break
# 
#         if field[next_row][next_col] == "T":
#             field[mouse_row][mouse_col] = "*"
#             mouse_row, mouse_col = next_row, next_col
#             field[mouse_row][mouse_col] = "M"
#             print("Mouse is trapped!")
#             break
# 
#         field[mouse_row][mouse_col] = "*"
#         mouse_row, mouse_col = next_row, next_col
#         field[mouse_row][mouse_col] = "M"
# 
#     for r in field:
#         print(''.join(r))
# 
# 
# if __name__ == '__main__':
#     main()
