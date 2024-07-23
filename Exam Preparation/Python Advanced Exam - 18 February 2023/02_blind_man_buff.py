def is_valid_index(idx, value):
    return 0 <= idx < value


def fill_matrix_and_takes_positions(m_row, m_col, rows):
    field = []
    for idx in range(rows):
        row = input().split()
        field.append(row)
        if "B" in row:
            m_row = idx
            m_col = row.index("B")
    return field, m_row, m_col


def next_move(m_row, m_col, direction, rows, cows):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    row, col = moves[direction][0], moves[direction][1]
    next_row = (m_row + row) if is_valid_index(m_row + row, rows) else None
    next_col = (m_col + col) if is_valid_index(m_col + col, cows) else None

    return next_row, next_col


def main():
    rows, cows = list(map(int, input().split()))
    m_row, m_col = 0, 0
    field, m_row, m_col = fill_matrix_and_takes_positions(m_row, m_col, rows)
    obstacle, player, empty = "O", "P", "-"
    moves_made, touched_opponents = 0, 0

    while True:
        if touched_opponents == 3:
            break
        direction = input()
        if direction == "Finish":
            break

        next_row, next_col = next_move(m_row, m_col, direction, rows, cows)
        if next_row is None or next_col is None or field[next_row][next_col] == obstacle:
            continue

        if field[next_row][next_col] == player:
            touched_opponents += 1

        moves_made += 1
        field[m_row][m_col] = empty
        m_row, m_col = next_row, next_col
        field[next_row][next_col] = player

    print("Game over!")
    print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")


if __name__ == '__main__':
    main()
