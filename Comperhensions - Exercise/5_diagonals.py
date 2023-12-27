def read_matrix(r):
    return [[int(x) for x in input().split(", ")] for _ in range(r)]


def find_prime_diagonal(mtrx):
    return [mtrx[row][row] for row in range(len(mtrx))]


def find_second_diagonal(mtrx):
    return [mtrx[row][len(mtrx) - row - 1] for row in range(len(mtrx))]


def print_result(first_diag, second_diag):
    print(f"First diagonal: {', '.join(str(x) for x in first_diag)}. Sum: {sum(first_diag)}")
    print(f"Second diagonal: {', '.join(str(x) for x in second_diag)}. Sum: {sum(second_diag)}")


rows = int(input())
matrix = read_matrix(rows)
prime_diagonal = find_prime_diagonal(matrix)
second_diagonal = find_second_diagonal(matrix)

print_result(prime_diagonal, second_diagonal)





# rows = int(input())

# matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
# first_diagonal = [matrix[row][row] for row in range(rows)]
# second_diagonal = [matrix[row][rows-row-1] for row in range(rows)]

# print(f"First diagonal: {', '.join(map(str, first_diagonal))}. Sum: {sum(first_diagonal)}")
# print(f"Second diagonal: {', '.join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}")

