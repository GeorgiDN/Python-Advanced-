def is_valid_index(idx, number):
    return 0 <= idx < number


def add(mtrx, curr_row, col, val, size):
    if is_valid_index(curr_row, size) and is_valid_index(col, size):
        mtrx[curr_row][col] += val
    else:
        print(f"Invalid coordinates")
    return mtrx


def subtract(mtrx, curr_row, col, val, size):
    if is_valid_index(curr_row, size) and is_valid_index(col, size):
        mtrx[curr_row][col] -= val
    else:
        print(f"Invalid coordinates")
    return mtrx


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    data = command.split()
    current_command, row, column, value = data[0], int(data[1]), int(data[2]), int(data[3])

    if current_command == "Add":
        matrix = add(matrix, row, column, value, rows)
    elif current_command == "Subtract":
        matrix = subtract(matrix, row, column, value, rows)

print('\n'.join(' '.join(map(str, r)) for r in matrix))

# for r in matrix:
#     print(" ".join(map(str, r)))
