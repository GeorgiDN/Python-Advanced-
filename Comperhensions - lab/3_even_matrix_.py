n = int(input())
matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(n)]
print(
    matrix)


# def read_matrix(r):
#     matrix = [[int(x) for x in input().split(", ")] for _ in range(r)]
#     return matrix


# def get_even_row(row):
#     result = [x for x in row if x % 2 == 0]
#     return result


# def get_even_matrix(matrix):
#     result = [get_even_row(row) for row in matrix]
#     return result


# rows = int(input())

# print(get_even_matrix(read_matrix(rows)))
