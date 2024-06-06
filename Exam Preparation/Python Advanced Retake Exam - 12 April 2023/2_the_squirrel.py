def is_valid_index(size_, idx):
    return 0 <= idx < size_


def next_move(size_, row, col, line):
    all_directions = {"up": [row - 1, col],
                      "down": [row + 1, col],
                      "right": [row, col + 1],
                      "left": [row, col - 1]}

    new_row, new_col = all_directions[line][0], all_directions[line][1]
    if is_valid_index(size_, new_row) \
            and is_valid_index(size_, new_col):
        return new_row, new_col
    return None, None


def fill_the_matrix_and_take_positions(n_size, s_row, s_col, hzn_count):
    matrix = []
    for r in range(n_size):
        row = list(input())
        matrix.append(row)
        if "s" in row:
            s_row = r
            s_col = row.index("s")
        if "h" in row:
            hzn_count += row.count("h")
    return matrix, s_row, s_col, hzn_count


def check_if_squirrel_is_out_of_boundaries(next_row, next_col):
    return next_row is None or next_col is None


def check_if_squirrel_is_in_trap(matrix, next_row, next_col):
    return matrix[next_row][next_col] == "t"


def check_for_hazelnut(field, next_row, next_col, hazelnuts, collected_three_hazelnut):
    if field[next_row][next_col] == "h":
        hazelnuts += 1
    collected_three_hazelnut = hazelnuts == 3
    return hazelnuts, collected_three_hazelnut


def print_result(collected_three_hazelnut, step_in_trap, out_of_boundaries, hazelnuts, hazelnut_count):
    possible_results = [out_of_boundaries, step_in_trap, collected_three_hazelnut]
    result_for_print = {out_of_boundaries: 'The squirrel is out of the field.',
                        step_in_trap: 'Unfortunately, the squirrel stepped on a trap...',
                        collected_three_hazelnut: 'Good job! You have collected all hazelnuts!'}

    if any(possible_results):
        true_index = next(i for i, condition in enumerate(possible_results) if condition)
        print(result_for_print[possible_results[true_index]])
    else:
        print("There are more hazelnuts to collect.")

    print(f"Hazelnuts collected: {hazelnuts}")


def main():
    size = int(input())
    directions = input().split(', ')
    hazelnut_count = 0
    hazelnuts = 0
    collected_three_hazelnut = False
    step_in_trap = False
    out_of_boundaries = False
    squirrel_row, squirrel_col = 0, 0

    field, squirrel_row, squirrel_col, hazelnut_count = (
        fill_the_matrix_and_take_positions(size, squirrel_row, squirrel_col, hazelnut_count))

    for direction in directions:
        if collected_three_hazelnut or step_in_trap or out_of_boundaries:
            break

        next_row, next_col = next_move(size, squirrel_row, squirrel_col, direction)

        out_of_boundaries = check_if_squirrel_is_out_of_boundaries(next_row, next_col)
        if out_of_boundaries:
            field[squirrel_row][squirrel_col] = "*"
            continue
        else:
            step_in_trap = check_if_squirrel_is_in_trap(field, next_row, next_col)
            if not step_in_trap:
                hazelnuts, collected_three_hazelnut = (
                    check_for_hazelnut(field, next_row, next_col, hazelnuts, collected_three_hazelnut))

        field[squirrel_row][squirrel_col] = "*"
        squirrel_row, squirrel_col = next_row, next_col
        field[squirrel_row][squirrel_col] = "s"  # where is squirrel

    print_result(collected_three_hazelnut, step_in_trap, out_of_boundaries, hazelnuts, hazelnut_count)


if __name__ == '__main__':
    main()

