def fill_the_field_and_find_coals_and_miner(size, field, miner_row, miner_col, coals_number):
    for r in range(size):
        row = input().split()
        field.append(row)
        if "s" in row:
            miner_row = r
            miner_col = row.index('s')
        if "c" in row:
            coals_number += row.count("c")

    return field, miner_row, miner_col, coals_number


def is_valid_index(value, max_value):
    return 0 <= value < max_value


def next_move(current_direction, curr_row, curr_col, size_):
    all_directions = {"up": [curr_row - 1, curr_col],
                      "down": [curr_row + 1, curr_col],
                      "right": [curr_row, curr_col + 1],
                      "left": [curr_row, curr_col - 1]}

    new_row, new_col = all_directions[current_direction][0], all_directions[current_direction][1]
    if is_valid_index(new_row, size_) \
            and is_valid_index(new_col, size_):
        return new_row, new_col
    return None, None


def main():
    size = int(input())
    directions = input().split()
    field = []
    miner_row, miner_col = None, None
    coals_number = 0
    game_over = False
    field, miner_row, miner_col, coals_number = fill_the_field_and_find_coals_and_miner(size, field, miner_row, miner_col, coals_number)

    for direction in directions:
        next_row, next_col = next_move(direction, miner_row, miner_col, size)
        if next_row is None or next_col is None:
            continue

        if field[next_row][next_col] == "c":
            coals_number -= 1
            field[miner_row][miner_col] = "*"
            if coals_number == 0:
                miner_row, miner_col = next_row, next_col
                print(f"You collected all coal! ({miner_row}, {miner_col})")
                field[miner_row][miner_col] = "s"
                break

        elif field[next_row][next_col] == "e":
            field[miner_row][miner_col] = "*"
            miner_row, miner_col = next_row, next_col
            print(f"Game over! ({miner_row}, {miner_col})")
            game_over = True
            field[miner_row][miner_col] = "s"
            break

        field[miner_row][miner_col] = "*"
        miner_row, miner_col = next_row, next_col
        field[miner_row][miner_col] = "s"

    if coals_number > 0 and not game_over:
        print(f"{coals_number} pieces of coal left. ({miner_row}, {miner_col})")


if __name__ == '__main__':
    main()
