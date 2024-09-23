def fill_the_route(rows):
    route = []
    tunel = []
    for r in range(rows):
        row = input().split()
        route.append(row)
        if "T" in row:
            for c in range(rows):
                if route[r][c] == "T":
                    tunel.append([r, c])

    return route, tunel


def next_move(c_row, c_col, direction):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    row, col = moves[direction][0], moves[direction][1]
    new_row = c_row + row
    new_col = c_col + col
    return new_row, new_col


def main():
    rows = int(input())
    car = input()
    route, tunnel = fill_the_route(rows)
    t_start_row, t_start_col = tunnel[0][0], tunnel[0][1]
    t_end_row, t_end_col = tunnel[1][0], tunnel[1][1]
    tunel, finish, empty = "T", "F", "."
    is_finished = False
    passed_kilometers = 0
    c_row, c_col = 0, 0

    while True:
        direction = input()
        if direction == "End":
            print(f"Racing car {car} DNF.")
            route[c_row][c_col] = "C"
            break

        if is_finished:
            print(f"Racing car {car} finished the stage!")
            route[c_row][c_col] = "C"
            break

        next_row, next_col = next_move(c_row, c_col, direction)
        passed_kilometers += 10

        if route[next_row][next_col] == "T":
            if next_row == t_start_row and next_col == t_start_col:
                c_row, c_col = t_end_row, t_end_col
            else:
                c_row, c_col = t_start_row, t_start_col
            route[c_row][c_col] = empty
            route[t_start_row][t_start_col] = empty
            route[t_end_row][t_end_col] = empty
            passed_kilometers += 20
            continue

        elif route[next_row][next_col] == finish:
            is_finished = True

        route[c_row][c_col] = empty
        c_row, c_col = next_row, next_col
        route[c_row][c_col] = empty

    print(f"Distance covered {passed_kilometers} km.")
    for row in route:
        print("".join(row))


if __name__ == '__main__':
    main()
