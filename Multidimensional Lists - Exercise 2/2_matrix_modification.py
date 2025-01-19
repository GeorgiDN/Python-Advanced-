def is_valid_index(value, max_value):
    return 0 <= value < max_value


size = int(input())
invalid_message = 'Invalid coordinates'

commands = {
    'Add': lambda mtrx, r, c, value: mtrx[r][c] + value,
    'Subtract': lambda mtrx, r, c, value: mtrx[r][c] - value
}

matrix = [[int(x) for x in input().split()] for _ in range(size)]

while True:
    command_info = input().split()
    if command_info[0] == 'END':
        break

    command, row, col, num = command_info[0], int(command_info[1]), int(command_info[2]), int(command_info[3])
    if not is_valid_index(row, size) or not is_valid_index(col, size):
        print(invalid_message)
    else:
        matrix[row][col] = commands[command](matrix, row, col, num)

[print(' '.join(map(str, row))) for row in matrix]

# for row in matrix:
#     print(' '.join(map(str, row)))



# def is_valid_index(idx, number):
#     return 0 <= idx < number


# def add(mtrx, curr_row, col, val, size):
#     if is_valid_index(curr_row, size) and is_valid_index(col, size):
#         mtrx[curr_row][col] += val
#     else:
#         print(f"Invalid coordinates")
#     return mtrx


# def subtract(mtrx, curr_row, col, val, size):
#     if is_valid_index(curr_row, size) and is_valid_index(col, size):
#         mtrx[curr_row][col] -= val
#     else:
#         print(f"Invalid coordinates")
#     return mtrx


# rows = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]

# while True:
#     command = input()
#     if command == "END":
#         break

#     data = command.split()
#     current_command, row, column, value = data[0], int(data[1]), int(data[2]), int(data[3])

#     if current_command == "Add":
#         matrix = add(matrix, row, column, value, rows)
#     elif current_command == "Subtract":
#         matrix = subtract(matrix, row, column, value, rows)

# print('\n'.join(' '.join(map(str, r)) for r in matrix))

# # for r in matrix:
# #     print(" ".join(map(str, r)))
