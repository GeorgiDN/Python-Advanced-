def fill_the_matrix_and_find_alice(a_row, a_col, mtrx_size):
    matrix = []
    for r in range(mtrx_size):
        row = input().split()
        matrix.append(row)
        if "A" in row:
            a_row = r
            a_col = row.index('A')
    return matrix, a_row, a_col


def is_valid_index(value, max_value):
    return 0 <= value < max_value


def next_move(line, curr_row, curr_col, mtrx_size):
    all_directions = {"up": [curr_row - 1, curr_col],
                      "down": [curr_row + 1, curr_col],
                      "right": [curr_row, curr_col + 1],
                      "left": [curr_row, curr_col - 1]}

    new_row, new_col = all_directions[line][0], all_directions[line][1]
    if is_valid_index(new_row, mtrx_size) \
            and is_valid_index(new_col, mtrx_size):
        return new_row, new_col
    return None, None


def main():
    size = int(input())
    field = []
    alice_row, alice_col = None, None
    collected_bags = 0
    alice_go_to_party = False
    alice_left_wonderland = False

    field, alice_row, alice_col = fill_the_matrix_and_find_alice(alice_row, alice_col, size)
    direction = " "
    while direction:
        if alice_left_wonderland or alice_go_to_party:
            break
        direction = input()
        next_row, next_col = next_move(direction, alice_row, alice_col, size)
        if next_row is None or next_col is None:
            alice_left_wonderland = True
            field[alice_row][alice_col] = "*"
            break

        if field[next_row][next_col] == "R":
            alice_left_wonderland = True

        if field[next_row][next_col].isdigit():
            bags_of_tea = int(field[next_row][next_col])
            collected_bags += bags_of_tea

        field[alice_row][alice_col] = "*"
        alice_row, alice_col = next_row, next_col
        field[alice_row][alice_col] = "A"  # to check where is alice
        field[alice_row][alice_col] = "*"
        if collected_bags >= 10:
            alice_go_to_party = True

    if alice_go_to_party:
        print("She did it! She went to the party.")
    elif alice_left_wonderland:
        print("Alice didn't make it to the tea party.")

    [print(' '.join(curr_row)) for curr_row in field]
    # for curr_row in field:
    #     print(' '.join(curr_row))


if __name__ == '__main__':
    main()
