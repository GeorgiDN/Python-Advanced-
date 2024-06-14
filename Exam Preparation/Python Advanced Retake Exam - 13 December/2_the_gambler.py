# https://judge.softuni.org/Contests/Practice/Index/4226#1

def is_valid_index(value, max_value):
    return 0 <= value < max_value


def next_move(rows, row, col, direction):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    d_row, d_col = moves[direction]
    row = (row + d_row)
    col = (col + d_col)
    if is_valid_index(row, rows) and is_valid_index(col, rows):
        return row, col
    return None, None


def fill_the_matrix_and_take_positions(field, g_row, g_col, size):
    for r in range(size):
        row = list(input())
        field.append(row)
        if "G" in row:
            g_row = r
            g_col = row.index("G")
    return field, g_row, g_col


def out_of_field_check(next_row, next_col):
    return next_row is None or next_col is None


def mark_past_moves(field, g_row, g_col, next_row, next_col):
    g_row, g_col = next_row, next_col
    field[g_row][g_col] = "G"
    return field, g_row, g_col, next_row, next_col


def jackpot_check(field, gambler_row, gambler_col, next_row, next_col, amount, jackpot):
    if field[next_row][next_col] == "J":
        jackpot = True
        amount += 100000
        field, gambler_row, gambler_col, next_row, next_col = (
            mark_past_moves(field, gambler_row, gambler_col, next_row, next_col))
        print("You win the Jackpot!")
    return field, gambler_row, gambler_col, next_row, next_col, amount, jackpot


def penalty_check(field, next_row, next_col, amount, game_over):
    if field[next_row][next_col] == "P":
        amount -= 200
        if amount <= 0:
            print("Game over! You lost everything!")
            game_over = True
    return amount, game_over


def print_matrix(game_over, field, amount):
    if not game_over:
        print(f"End of the game. Total amount: {amount}$")
        for row in field:
            print(''.join(row))


def main():
    size = int(input())
    field = []
    gambler_row, gambler_col = None, None
    amount = 100
    game_over, jackpot = False, False

    field, gambler_row, gambler_col = (
        fill_the_matrix_and_take_positions(field, gambler_row, gambler_col, size))

    while True:
        line = input()
        if line == "end":
            break
        next_row, next_col = next_move(size, gambler_row, gambler_col, line)
        field[gambler_row][gambler_col] = '-'

        game_over = out_of_field_check(next_row, next_col)
        if game_over:
            print("Game over! You lost everything!")
            break

        if field[next_row][next_col] == "W":
            amount += 100

        amount, game_over = \
            penalty_check(field, next_row, next_col, amount, game_over)
        if game_over:
            break

        field, gambler_row, gambler_col, next_row, next_col, amount, jackpot =\
            jackpot_check(field, gambler_row, gambler_col, next_row, next_col, amount, jackpot)

        if jackpot:
            break

        field, gambler_row, gambler_col, next_row, next_col = (
            mark_past_moves(field, gambler_row, gambler_col, next_row, next_col))

    print_matrix(game_over, field, amount)


if __name__ == '__main__':
    main()




####################################################################################################################
# def is_valid_index(value, max_value):
#     return 0 <= value < max_value
#
#
# def next_move(command, row, col):
#     if command == "up" and is_valid_index(row - 1, size):
#         return row - 1, col
#     if command == "down" and is_valid_index(row + 1, size):
#         return row + 1, col
#     if command == "left" and is_valid_index(col - 1, size):
#         return row, col - 1
#     if command == "right" and is_valid_index(col + 1, size):
#         return row, col + 1
#     return None, None
#
#
# size = int(input())
# field = []
# gambler_row, gambler_col = None, None
# amount = 100
# game_over = False
#
# for r in range(size):
#     row = list(input())
#     field.append(row)
#     if "G" in row:
#         gambler_row = r
#         gambler_col = row.index("G")
#         start_row = gambler_row
#         start_col = gambler_col
#
# while True:
#     line = input()
#     if line == "end":
#         break
#     next_row, next_col = next_move(line, gambler_row, gambler_col)
#     field[gambler_row][gambler_col] = '-'
#     if next_row is None or next_col is None:
#         print("Game over! You lost everything!")
#         game_over = True
#         break
#     if field[next_row][next_col] == "W":
#         amount += 100
#     if field[next_row][next_col] == "P":
#         amount -= 200
#         if amount <= 0:
#             print("Game over! You lost everything!")
#             game_over = True
#             break
#     if field[next_row][next_col] == "J":
#         amount += 100000
#         gambler_row, gambler_col = next_row, next_col
#         field[gambler_row][gambler_col] = "G"
#         print("You win the Jackpot!")
#         break
#     gambler_row, gambler_col = next_row, next_col
#     field[gambler_row][gambler_col] = "G"
#
# if not game_over:
#     print(f"End of the game. Total amount: {amount}$")
#     for row in field:
#         print(''.join(row))
