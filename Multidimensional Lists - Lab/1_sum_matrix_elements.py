rows, columns = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0

for _ in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)

for row in range(rows):
    for column in range(columns):
        total_sum += matrix[row][column]

print(total_sum)
print(matrix)
