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
