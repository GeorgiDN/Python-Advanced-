EMPTY_POSITION = '.'
ROWS = 6

def next_move(pl_row, pl_col, direction):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    d_row, d_col = directions[direction][0], directions[direction][1]
    next_row, next_col = pl_row + d_row, pl_col + d_col
    return next_row, next_col


def create(matrix, value, next_row, next_col):
    if matrix[next_row][next_col] == EMPTY_POSITION:
        matrix[next_row][next_col] = value
    return matrix


def update(matrix, value, next_row, next_col):
    if matrix[next_row][next_col].isdigit() or matrix[next_row][next_col].isalpha():
        matrix[next_row][next_col] = value
    return matrix


def delete(matrix, next_row, next_col):
    matrix[next_row][next_col] = EMPTY_POSITION
    return matrix


def read(matrix, next_row, next_col):
    if matrix[next_row][next_col].isdigit() or matrix[next_row][next_col].isalpha():
        print(matrix[next_row][next_col])


def main():
    matrix = [input().split() for _ in range(ROWS)]
    coordinates = input()
    pl_row, pl_col = int(coordinates[1]), int(coordinates[4])

    while True:
        command_input = input()
        if command_input == 'Stop':
            break

        command_info = command_input.split(', ')
        command = command_info[0]
        direction = command_info[1]

        next_row, next_col = next_move(pl_row, pl_col, direction)

        if command == 'Create':
            value = command_info[2]
            matrix = create(matrix, value, next_row, next_col)

        elif command == 'Update':
            value = command_info[2]
            matrix = update(matrix, value, next_row, next_col)

        elif command == 'Delete':
            matrix = delete(matrix, next_row, next_col)

        elif command == 'Read':
            read(matrix, next_row, next_col)

        pl_row, pl_col = next_row, next_col

    for row in matrix:
        print(*row)


if __name__ == '__main__':
    main()
