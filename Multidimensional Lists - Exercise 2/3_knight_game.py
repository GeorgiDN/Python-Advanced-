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
