rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
primary_diagonal_sum = sum([sum(matrix[i][i] for i in range(rows))])
print(primary_diagonal_sum)



# IT DOES NOT WORK IN JUDGE SYSTEM THIS SYNTAX -> :=
# rows = int(input())
# matrix_and_diagonal_sum = (
#     (matrix := [[int(x) for x in input().split()] for _ in range(rows)]),
#     (diagonal_sum := sum(matrix[i][i] for i in range(rows))),
# )[1]
#
# print(matrix_and_diagonal_sum)




# n = int(input())
# matrix = []
#
# for _ in range(n):
#     matrix.append([int(x) for x in input().split()])
#
# primary_diagonal_sum = sum([matrix[i][i] for i in range(n)])
# print(primary_diagonal_sum)




# n = int(input())
# matrix = []
# primary_diagonal_sum = []
# idx = 0
# for _ in range(n):
#     matrix.append([int(x) for x in input().split()])
#
# for col in range(1):
#     for row in matrix:
#         column = row[col + idx]
#         primary_diagonal_sum.append(column)
#         idx += 1
#     print(sum(primary_diagonal_sum))
#     break
