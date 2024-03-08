def is_valid_index(number, idx):
    return 0 <= idx < number


def is_valid_input(data_, rows, cols):
    if len(data_) == 5:
        curr_command, idx1, idx2, idx3, idx4 = data_[0], int(data_[1]), int(data_[2]), int(data_[3]), int(data_[4])
        if curr_command == "swap":
            if is_valid_index(rows, idx1) and is_valid_index(cols, idx2) and \
                    is_valid_index(rows, idx3) and is_valid_index(cols, idx4):
                return True
    return False


def swap(mtrx, idx1, idx2, idx3, idx4):
    mtrx[idx1][idx2], mtrx[idx3][idx4] = mtrx[idx3][idx4], mtrx[idx1][idx2]

    for row in mtrx:
        print(*row)
    return mtrx


rows, cols = [
    int(x) for x in input().split()
]

matrix = [
    [x for x in input().split()] for _ in range(rows)
]


while True:
    command = input()
    if command == "END":
        break

    data = command.split()
    if not is_valid_input(data, rows, cols):
        print("Invalid input!")
    else:
        index1, index2, index3, index4 = int(data[1]), int(data[2]), int(data[3]), int(data[4])
        matrix = swap(matrix, index1, index2, index3, index4)




# def swap(row1, col1, row2, col2):
#     matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
# 
# 
# rows, columns = [int(x) for x in input().split()]
# matrix = [input().split() for x in range(rows)]
# 
# while True:
#     command = input()
#     if command == "END":
#         break
#     if not command.startswith("swap") or len(command.split()) != 5:
#         print("Invalid input!")
#         continue
#     row1, col1, row2, col2 = [int(x) for x in command.split()[1:]]
# 
#     if row1 in range(rows) and col1 in range(columns) and row2 in range(rows) and col2 in range(columns):
#         swap(row1, col1, row2, col2)
#         [print(" ".join(row)) for row in matrix]
#     else:
#         print("Invalid input!")

