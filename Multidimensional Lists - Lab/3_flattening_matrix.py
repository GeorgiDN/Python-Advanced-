rows = int(input())
matrix = []

for _ in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.extend(numbers)

print(matrix)
