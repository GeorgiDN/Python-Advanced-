import sys
rows, columns = [int(x) for x in input().split(" ")]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(" ")])

max_sum = -sys.maxsize
max_submatrix = []
for row in range(rows - 2):
    for col in range(columns - 2):
        submatrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
            [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
            [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]

        sum_elements = sum(submatrix[0]) + sum(submatrix[1]) + sum(submatrix[2])
        if sum_elements > max_sum:
            max_sum = sum_elements
            max_submatrix = submatrix

print(f"Sum = {max_sum}")
for row in max_submatrix:
    print(" ".join(str(x) for x in row))
