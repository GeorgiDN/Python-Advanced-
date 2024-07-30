def fill_matrix_and_takes_positions(s_row, s_col, rows):
    field = []
    for idx in range(rows):
        row = list(input())
        field.append(row)
        if "S" in row:
            s_row = idx
            s_col = row.index("S")

    return field, s_row, s_col


def next_move(s_row, s_col, direction):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    row, col = moves[direction][0], moves[direction][1]
    next_row = (s_row + row)
    next_col = (s_col + col)

    return next_row, next_col


def main():
    rows = int(input())
    s_row, s_col = 0, 0
    field, s_row, s_col, = (
        fill_matrix_and_takes_positions(s_row, s_col, rows))
    naval_mine, cruiser, empty = "*", "C", "-"
    hit_cruisers = 0
    reached_mines = 0
    mission_accomplished = False
    failed_mission = False
    last_row, last_col = None, None

    while True:
        if mission_accomplished or failed_mission:
            break

        direction = input()
        next_row, next_col = next_move(s_row, s_col, direction)

        if field[next_row][next_col] == naval_mine:
            reached_mines += 1
            if reached_mines == 3:
                failed_mission = True
                last_row, last_col = next_row, next_col

        elif field[next_row][next_col] == cruiser:
            hit_cruisers += 1
            if hit_cruisers == 3:
                mission_accomplished = True

        field[s_row][s_col] = empty
        s_row, s_col = next_row, next_col
        field[s_row][s_col] = "S"

    if mission_accomplished:
        print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
    elif failed_mission:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{last_row}, {last_col}]!")

    for row in field:
        print("".join(row))


if __name__ == "__main__":
    main()
