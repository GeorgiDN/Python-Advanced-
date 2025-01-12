rows, cols = list(map(int, input().split(', ')))
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]
sum_cols = [sum(matrix[row][col] for row in range(rows)) for col in range(cols)]
print('\n'.join(map(str, sum_cols)))


# rows, cols = map(int, input().split(', '))
# matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]
# sum_cols = []
#
# for col in range(cols):
#     total_sum = 0
#     for row in range(rows):
#         num = matrix[row][col]
#         total_sum += num
#     sum_cols.append(total_sum)
#
# print('\n'.join(map(str, sum_cols)))



# rows, cols = [int(x) for x in input().split(", ")]
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]

# print('\n'.join(map(str, [sum(row[col] for row in matrix) for col in range(cols)])))



# rows, cols = [int(x) for x in input().split(", ")]
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# for col in range(cols):
#     sum_cols = 0
#     for row in matrix:
#         sum_cols += row[col]
#     print(sum_cols)




# rows, columns = [int(x) for x in input().split(", ")]
# matrix = []
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split()])
#
# for col in range(columns):
#     column = [row[col] for row in matrix]
#     print(sum(column))




# rows, columns = [int(x) for x in input().split(", ")]
# matrix = []
# result = []
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split()])
#
# for col in range(columns):
#     for row in matrix:
#         column = row[col]
#         result.append(column)
#
#     print(sum(result))
#     result = []
