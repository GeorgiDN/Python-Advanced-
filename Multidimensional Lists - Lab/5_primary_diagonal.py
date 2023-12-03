n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

primary_diagonal_sum = sum([matrix[i][i] for i in range(n)])
print(primary_diagonal_sum)
