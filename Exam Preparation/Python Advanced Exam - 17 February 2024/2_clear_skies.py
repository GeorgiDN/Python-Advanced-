def is_valid_index(idx, value):
    return 0 <= idx < value


def fill_matrix_and_takes_pos(pl_row, pl_col, rows, player, count_enemies):
    matrix = []
    for idx in range(rows):
        row = list(input())
        matrix.append(row)
        if player in row:
            pl_row = idx
            pl_col = row.index(player)
        if 'E' in row:
            count_enemies += row.count('E')

    return matrix, pl_row, pl_col, count_enemies


def next_move(pl_row, pl_col, direction, rows):
    moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    d_row, d_col = moves[direction][0], moves[direction][1]
    next_row = (pl_row + d_row) if is_valid_index(pl_row + d_row, rows) else None
    next_col = (pl_col + d_col) if is_valid_index(pl_col + d_col, rows) else None

    return next_row, next_col


def main():
    rows = int(input())
    pl_row, pl_col = 0, 0
    count_enemies = 0
    jet, empty, enemy, repair = 'J', '-', 'E', 'R'
    armour = 300
    matrix, pl_row, pl_col, count_enemies = (
        fill_matrix_and_takes_pos(pl_row, pl_col, rows, jet, count_enemies))

    while True:

        if armour == 0:
            print(f'Mission failed, your jetfighter was shot down! Last coordinates [{pl_row}, {pl_col}]!')
            break
        elif count_enemies == 0:
            print('Mission accomplished, you neutralized the aerial threat!')
            break
        direction = input()

        next_row, next_col = next_move(pl_row, pl_col, direction, rows)

        if matrix[next_row][next_col] == enemy:
            armour -= 100
            count_enemies -= 1

        if matrix[next_row][next_col] == repair:
            armour = 300

        matrix[pl_row][pl_col] = empty
        pl_row, pl_col = next_row, next_col
        matrix[pl_row][pl_col] = jet

    for row in matrix:
        print(''.join(row))


if __name__ == '__main__':
    main()


###############################################################################################



# def next_move(direction, row, col, rows):
#     moves = {
#         "up": (-1, 0),
#         "down": (1, 0),
#         "left": (0, -1),
#         "right": (0, 1)
#     }

#     d_row, d_col = moves[direction]
#     row = (row + d_row)
#     col = (col + d_col)
#     return row, col

# def fill_the_field_and_find_jet_position(size, j_row, j_col, enemies):
#     field = []
#     for r in range(size):
#         row = list(input())
#         field.append(row)
#         if "J" in row:
#             j_row = r
#             j_col = row.index("J")
#         if "E" in row:
#             enemies += row.count("E")

#     return field, j_row, j_col, enemies


# def main():
#     size = int(input())
#     jet_row, jet_col = None, None
#     enemies = 0
#     field, jet_row, jet_col, enemies = fill_the_field_and_find_jet_position(size, jet_row, jet_col, enemies)
#     jet_armour = 300
#     line = ' '

#     while line:
#         line = input()

#         next_row, next_col = next_move(line, jet_row, jet_col, size)
#         field[jet_row][jet_col] = "-"

#         if field[next_row][next_col] == "E":
#             field[next_row][next_col] = "-"
#             enemies -= 1
#             if enemies == 0:
#                 print("Mission accomplished, you neutralized the aerial threat!")
#                 jet_row, jet_col = next_row, next_col
#                 field[jet_row][jet_col] = "J"
#                 break
#             else:
#                 jet_armour -= 100
#                 if jet_armour <= 0:
#                     jet_row, jet_col = next_row, next_col
#                     field[jet_row][jet_col] = "J"
#                     print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet_row}, {jet_col}]!")
#                     break

#         elif field[next_row][next_col] == "R":
#             jet_armour = 300
#             field[next_row][next_col] = "-"

#         jet_row, jet_col = next_row, next_col
#         field[jet_row][jet_col] = "J"

#     for row_ in field:
#         print(''.join(row_))


# if __name__ == "__main__":
#     main()





#######################################################################################################################################################
# def is_valid(value, max_value):
#     return 0 <= value < max_value


# def next_move(command, current_row, current_col, size_):
#     if command == "up" and is_valid(current_row - 1, size_):
#         return current_row - 1, current_col
#     if command == "down" and is_valid(current_row + 1, size_):
#         return current_row + 1, current_col
#     if command == "left" and is_valid(current_col - 1, size_):
#         return current_row, current_col - 1
#     if command == "right" and is_valid(current_col + 1, size_):
#         return current_row, current_col + 1
#     return None, None


# def fill_the_field_and_find_jet_position(size_, jet_row_, jet_col_):
#     field_ = []
#     for r in range(size_):
#         row = list(input())
#         field_.append(row)
#         if "J" in row:
#             jet_row_ = r
#             jet_col_ = row.index("J")

#     return field_, jet_row_, jet_col_


# def have_enemies_left(matrix, size_):
#     enemy_left = False
#     for row in range(size_):
#         for col in range(size_):
#             if matrix[row][col] == "E":
#                 enemy_left = True
#                 break
#     return enemy_left


# def main():
#     size = int(input())
#     jet_row, jet_col = None, None
#     field, jet_row, jet_col = fill_the_field_and_find_jet_position(size, jet_row, jet_col)
#     jet_armour = 300

#     line = ' '

#     while line:
#         line = input()

#         next_row, next_col = next_move(line, jet_row, jet_col, size)
#         field[jet_row][jet_col] = "-"

#         if field[next_row][next_col] == "E":
#             field[next_row][next_col] = "-"
#             if not have_enemies_left(field, size):
#                 print("Mission accomplished, you neutralized the aerial threat!")
#                 jet_row, jet_col = next_row, next_col
#                 field[jet_row][jet_col] = "J"
#                 break
#             else:
#                 jet_armour -= 100
#                 if jet_armour <= 0:
#                     jet_row, jet_col = next_row, next_col
#                     field[jet_row][jet_col] = "J"
#                     print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet_row}, {jet_col}]!")
#                     break

#         elif field[next_row][next_col] == "R":
#             jet_armour = 300
#             field[next_row][next_col] = "-"

#         jet_row, jet_col = next_row, next_col
#         field[jet_row][jet_col] = "J"

#     for row_ in field:
#         print(''.join(row_))


# if __name__ == "__main__":
#     main()
