def is_valid_index(idx, value):
    return 0 <= idx < value


def fill_matrix_and_takes_pos(pl_row, pl_col, rows, player, total_stars):
    matrix = []
    for idx in range(rows):
        row = list(input())
        matrix.append(row)
        if player in row:
            pl_row = idx
            pl_col = row.index(player)
        if '*' in row:
            total_stars += row.count('*')

    return matrix, pl_row, pl_col, total_stars


def next_move(pl_row, pl_col, direction, rows):
    moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    d_row, d_col = moves[direction][0], moves[direction][1]

    next_row = (pl_row + d_row) % rows
    next_col = (pl_col + d_col) % rows

    return next_row, next_col


def main():
    rows = int(input())
    pl_row, pl_col = 0, 0
    total_stars = 0
    player, empty, star, ghost, freeze = 'P', '-', '*', 'G', 'F'
    matrix, pl_row, pl_col, total_stars = (
        fill_matrix_and_takes_pos(pl_row, pl_col, rows, player, total_stars))
    start_row, start_col = pl_row, pl_col
    health_left = 100
    matrix[pl_row][pl_col] = empty
    temporary_freeze = False

    while True:
        if health_left <= 0:
            print(f"Game over! Pacman last coordinates [{pl_row},{pl_col}]")
            break

        if total_stars == 0:
            print("Pacman wins! All the stars are collected.")
            break

        direction = input()

        if direction == 'end':
            print("Pacman failed to collect all the stars.")
            break

        next_row, next_col = next_move(pl_row, pl_col, direction, rows)

        if matrix[next_row][next_col] == star:
            total_stars -= 1

        if matrix[next_row][next_col] == ghost:
            if not temporary_freeze:
                health_left -= 50

        if matrix[next_row][next_col] == freeze:
            temporary_freeze = True
            pl_row, pl_col = next_row, next_col
            matrix[pl_row][pl_col] = empty
            continue

        temporary_freeze = False
        pl_row, pl_col = next_row, next_col
        matrix[pl_row][pl_col] = empty

    print(f"Health: {health_left}")
    if total_stars != 0:
        print(f"Uncollected stars: {total_stars}")

    matrix[pl_row][pl_col] = player
    for row in matrix:
        print(''.join(row))


if __name__ == '__main__':
    main()
