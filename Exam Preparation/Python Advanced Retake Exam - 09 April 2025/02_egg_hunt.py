def is_valid_index(idx, value):
    return 0 <= idx < value


def fill_matrix_and_takes_pos(pl_row, pl_col, rows, player):
    matrix = []
    for idx in range(rows):
        row = list(input())
        # row = input().split()
        matrix.append(row)
        if player in row:
            pl_row = idx
            pl_col = row.index(player)

    return matrix, pl_row, pl_col


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
    # rows, cols = list(map(int, input().split(", ")))
    rows = int(input())
    pl_row, pl_col = 0, 0
    player, empty, egg, trap, flower = 'B', '.', 'E', 'T', 'F'
    matrix, pl_row, pl_col = (
        fill_matrix_and_takes_pos(pl_row, pl_col, rows, player))
    start_row, start_col = pl_row, pl_col
    collected_eggs = 5
    goal_eggs = 10
    matrix[pl_row][pl_col] = empty

    while True:

        if collected_eggs >= goal_eggs:
            print(f"Easter Bunny wins! Collected eggs: {collected_eggs}.")
            matrix[pl_row][pl_col] = player
            break

        if collected_eggs <= 0:
            print("Game over! Easter Bunny has no eggs left.")
            matrix[pl_row][pl_col] = player
            break

        direction = input()

        if direction == 'stop':
            matrix[pl_row][pl_col] = player
            print(f"Easter Bunny stopped hunting with {collected_eggs} eggs.")
            break

        next_row, next_col = next_move(pl_row, pl_col, direction, rows)

        if next_row is None or next_col is None:
            pl_row, pl_col = start_row, start_col
            continue

        if matrix[next_row][next_col] == egg:
            collected_eggs += 1

        if matrix[next_row][next_col] == trap:
            collected_eggs -= 1

        if matrix[next_row][next_col] == flower:
            collected_eggs *= 2

        matrix[pl_row][pl_col] = empty
        pl_row, pl_col = next_row, next_col
        matrix[pl_row][pl_col] = empty

    for row in matrix:
        print(''.join(row))


if __name__ == '__main__':
    main()
