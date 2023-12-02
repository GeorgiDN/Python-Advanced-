rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for col in range(columns):
    column = [row[col] for row in matrix]
    print(sum(column))
  
