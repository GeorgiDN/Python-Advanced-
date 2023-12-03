
rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
max_sum = 0
max_submatrix = []
for row in range(rows - 1):
    for col in range(columns - 1):
        submatrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]
        sum_elements = sum(submatrix[0]) + sum(submatrix[1])
        if sum_elements > max_sum:
            max_sum = sum_elements
            max_submatrix = submatrix

for row in max_submatrix:
    print(" ".join(str(x) for x in row))
print(max_sum)
