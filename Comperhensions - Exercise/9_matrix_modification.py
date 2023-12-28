def rows_input():
    return int(input())


def read_matrix(r):
    matrix = [[int(x) for x in input().split(" ")] for _ in range(r)]
    return matrix


def is_valid(val, max_val):
    return 0 <= val < max_val


def add(mtrx, r, c, num):
    if is_valid(r, len(mtrx)) and is_valid(c, len(mtrx[0])):
        mtrx[r][c] += num
        return mtrx
    return None


def subtract(mtrx, r, c, num):
    if is_valid(r, len(mtrx)) and is_valid(c, len(mtrx[0])):
        mtrx[r][c] -= num
        return mtrx
    return None


def modify_matrix(mod_mtrx):
    while True:
        result = ''
        command = input()
        if command == "END":
            break

        info = command.split(" ")
        action, row, col, number = info[0], int(info[1]), int(info[2]), int(info[3])

        if action == "Add":
            result = add(mod_mtrx, row, col, number)
            if result is None:
                print("Invalid coordinates")
                continue
            mod_mtrx = result
        elif action == "Subtract":
            result = subtract(mod_mtrx, row, col, number)
            if result is None:
                print("Invalid coordinates")
                continue
            mod_mtrx = result

    return mod_mtrx


def print_result(mod_mtrx):
    return print(*[' '.join(map(str, row)) for row in mod_mtrx], sep="\n")


rows_number = rows_input()
matrix_read = read_matrix(rows_number)
modified_matrix = modify_matrix(matrix_read)
take_output = print_result(modified_matrix)
