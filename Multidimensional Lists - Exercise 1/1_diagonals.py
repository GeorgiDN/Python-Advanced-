rows = int(input())
matrix = []

primary_diagonal_numbers = []
secondary_diagonal_numbers = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for i in range(rows):
    primary_diagonal_numbers.append(matrix[i][i])
    secondary_diagonal_numbers.append(matrix[i][(rows - 1) - i])


print(f"Primary diagonal: {', '.join(map(str, primary_diagonal_numbers))}. Sum: {sum(primary_diagonal_numbers)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal_numbers))}. Sum: {sum(secondary_diagonal_numbers)}")
