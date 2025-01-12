rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]
rectangular_matrix = []
max_sum = float('-inf')

for r in range(rows - 2):
    for c in range(cols - 2):
        submatrix_1 = [matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]]
        submatrix_2 = [matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]]
        submatrix_3 = [matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]]
        total_sum = sum(submatrix_1) + sum(submatrix_2) + sum(submatrix_3)
        if total_sum > max_sum:
            max_sum = total_sum
            rectangular_matrix = [submatrix_1, submatrix_2, submatrix_3]

print(f'Sum = {max_sum}')
[print(' '.join(map(str, row))) for row in rectangular_matrix]
# for row in rectangular_matrix:
#     print(' '.join(map(str, row)))


# import sys

# rows, cols = [int(x) for x in input().split()]
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# max_square_sum = -sys.maxsize
# max_submatrix = []

# for row in range(rows - 2):
#     for col in range(cols - 2):
#         submatrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
#                          [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
#                          [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]

#         current_square_sum = sum(submatrix[0]) + sum(submatrix[1]) + sum(submatrix[2])
#         if current_square_sum > max_square_sum:
#             max_square_sum = current_square_sum
#             max_submatrix.clear()
#             max_submatrix.append(submatrix[0])
#             max_submatrix.append(submatrix[1])
#             max_submatrix.append(submatrix[2])

# print(f"Sum = {max_square_sum}")
# for r in max_submatrix:
#     print(' '.join(map(str, r)))



# import sys
#
# rows, cols = [int(x) for x in input().split()]
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# max_square_sum = -sys.maxsize
# submatrix = []
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         current_square_sum = matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] \
#             + matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2] \
#             + matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]
#         if current_square_sum > max_square_sum:
#             max_square_sum = current_square_sum
#             submatrix.clear()
#             submatrix.append([matrix[row][col], matrix[row][col+1], matrix[row][col+2]])
#             submatrix.append([matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]])
#             submatrix.append([matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]])
#
# print(f"Sum = {max_square_sum}")
# for r in submatrix:
#     print(' '.join(map(str, r)))




# import sys
# rows, columns = [int(x) for x in input().split(" ")]
# matrix = []

# for _ in range(rows):
#     matrix.append([int(x) for x in input().split(" ")])

# max_sum = -sys.maxsize
# max_submatrix = []
# for row in range(rows - 2):
#     for col in range(columns - 2):
#         submatrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
#             [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
#             [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]

#         sum_elements = sum(submatrix[0]) + sum(submatrix[1]) + sum(submatrix[2])
#         if sum_elements > max_sum:
#             max_sum = sum_elements
#             max_submatrix = submatrix

# print(f"Sum = {max_sum}")
# for row in max_submatrix:
#     print(" ".join(str(x) for x in row))
