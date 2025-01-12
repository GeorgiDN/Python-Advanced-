rows = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(rows)]
even_matrix = [[num for num in row if num % 2 == 0] for row in matrix]
print(even_matrix)


##########################################################################################
# rows = int(input())
# matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(rows)]
# print(matrix)


##########################################################################################
# rows = int(input())
# print([[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(rows)])


##########################################################################################
# print([[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(int(input()))])


##########################################################################################
# def read_matrix(r):
#     matrix = [[int(x) for x in input().split(", ")] for _ in range(r)]
#     return matrix
#
#
# def get_even_row(row):
#     result = [x for x in row if x % 2 == 0]
#     return result
#
#
# def get_even_matrix(matrix):
#     result = [get_even_row(row) for row in matrix]
#     return result
#
#
# rows = int(input())
#
# print(get_even_matrix(read_matrix(rows)))


##########################################################################################
# rows = int(input())
# matrix = []
# for _ in range(rows):
#     row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
#     matrix.append(row)
#
# print(matrix)

