def is_valid_index(idx, size):
    return 0 <= idx < size


def check_for_items_to_collect(symbol, collected_decorations):
    if symbol in collected_decorations:
        collected_decorations[symbol] += 1
    return collected_decorations


def check_if_all_items_are_collected(collected_decorations, cookies, decorations, gifts):
    all_collected = collected_decorations['C'] == cookies and collected_decorations[
        'D'] == decorations and collected_decorations['G'] == gifts
    return all_collected


def take_positions_and_data(field, my_row, my_col, cookies, gifts, decorations, rows, cols):
    for r in range(rows):
        row = input().split()
        field.append(row)
        if 'Y' in row:
            my_row = r
            my_col = row.index('Y')
        if 'D' in row or 'C' or 'G' in row:
            cookies += row.count('C')
            gifts += row.count('G')
            decorations += row.count('D')

    return field, my_row, my_col, cookies, gifts, decorations


def validate_directions(next_row, next_col, rows, cols, direction):
    revert_moves = {'up': next_row + rows,
                    'down': next_row - rows,
                    'left': next_col + cols,
                    'right': next_col - cols
                    }

    if not is_valid_index(next_row, rows):
        next_row = revert_moves[direction]

    elif not is_valid_index(next_col, cols):
        next_col = revert_moves[direction]

    return next_row, next_col


def next_move(field, my_row, my_col, steps, direction, rows, cols, collected_decorations,
              all_collected_items, cookies, gifts, decorations):
    possible_moves = {'up': [-1, 0],
                      'down': [1, 0],
                      'left': [0, -1],
                      'right': [0, 1]
                      }

    past_moves = []

    for step in range(steps):
        next_row, next_col = my_row + possible_moves[direction][0], my_col + possible_moves[direction][1]

        next_row, next_col = validate_directions(next_row, next_col, rows, cols, direction)
        my_row, my_col = next_row, next_col
        moves = (next_row, next_col)
        if moves not in past_moves:
            past_moves.append(moves)

    for move in past_moves:
        r, c = int(move[0]), int(move[1])
        symbol = field[r][c]
        collected_decorations = check_for_items_to_collect(symbol, collected_decorations)
        all_collected_items = check_if_all_items_are_collected(collected_decorations, cookies, decorations, gifts)

        if all_collected_items:
            field[r][c] = "x"
            field[r][c] = "Y"
            break
        field[r][c] = "Y"  # just for temporary check the position
        field[r][c] = "x"

    return field, my_row, my_col, collected_decorations, all_collected_items, cookies, gifts, decorations


def print_result(field, collected_decorations, all_collected_items):
    if all_collected_items:
        print("Merry Christmas!")

    print("You've collected:\n"
          f"- {collected_decorations['D']} Christmas decorations\n"
          f"- {collected_decorations['G']} Gifts\n"
          f"- {collected_decorations['C']} Cookies")

    for r in field:
        print(' '.join(r))


def main():
    cookies = 0
    gifts = 0
    decorations = 0

    all_collected_items = False
    collected_decorations = {'C': 0,
                             'G': 0,
                             'D': 0}
    field = []
    my_row, my_col = 0, 0
    rows, cols = list(map(int, input().split(', ')))

    field, my_row, my_col, cookies, gifts, decorations = (
        take_positions_and_data(field, my_row, my_col, cookies, gifts, decorations, rows, cols))

    start_row, start_col = my_row, my_col

    while True:
        if all_collected_items:
            field[start_row][start_col] = 'x'
            break

        command = input()
        if command == 'End':
            field[start_row][start_col] = 'x'
            field[my_row][my_col] = 'Y'
            break

        direction, steps = command.split('-')
        steps = int(steps)

        field, my_row, my_col, collected_decorations, all_collected_items, cookies, gifts, decorations = (
            next_move(field, my_row, my_col, steps, direction, rows, cols, collected_decorations, all_collected_items,
                      cookies, gifts, decorations))

        all_collected_items = check_if_all_items_are_collected(collected_decorations, cookies, decorations, gifts)

    print_result(field, collected_decorations, all_collected_items)


if __name__ == '__main__':
    main()
