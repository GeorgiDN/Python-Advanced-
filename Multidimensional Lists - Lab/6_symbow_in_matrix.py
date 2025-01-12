rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]
searched_symbol = input()
founded_symbol = next(((row, col) for row in range(rows) for col in range(rows) if matrix[row][col] == searched_symbol), None)
print(founded_symbol) if founded_symbol else print(f"{searched_symbol} does not occur in the matrix")



# rows = int(input())
# matrix = [[x for x in input()] for _ in range(rows)]
# symbol = input()
# found = False

# for idx in range(rows):
#     if not found:
#         row = matrix[idx]
#         if symbol in row:
#             found = True
#             print((idx, row.index(symbol)))
#             break

# if not found:
#     print(f'{symbol} does not occur in the matrix')


# rows = int(input())
# matrix = [[x for x in input()] for _ in range(rows)]
# searched_symbow = input()
# founded_symbow = False
#
# for row in range(rows):
#     if founded_symbow:
#         break
#     for col in range(rows):
#         if matrix[row][col] == searched_symbow:
#             print((row, col))
#             founded_symbow = True
#             break
#
# if not founded_symbow:
#     print(f"{searched_symbow} does not occur in the matrix")




# rows = int(input())
# matrix = []
# found_condition = False
# 
# for _ in range(rows):
#     matrix.append([x for x in input()])
# 
# symbol = input()
# 
# for col in range(rows):
#     for idx, row in enumerate(matrix):
#         column = row[col]
#         if column == symbol:
#             print(f"({idx}, {col})")
#             found_condition = True
#             break
# 
# if not found_condition:
#     print(f"{symbol} does not occur in the matrix")
