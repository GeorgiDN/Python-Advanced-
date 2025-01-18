def is_valid_index(index, max_value):
    return 0 <= index < max_value


def next_move(p_row, p_col, direction, size):
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    d_row, d_col = directions[direction][0], directions[direction][1]
    next_row = p_row + d_row if is_valid_index(p_row + d_row, size) else None
    next_col = p_col + d_col if is_valid_index(p_col + d_col, size) else None

    return next_row, next_col


def main():
    size, commands = int(input()), input().split()
    matrix, empty, end, coal, miner, game_over = [], '*', 'e', 'c', 's', False
    miner_row, miner_col, coals_number = 0, 0, 0

    for idx in range(size):
        row = input().split()
        matrix.append(row)
        if miner in row:
            miner_row, miner_col = idx, row.index(miner)
        if coal in row:
            coals_number += row.count(coal)

    coals_left = coals_number
    for direction in commands:
        if game_over: break
        
        next_row, next_col = next_move(miner_row, miner_col, direction, size)

        if next_row is not None and next_col is not None:
            if matrix[next_row][next_col] == end:
                game_over = True
                print(f'Game over! ({next_row}, {next_col})')

            if matrix[next_row][next_col] == coal:
                coals_left -= 1

            matrix[miner_row][miner_col] = empty
            miner_row, miner_col = next_row, next_col
            matrix[miner_row][miner_col] = empty

    if not game_over:
        print(f'You collected all coal! ({miner_row}, {miner_col})') if coals_left == 0 \
            else print(f'{coals_left} pieces of coal left. ({miner_row}, {miner_col})')


if __name__ == '__main__':
    main()


############################################################################################################################################################################
# def fill_the_field_and_find_coals_and_miner(size, field, miner_row, miner_col, coals_number):
#     for r in range(size):
#         row = input().split()
#         field.append(row)
#         if "s" in row:
#             miner_row = r
#             miner_col = row.index('s')
#         if "c" in row:
#             coals_number += row.count("c")
#
#     return field, miner_row, miner_col, coals_number
#
#
# def is_valid_index(value, max_value):
#     return 0 <= value < max_value
#
#
# def next_move(current_direction, curr_row, curr_col, size_):
#     all_directions = {"up": [curr_row - 1, curr_col],
#                       "down": [curr_row + 1, curr_col],
#                       "right": [curr_row, curr_col + 1],
#                       "left": [curr_row, curr_col - 1]}
#
#     new_row, new_col = all_directions[current_direction][0], all_directions[current_direction][1]
#     if is_valid_index(new_row, size_) \
#             and is_valid_index(new_col, size_):
#         return new_row, new_col
#     return None, None
#
#
# def main():
#     size = int(input())
#     directions = input().split()
#     field = []
#     miner_row, miner_col = None, None
#     coals_number = 0
#     game_over = False
#     field, miner_row, miner_col, coals_number =\
#         fill_the_field_and_find_coals_and_miner(size, field, miner_row, miner_col, coals_number)
#
#     for direction in directions:
#         next_row, next_col = next_move(direction, miner_row, miner_col, size)
#         if next_row is None or next_col is None:
#             continue
#
#         if field[next_row][next_col] == "c":
#             coals_number -= 1
#             field[miner_row][miner_col] = "*"
#             if coals_number == 0:
#                 miner_row, miner_col = next_row, next_col
#                 print(f"You collected all coal! ({miner_row}, {miner_col})")
#                 field[miner_row][miner_col] = "s"
#                 break
#
#         elif field[next_row][next_col] == "e":
#             field[miner_row][miner_col] = "*"
#             miner_row, miner_col = next_row, next_col
#             print(f"Game over! ({miner_row}, {miner_col})")
#             game_over = True
#             field[miner_row][miner_col] = "s"
#             break
#
#         field[miner_row][miner_col] = "*"
#         miner_row, miner_col = next_row, next_col
#         field[miner_row][miner_col] = "s"
#
#     if coals_number > 0 and not game_over:
#         print(f"{coals_number} pieces of coal left. ({miner_row}, {miner_col})")
#
#
# if __name__ == '__main__':
#     main()


#########################################################################################################################################################
# size = int(input())
# commands = input().split()
# matrix = []
# coal = 0
# miner_row, miner_col = 0, 0
# game_over_condition = False
# new_row = 0
# new_col = 0
#
#
# for row in range(size):
#     current_row = [x for x in input().split()]
#     matrix.append(current_row)
#     for col in range(size):
#         if current_row[col] == "s":
#             miner_row, miner_col = row, col
#         elif current_row[col] == "c":
#             coal += 1
#
# for command in commands:
#     if command == "up":
#         if miner_row - 1 in range(size):
#             new_row, new_col = miner_row - 1, miner_col
#         else:
#             continue
#     elif command == "down":
#         if miner_row + 1 in range(size):
#             new_row, new_col = miner_row + 1, miner_col
#         else:
#             continue
#     elif command == "left":
#         if miner_col - 1 in range(size):
#             new_row, new_col = miner_row, miner_col - 1
#         else:
#             continue
#     elif command == "right":
#         if miner_col + 1 in range(size):
#             new_row, new_col = miner_row, miner_col + 1
#         else:
#             continue
#     symbol_to_overcome = matrix[new_row][new_col]
#     if symbol_to_overcome == "c":
#         coal -= 1
#     elif symbol_to_overcome == "e":
#         print(f"Game over! ({new_row}, {new_col})")
#         game_over_condition = True
#         break
#     matrix[new_row][new_col] = "s"
#     matrix[miner_row][miner_col] = "*"
#     miner_row, miner_col = new_row, new_col
#     if coal == 0:
#         print(f"You collected all coal! ({new_row}, {new_col})")
#         game_over_condition = True
#         break
#
# if not game_over_condition:
#     print(f"{coal} pieces of coal left. ({miner_row}, {miner_col})")
