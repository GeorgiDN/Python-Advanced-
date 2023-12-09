size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0
attacking_knight = []

while True:
    max_attacks = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                atack = 0
                if (row - 1) in range(size) and (col - 2) in range(size) and matrix[row - 1][col - 2] == "K":
                    atack += 1
                if (row - 2) in range(size) and (col - 1) in range(size) and matrix[row - 2][col - 1] == "K":
                    atack += 1
                if (row - 2) in range(size) and (col + 1) in range(size) and matrix[row - 2][col + 1] == "K":
                    atack += 1
                if (row - 1) in range(size) and (col + 2) in range(size) and matrix[row - 1][col + 2] == "K":
                    atack += 1
                if (row + 1) in range(size) and (col + 2) in range(size) and matrix[row + 1][col + 2] == "K":
                    atack += 1
                if (row + 2) in range(size) and (col + 1) in range(size) and matrix[row + 2][col + 1] == "K":
                    atack += 1
                if (row + 2) in range(size) and (col - 1) in range(size) and matrix[row + 2][col - 1] == "K":
                    atack += 1
                if (row + 1) in range(size) and (col - 2) in range(size) and matrix[row + 1][col - 2] == "K":
                    atack += 1

                if atack > max_attacks:
                    max_attacks = atack
                    attacking_knight = [row, col]
    if max_attacks == 0:
        break
    knight_row, knight_col = attacking_knight
    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)



# #  With function
# def possible_attacks(r, c):
#     result = 0
#     if (r - 1) in range(size) and (c - 2) in range(size) and matrix[r - 1][c - 2] == "K":
#         result += 1
#     if (r - 2) in range(size) and (c - 1) in range(size) and matrix[r - 2][c - 1] == "K":
#         result += 1
#     if (r - 2) in range(size) and (c + 1) in range(size) and matrix[r - 2][c + 1] == "K":
#         result += 1
#     if (r - 1) in range(size) and (c + 2) in range(size) and matrix[r - 1][c + 2] == "K":
#         result += 1
#     if (r + 1) in range(size) and (c + 2) in range(size) and matrix[r + 1][c + 2] == "K":
#         result += 1
#     if (r + 2) in range(size) and (c + 1) in range(size) and matrix[r + 2][c + 1] == "K":
#         result += 1
#     if (r + 2) in range(size) and (c - 1) in range(size) and matrix[r + 2][c - 1] == "K":
#         result += 1
#     if (r + 1) in range(size) and (c - 2) in range(size) and matrix[r + 1][c - 2] == "K":
#         result += 1
#     return result


# size = int(input())
# matrix = []

# for _ in range(size):
#     matrix.append(list(input()))

# removed_knights = 0
# attacking_knight = []

# while True:
#     max_attacks = 0
#     for row in range(size):
#         for col in range(size):
#             if matrix[row][col] == "K":
#                 attacks = possible_attacks(row, col)
#                 if attacks > max_attacks:
#                     max_attacks = attacks
#                     attacking_knight = [row, col]
#     if max_attacks == 0:
#         break
#     knight_row, knight_col = attacking_knight
#     matrix[knight_row][knight_col] = "0"
#     removed_knights += 1

# print(removed_knights)
