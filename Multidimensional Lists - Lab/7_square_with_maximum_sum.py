rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
max_square_sum = 0
submatrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        current_square_sum = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1]
        if current_square_sum > max_square_sum:
            max_square_sum = current_square_sum
            submatrix.clear()
            submatrix.append([matrix[row][col], matrix[row][col + 1]])
            submatrix.append([matrix[row+1][col], matrix[row+1][col + 1]])

for r in submatrix:
    print(' '.join(map(str, r)))
print(max_square_sum)




##############################################################################################################################################
# rows, cols = [int(x) for x in input().split(", ")]
# matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
#
# submatrix = max([
#     [
#         [matrix[row][col], matrix[row][col + 1]],
#         [matrix[row + 1][col], matrix[row + 1][col + 1]]
#     ]
#     for row in range(rows - 1)
#     for col in range(cols - 1)
# ], key=lambda mtrx: sum(map(sum, mtrx)))
#
#
# result = '\n'.join([' '.join(map(str, r)) for r in submatrix])
# print(result)
# max_sum = sum(map(sum, submatrix))
# print(max_sum)




########################################################################################################################################################
# rows, cols = [int(x) for x in input().split(", ")]
# matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
# submatrix = max([[[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]] for row in range(rows - 1) for col in range(cols - 1)], key=lambda mtrx: sum(map(sum, mtrx)))
# print('\n'.join([' '.join(map(str, r)) for r in submatrix]))
# print(sum(map(sum, submatrix)))





#########################################################################################################################################################
# rows, columns = [int(x) for x in input().split(", ")]
# matrix = []
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split(", ")])
# max_sum = 0
# max_submatrix = []
# for row in range(rows - 1):
#     for col in range(columns - 1):
#         submatrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]
#         sum_elements = sum(submatrix[0]) + sum(submatrix[1])
#         if sum_elements > max_sum:
#             max_sum = sum_elements
#             max_submatrix = submatrix
#
# for row in max_submatrix:
#     print(" ".join(str(x) for x in row))
# print(max_sum)
