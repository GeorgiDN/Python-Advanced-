class ModifiedMatrix:
    def __init__(self):
        self.number_rows = 0
        self.matrix = []
        self.action = ""

    def take_rows_input(self):
        self.number_rows = self._rows_input()

    def read_matrix(self):
        self.matrix = self._read_matrix(self.number_rows)

    def modify_matrix(self):
        self.matrix = self._modify_matrix(self.matrix)

    def print_result(self):
        self._print_result(self.matrix)

    # Helper methods
    def _rows_input(self):
        return int(input())

    def _read_matrix(self, r):
        matrix = [[int(x) for x in input().split(" ")] for _ in range(r)]
        return matrix

    def _is_valid(self, val, max_val):
        return 0 <= val < max_val

    def _add(self, mtrx, r, c, num):
        if self._is_valid(r, len(mtrx)) and self._is_valid(c, len(mtrx[0])):
            mtrx[r][c] += num
            return mtrx
        return None

    def _subtract(self, mtrx, r, c, num):
        if self._is_valid(r, len(mtrx)) and self._is_valid(c, len(mtrx[0])):
            mtrx[r][c] -= num
            return mtrx
        return None

    def _modify_matrix(self, mod_mtrx):
        while True:
            command = input()
            if command == "END":
                break

            info = command.split(" ")
            action, row, col, number = info[0], int(info[1]), int(info[2]), int(info[3])

            if action == "Add":
                result = self._add(mod_mtrx, row, col, number)
                if result is None:
                    print("Invalid coordinates")
                    continue
                mod_mtrx = result
            elif action == "Subtract":
                result = self._subtract(mod_mtrx, row, col, number)
                if result is None:
                    print("Invalid coordinates")
                    continue
                mod_mtrx = result

        return mod_mtrx

    def _print_result(self, mod_mtrx):
        print(*[' '.join(map(str, row)) for row in mod_mtrx], sep="\n")


modified_matrix = ModifiedMatrix()
modified_matrix.take_rows_input()
modified_matrix.read_matrix()
modified_matrix.modify_matrix()
modified_matrix.print_result()






##
# def rows_input():
#     return int(input())


# def read_matrix(r):
#     matrix = [[int(x) for x in input().split(" ")] for _ in range(r)]
#     return matrix


# def is_valid(val, max_val):
#     return 0 <= val < max_val


# def add(mtrx, r, c, num):
#     if is_valid(r, len(mtrx)) and is_valid(c, len(mtrx[0])):
#         mtrx[r][c] += num
#         return mtrx
#     return None


# def subtract(mtrx, r, c, num):
#     if is_valid(r, len(mtrx)) and is_valid(c, len(mtrx[0])):
#         mtrx[r][c] -= num
#         return mtrx
#     return None


# def modify_matrix(mod_mtrx):
#     while True:
#         result = ''
#         command = input()
#         if command == "END":
#             break

#         info = command.split(" ")
#         action, row, col, number = info[0], int(info[1]), int(info[2]), int(info[3])

#         if action == "Add":
#             result = add(mod_mtrx, row, col, number)
#             if result is None:
#                 print("Invalid coordinates")
#                 continue
#             mod_mtrx = result
#         elif action == "Subtract":
#             result = subtract(mod_mtrx, row, col, number)
#             if result is None:
#                 print("Invalid coordinates")
#                 continue
#             mod_mtrx = result

#     return mod_mtrx


# def print_result(mod_mtrx):
#     return print(*[' '.join(map(str, row)) for row in mod_mtrx], sep="\n")


# rows_number = rows_input()
# matrix_read = read_matrix(rows_number)
# modified_matrix = modify_matrix(matrix_read)
# take_output = print_result(modified_matrix)

