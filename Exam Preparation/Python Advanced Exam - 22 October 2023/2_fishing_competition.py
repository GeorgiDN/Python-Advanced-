def next_move(rows, row, col, direction):
    moves = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}

    d_row, d_col = moves[direction]
    row = (row + d_row) % rows
    col = (col + d_col) % rows
    return row, col


def fill_the_matrix_and_find_ship_position(rows, row, col):
    matrix = []
    for idx in range(rows):
        r = list(input())
        matrix.append(r)
        if 'S' in r:
            row = idx
            col = r.index('S')
    return matrix, row, col


def whirlpool_check(matrix, row, col):
    return matrix[row][col] == 'W'


def mark_past_moves(field, ship_row, ship_col, next_row, next_col):
    field[ship_row][ship_col] = '-'
    ship_row, ship_col = next_row, next_col
    field[ship_row][ship_col] = 'S'
    return field, ship_row, ship_col, next_row, next_col


def fish_check(field, next_row, next_col):
    return field[next_row][next_col].isdigit()


def print_result(field, fish_amount, quota_goal, fall_in_whirlpool, last_coordinates):
    result = ''
    if fall_in_whirlpool:
        last_row, last_col = last_coordinates[0], last_coordinates[1]
        result += (f'You fell into a whirlpool! '
                   f'The ship sank and you lost the fish you caught. '
                   f'Last coordinates of the ship: [{last_row},{last_col}]\n')

    else:
        if fish_amount >= quota_goal:
            result += 'Success! You managed to reach the quota!\n'
        else:
            lack_of_fish = quota_goal - fish_amount
            result += (f"You didn't catch enough fish and didn't reach the quota! "
                       f"You need {lack_of_fish} tons of fish more.\n")

        result += f'Amount of fish caught: {fish_amount} tons.\n' if fish_amount > 0 else ''

        for row in field:
            string_row = ''.join(row)
            result += f"{string_row}\n"

    result.strip()
    return print(result)


def main():
    fish_amount = 0
    ship_row, ship_col = 0, 0
    fall_in_whirlpool = False
    quota_goal = 20
    last_coordinates = None
    rows = int(input())
    field, ship_row, ship_col = fill_the_matrix_and_find_ship_position(rows, ship_row, ship_col)

    while True:
        command = input()
        if command == 'collect the nets':
            break

        direction = command
        next_row, next_col = next_move(rows, ship_row, ship_col, direction)
        fall_in_whirlpool = whirlpool_check(field, next_row, next_col)
        if fall_in_whirlpool:
            last_coordinates = next_row, next_col
            field, ship_row, ship_col, next_row, next_col = (
                mark_past_moves(field, ship_row, ship_col, next_row, next_col))
            break

        have_fish = fish_check(field, next_row, next_col)
        if have_fish:
            amount = int(field[next_row][next_col])
            fish_amount += amount

        field, ship_row, ship_col, next_row, next_col = (
            mark_past_moves(field, ship_row, ship_col, next_row, next_col))

    print_result(field, fish_amount, quota_goal, fall_in_whirlpool, last_coordinates)


if __name__ == '__main__':
    main()




# def is_valid(value, max_value):
#     return 0 <= value < max_value
#
#
# def next_move(command, current_row, current_col):
#     if command == 'up':
#         if is_valid(current_row-1, size):
#             return current_row-1, current_col
#         return current_row + (size-1), current_col
#     if command == 'down':
#         if is_valid(current_row+1, size):
#             return current_row+1, current_col
#         return current_row - (size-1), current_col
#     if command == 'left':
#         if is_valid(current_col-1, size):
#             return current_row, current_col-1
#         return current_row, current_col + (size - 1)
#     if command == 'right':
#         if is_valid(current_col+1, size):
#             return current_row, current_col+1
#         return current_row, current_col - (size - 1)
#
#
# size = int(input())
# fishing_area = []
# fish_amount = 0
# boat_row, boat_col = None, None
# whirlpool = False
#
# for r in range(size):
#     row = list(input())
#     fishing_area.append(row)
#     if 'S' in row:
#         boat_row = r
#         boat_col = row.index('S')
#         start_row = boat_row
#         start_col = boat_col
#
# while True:
#     line = input()
#     if line == 'collect the nets':
#         fishing_area[boat_row][boat_col] = "S"
#         break
#     next_row, next_col = next_move(line, boat_row, boat_col)
#
#     if fishing_area[next_row][next_col] == "W":
#         fishing_area[boat_row][boat_col] = '-'
#         boat_row, boat_col = next_row, next_col
#         fishing_area[boat_row][boat_col] = 'W'
#         last_coordinates = boat_row, boat_col
#         print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
#               f" Last coordinates of the ship: [{','.join(map(str, last_coordinates))}]")
#         whirlpool = True
#         break
#     if fishing_area[next_row][next_col].isdigit():
#         passage = int(fishing_area[next_row][next_col])
#         fish_amount += passage
#
#     fishing_area[boat_row][boat_col] = 'S'
#     fishing_area[boat_row][boat_col] = "-"
#     boat_row, boat_col = next_row, next_col
#     fishing_area[boat_row][boat_col] = "-"
#
# if fish_amount >= 20 and not whirlpool:
#     print(f"Success! You managed to reach the quota!")
# elif fish_amount < 20 and not whirlpool:
#     diff = 20 - fish_amount
#     print(f"You didn't catch enough fish and didn't reach the quota!"
#           f" You need {diff} tons of fish more.")
# if fish_amount > 0 and not whirlpool:
#     print(f"Amount of fish caught: {fish_amount} tons.")
# if not whirlpool:
#     for row_ in fishing_area:
#         print(''.join(row_))
#
