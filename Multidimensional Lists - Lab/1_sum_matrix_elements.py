rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
total_sum = sum([num for row in matrix for num in row])

print(total_sum)
print(matrix)


# rows, cols = list(map(int, input().split(', ')))
# matrix = [list(map(int, input().split(', '))) for _ in range(rows)]
# print(sum([num for row in matrix for num in row]))
# print(matrix)


# rows, columns = [int(x) for x in input().split(", ")]
# matrix = []
# total_sum = 0

# for _ in range(rows):
#     numbers = [int(x) for x in input().split(", ")]
#     matrix.append(numbers)

# for row in range(rows):
#     for column in range(columns):
#         total_sum += matrix[row][column]

# print(total_sum)
# print(matrix)
