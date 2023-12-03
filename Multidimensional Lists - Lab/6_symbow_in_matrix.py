rows = int(input())
matrix = []
found_condition = False

for _ in range(rows):
    matrix.append([x for x in input()])

symbol = input()

for col in range(rows):
    for idx, row in enumerate(matrix):
        column = row[col]
        if column == symbol:
            print(f"({idx}, {col})")
            found_condition = True
            break

if not found_condition:
    print(f"{symbol} does not occur in the matrix")
