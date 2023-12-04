rows, columns = [int(x) for x in input().split(" ")]

matrix = []
for _ in range(rows):
    matrix.append([x for x in input().split(' ')])

squares = []

for row in range(rows - 1):
    for col in range(columns - 1):
        submatrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]
        if submatrix[0][0] == submatrix[0][1] and submatrix[1][0] == submatrix[1][1] \
                and submatrix[0][0] == submatrix[1][1]:
            squares.append(submatrix)

print(len(squares))
