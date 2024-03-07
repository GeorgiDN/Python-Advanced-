rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]
max_square_sum = 0
square_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col+1] and matrix[row+1][col] == matrix[row+1][col+1] \
                and matrix[row][col] == matrix[row+1][col+1]:
            current_square = [matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]]
            square_matrix.append(current_square)

print(len(square_matrix))




# rows, columns = [int(x) for x in input().split(" ")]

# matrix = []
# for _ in range(rows):
#     matrix.append([x for x in input().split(' ')])

# squares = []

# for row in range(rows - 1):
#     for col in range(columns - 1):
#         submatrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]
#         if submatrix[0][0] == submatrix[0][1] and submatrix[1][0] == submatrix[1][1] \
#                 and submatrix[0][0] == submatrix[1][1]:
#             squares.append(submatrix)

# print(len(squares))
