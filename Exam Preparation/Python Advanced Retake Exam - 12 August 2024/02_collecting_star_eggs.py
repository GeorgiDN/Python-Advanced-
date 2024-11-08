def is_valid_index(idx, value):
    return 0 <= idx < value


def fill_matrix_and_takes_positions(p_row, p_col, rows):
    field = []
    for idx in range(rows):
        row = input().split()
        field.append(row)
        if "P" in row:
            p_row = idx
            p_col = row.index("P")

    return field, p_row, p_col


def next_move(p_row, p_col, direction, rows):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    row, col = moves[direction][0], moves[direction][1]
    next_row = (p_row + row) if is_valid_index(p_row + row, rows) else None
    next_col = (p_col + col) if is_valid_index(p_col + col, rows) else None

    return next_row, next_col


def main():

    rows = int(input())
    p_row, p_col = 0, 0
    field, p_row, p_col, = (
        fill_matrix_and_takes_positions(p_row, p_col, rows))

    empty, obstacle, star = ".", "#", "*"
    collected_stars = 2
    win = False
    lost = False

    while True:
        if win or lost:
            break
        direction = input()

        next_row, next_col = next_move(p_row, p_col, direction, rows)

        if next_row is None or next_col is None:
            field[p_row][p_col] = empty
            p_row, p_col = 0, 0
            if field[p_row][p_col] == star:
                collected_stars += 1
                if collected_stars == 10:
                    win = True
            field[p_row][p_col] = "P"
            continue

        elif field[next_row][next_col] == star:
            collected_stars += 1
            if collected_stars == 10:
                win = True

        elif field[next_row][next_col] == obstacle:
            collected_stars -= 1
            if collected_stars == 0:
                lost = True
            continue

        field[p_row][p_col] = empty
        p_row, p_col = next_row, next_col
        field[next_row][next_col] = "P"

    if win:
        print("You won! You have collected 10 stars.")
    elif lost:
        print("Game over! You are out of any stars.")

    print(f"Your final position is [{p_row}, {p_col}]")

    for row in field:
        print(" ".join(row))


if __name__ == "__main__":
    main()