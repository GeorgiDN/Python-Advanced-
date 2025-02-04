def is_valid_index(idx, value):
    return 0 <= idx < value


def fill_matrix_and_takes_pos(pl_row, pl_col, rows, player, bomb, bomb_row, bomb_col):
    matrix = []
    for idx in range(rows):
        row = list(input())
        matrix.append(row)
        if player in row:
            pl_row, pl_col = idx, row.index(player)
        if bomb in row:
            bomb_row, bomb_col = idx, row.index(bomb)

    return matrix, pl_row, pl_col, bomb_row, bomb_col


def next_move(pl_row, pl_col, direction, rows, cols):
    moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    d_row, d_col = moves[direction][0], moves[direction][1]
    next_row = (pl_row + d_row) if is_valid_index(pl_row + d_row, rows) else None
    next_col = (pl_col + d_col) if is_valid_index(pl_col + d_col, cols) else None
    return next_row, next_col


def print_terrorist_win_message(seconds):
    print('Terrorists win!')
    print('Bomb was not defused successfully!')
    print(f'Time needed: {seconds} second/s.')


def main():
    rows, cols = list(map(int, input().split(", ")))
    player_row, player_col = 0, 0
    bomb_row, bomb_col = 0, 0
    player, empty, terrorist, bomb = 'C', '*', 'T', 'B'
    matrix, player_row, player_col, bomb_row, bomb_col = (
        fill_matrix_and_takes_pos(player_row, player_col, rows, player, bomb, bomb_row, bomb_col))
    start_row, start_col = player_row, player_col
    seconds_left = 16
    defuse_time = 4

    while True:

        if seconds_left <= 0:
            print_terrorist_win_message(seconds=0)
            break

        direction = input()

        if direction == 'defuse':
            if (player_row, player_col) == (bomb_row, bomb_col):
                if defuse_time <= seconds_left:
                    matrix[bomb_row][bomb_col] = 'D'
                    time_needed = seconds_left - defuse_time
                    print('Counter-terrorist wins!')
                    print(f'Bomb has been defused: {time_needed} second/s remaining.')
                    break
                else:  # bomb explodes
                    time_needed = defuse_time - seconds_left
                    print_terrorist_win_message(time_needed)
                    matrix[bomb_row][bomb_col] = 'X'
                    break

            else:
                seconds_left -= 2
                continue

        next_row, next_col = next_move(player_row, player_col, direction, rows, cols)
        seconds_left -= 1

        if next_row is None or next_col is None:
            continue

        if matrix[next_row][next_col] == terrorist:
            print('Terrorists win!')
            matrix[next_row][next_col] = empty
            break

        player_row, player_col = next_row, next_col

    matrix[start_row][start_col] = player
    for row in matrix:
        print(''.join(row))


if __name__ == '__main__':
    main()

