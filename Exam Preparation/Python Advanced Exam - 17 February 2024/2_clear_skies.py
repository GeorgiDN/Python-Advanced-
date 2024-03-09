def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col, size_):
    if command == "up" and is_valid(current_row - 1, size_):
        return current_row - 1, current_col
    if command == "down" and is_valid(current_row + 1, size_):
        return current_row + 1, current_col
    if command == "left" and is_valid(current_col - 1, size_):
        return current_row, current_col - 1
    if command == "right" and is_valid(current_col + 1, size_):
        return current_row, current_col + 1
    return None, None


def fill_the_field_and_find_jet_position(size_, jet_row_, jet_col_):
    field_ = []
    for r in range(size_):
        row = list(input())
        field_.append(row)
        if "J" in row:
            jet_row_ = r
            jet_col_ = row.index("J")

    return field_, jet_row_, jet_col_


def have_enemies_left(matrix, size_):
    enemy_left = False
    for row in range(size_):
        for col in range(size_):
            if matrix[row][col] == "E":
                enemy_left = True
                break
    return enemy_left


def main():
    size = int(input())
    jet_row, jet_col = None, None
    field, jet_row, jet_col = fill_the_field_and_find_jet_position(size, jet_row, jet_col)
    jet_armour = 300

    line = ' '

    while line:
        line = input()

        next_row, next_col = next_move(line, jet_row, jet_col, size)
        field[jet_row][jet_col] = "-"

        if field[next_row][next_col] == "E":
            field[next_row][next_col] = "-"
            if not have_enemies_left(field, size):
                print("Mission accomplished, you neutralized the aerial threat!")
                jet_row, jet_col = next_row, next_col
                field[jet_row][jet_col] = "J"
                break
            else:
                jet_armour -= 100
                if jet_armour <= 0:
                    jet_row, jet_col = next_row, next_col
                    field[jet_row][jet_col] = "J"
                    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet_row}, {jet_col}]!")
                    break

        elif field[next_row][next_col] == "R":
            jet_armour = 300
            field[next_row][next_col] = "-"

        jet_row, jet_col = next_row, next_col
        field[jet_row][jet_col] = "J"

    for row_ in field:
        print(''.join(row_))


if __name__ == "__main__":
    main()
