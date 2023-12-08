rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input()
    if command == "END":
        break

    command = command.split()
    operator = command[0]
    row = int(command[1])
    col = int(command[2])
    val = int(command[3])
    if row in range(rows) and col in range(rows):
        if operator == 'Add':
            matrix[row][col] += val
        elif operator == "Subtract":
            matrix[row][col] -= val
    else:
        print('Invalid coordinates')

for el in matrix:
    print(*el)




# def matrix_modification(modification, r, c, val):
#     if r in range(size) and c in range(size):
#         if modification == "Add":
#             matrix[r][c] += val
#         elif modification == "Subtract":
#             matrix[r][c] -= val
#     else:
#         print("Invalid coordinates")


# size = int(input())
# matrix = []

# for _ in range(size):
#     matrix.append([int(x) for x in input().split()])

# while True:
#     command = input()
#     if command.startswith("END"):
#         break
#     action = command.split()[0]
#     row, col, value = [int(x) for x in command.split()[1:]]
#     matrix_modification(action, row, col, value)

# [print(" ".join([str(x) for x in element])) for element in matrix]
