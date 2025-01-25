class MatrixContentError(Exception):
    pass


class MatrixSizeError(Exception):
    pass


def validate_matrix(matrix):
    for row in matrix:
        for element in row:
            if not element.isdigit():
                raise MatrixContentError("The matrix must consist of only integers")

    rows = len(matrix)
    for row in matrix:
        if len(row) != rows:
            raise MatrixSizeError("The size of the matrix is not a perfect square")


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()


mtrx = []

while True:
    line = input().strip()
    if not line:
        break
    mtrx.append(line.split())


validate_matrix(mtrx)
mtrx = [[int(num) for num in row] for row in mtrx]
rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=" ")
    
