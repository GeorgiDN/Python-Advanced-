def is_valid_index(idx, value):
    return 0 <= idx < value


def fill_matrix_and_take_pos(curr_row, curr_col, rows, letter, bomb_row, bomb_col):
    field = []
    for idx in range(rows):
        row = list(input())
        field.append(row)
        if letter in row:
            curr_row = idx
            curr_col = row.index(letter)
        if "B" in row:
            bomb_row = idx
            bomb_col = row.index("B")

    return field, curr_row, curr_col, bomb_row, bomb_col


def next_move(curr_row, curr_col, direction, rows, cows):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    row, col = moves[direction][0], moves[direction][1]
    next_row = (curr_row + row) if is_valid_index(curr_row + row, rows) else None
    next_col = (curr_col + col) if is_valid_index(curr_col + col, cows) else None

    return next_row, next_col


def print_terrorist_win_message(seconds):
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {seconds} second/s.")


def mark_passed_moves(field, c_row, c_col, next_row, next_col, empty):
    field[c_row][c_col] = empty
    c_row, c_col = next_row, next_col
    field[c_row][c_col] = empty
    return field, c_row, c_col, next_row, next_col


def main():
    rows, cows = list(map(int, input().split(", ")))
    c_row, c_col = 0, 0
    bomb_row, bomb_col = 0, 0
    counter, terrorist, bomb, empty = "C", "T", "B", "*"
    field, c_row, c_col, bomb_row, bomb_col = (
        fill_matrix_and_take_pos(c_row, c_col, rows, counter, bomb_row, bomb_col))
    start_row, start_col = c_row, c_col
    seconds_left, defuse_time = 16, 4

    while True:
        if seconds_left <= 0:
            print_terrorist_win_message(seconds=0)
            break

        direction = input()
        if direction == "defuse":
            if (c_row, c_col) == (bomb_row, bomb_col):
                if seconds_left >= defuse_time:
                    field[c_row][c_col] = "D"
                    print("Counter-terrorist wins!")
                    print(f"Bomb has been defused: {seconds_left - defuse_time} second/s remaining.")
                    break

                elif seconds_left < defuse_time:
                    field[c_row][c_col] = "X"
                    time_needed = abs(seconds_left - defuse_time)
                    print_terrorist_win_message(time_needed)
                    break

            else:
                seconds_left -= 2
                continue

        next_row, next_col = next_move(c_row, c_col, direction, rows, cows)
        if next_row is None or next_col is None:
            seconds_left -= 1
            continue

        if field[next_row][next_col] == terrorist:
            field, c_row, c_col, next_row, next_col = \
                mark_passed_moves(field, c_row, c_col, next_row, next_col, empty)
            field[bomb_row][bomb_col] = bomb
            print("Terrorists win!")
            break

        seconds_left -= 1
        field, c_row, c_col, next_row, next_col = \
        mark_passed_moves(field, c_row, c_col, next_row, next_col, empty)

    field[start_row][start_col] = counter
    for row in field:
        print(''.join(row))


if __name__ == '__main__':
    main()