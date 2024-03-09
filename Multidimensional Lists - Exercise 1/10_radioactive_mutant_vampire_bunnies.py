def fill_the_field_and_find_player(num_of_rows, cols, matrix, player_row, player_col):
    for r in range(num_of_rows):
        row = list(input())
        matrix.append(row)
        if "P" in row:
            player_row = r
            player_col = row.index('P')
    return matrix, player_row, player_col


def is_valid_index(value, max_value):
    return 0 <= value < max_value


def next_move(current_direction, current_row, current_col, num_of_rows, cols):
    if current_direction == "U" and is_valid_index(current_row - 1, num_of_rows):
        return current_row - 1, current_col
    if current_direction == "D" and is_valid_index(current_row + 1, num_of_rows):
        return current_row + 1, current_col
    if current_direction == "L" and is_valid_index(current_col - 1, cols):
        return current_row, current_col - 1
    if current_direction == "R" and is_valid_index(current_col + 1, cols):
        return current_row, current_col + 1
    return None, None


def bunny_spread(matrix, num_of_rows, cols, player_dead):
    bunny_coordinates = []
    for row in range(num_of_rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                bunny_coordinates.append([row, col])

    for coordinates in bunny_coordinates:
        b_row, b_col = coordinates[0], coordinates[1]
        if is_valid_index(b_row - 1, num_of_rows):  # up
            if matrix[b_row - 1][b_col] == "P":
                player_dead = True
            matrix[b_row - 1][b_col] = "B"
        if is_valid_index(b_row + 1, num_of_rows):
            if matrix[b_row + 1][b_col] == "P":
                player_dead = True
            matrix[b_row + 1][b_col] = "B"  # down
        if is_valid_index(b_col - 1, cols):
            if matrix[b_row][b_col - 1] == "P":
                player_dead = True
            matrix[b_row][b_col - 1] = "B"  # left
        if is_valid_index(b_col + 1, cols):
            if matrix[b_row][b_col + 1] == "P":
                player_dead = True
            matrix[b_row][b_col + 1] = "B"  # right

    return matrix, player_dead


def main():
    rows, columns = [int(x) for x in input().split()]
    field = []
    player_row, player_col = 0, 0
    player_is_dead = False
    player_won = False
    field, player_row, player_col = \
        fill_the_field_and_find_player(rows, columns, field, player_row, player_col)
    directions = list(input())

    for direction in directions:
        next_row, next_col = next_move(direction, player_row, player_col, rows, columns)
        if next_row is None or next_col is None:
            if not player_is_dead:
                player_won = True
                field[player_row][player_col] = "."
        else:
            if field[next_row][next_col] == "B":
                player_is_dead = True
                player_row, player_col = next_row, next_col
            else:
                field[player_row][player_col] = "."
                player_row, player_col = next_row, next_col
                field[player_row][player_col] = "P"

        field, player_is_dead = bunny_spread(field, rows, columns, player_is_dead)
        if player_won or player_is_dead:
            break

    [print(''.join(element)) for element in field]
    print(f"dead: {player_row} {player_col}") if player_is_dead else print(f"won: {player_row} {player_col}")


if __name__ == '__main__':
    main()
