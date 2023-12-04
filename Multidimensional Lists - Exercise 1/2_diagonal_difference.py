rows = int(input())
matrix = []

primary_diagonal_numbers = []
secondary_diagonal_numbers = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(" ")])

for i in range(rows):
    primary_diagonal_numbers.append(matrix[i][i])
    secondary_diagonal_numbers.append(matrix[i][(rows - 1) - i])

diff = abs(sum(primary_diagonal_numbers) - sum(secondary_diagonal_numbers))
print(diff)
