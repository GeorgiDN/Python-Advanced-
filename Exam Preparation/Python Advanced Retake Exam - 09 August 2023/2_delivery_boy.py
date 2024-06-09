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


def fill_the_matrix_and_take_positions(rows, b_row, b_col, field):
    field = []
    for r in range(rows):
        row = list(input())
        field.append(row)
        if "B" in row:
            b_row = r
            b_col = row.index("B")

    return field, b_row, b_col


def check_out_of_boundaries(next_row, next_col):
    return next_row is None or next_col is None


def main():
    field = []
    boy_row, boy_col = 0, 0
    rows, cols = [int(x) for x in input().split()]
    field, boy_row, boy_col = fill_the_matrix_and_take_positions(rows, boy_row, boy_col, field)
    out_of_field = False
    start_row, start_col = boy_row, boy_col

    while True:
        direction = input()
        if not direction:
            break

        next_row, next_col = next_move(rows, cols, boy_row, boy_col, direction)
        out_of_field = check_out_of_boundaries(next_row, next_col)
        if out_of_field:
            field[start_row][start_col] = ' '
            print('The delivery is late. Order is canceled.')
            break

        if field[next_row][next_col] == "*":
            continue

        if field[next_row][next_col] == "P":
            print('Pizza is collected. 10 minutes for delivery.')
            field[boy_row][boy_col] = '.'
            boy_row, boy_col = next_row, next_col
            field[next_row][next_col] = "R"
            continue

        if field[next_row][next_col] == "A":
            print("Pizza is delivered on time! Next order...")
            field[next_row][next_col] = "P"
            if field[boy_row][boy_col] != "R":
                field[boy_row][boy_col] = '.'
            field[start_row][start_col] = 'B'
            break

        if field[boy_row][boy_col] != "R":
            field[boy_row][boy_col] = "B"
            field[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        field[boy_row][boy_col] = '.'

    for r in field:
        print(''.join(r))


main()
