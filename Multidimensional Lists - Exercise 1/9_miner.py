size = int(input())
commands = input().split()
matrix = []
coal = 0
miner_row, miner_col = 0, 0
game_over_condition = False
new_row = 0
new_col = 0


for row in range(size):
    current_row = [x for x in input().split()]
    matrix.append(current_row)
    for col in range(size):
        if current_row[col] == "s":
            miner_row, miner_col = row, col
        elif current_row[col] == "c":
            coal += 1

for command in commands:
    if command == "up":
        if miner_row - 1 in range(size):
            new_row, new_col = miner_row - 1, miner_col
        else:
            continue
    elif command == "down":
        if miner_row + 1 in range(size):
            new_row, new_col = miner_row + 1, miner_col
        else:
            continue
    elif command == "left":
        if miner_col - 1 in range(size):
            new_row, new_col = miner_row, miner_col - 1
        else:
            continue
    elif command == "right":
        if miner_col + 1 in range(size):
            new_row, new_col = miner_row, miner_col + 1
        else:
            continue
    symbol_to_overcome = matrix[new_row][new_col]
    if symbol_to_overcome == "c":
        coal -= 1
    elif symbol_to_overcome == "e":
        print(f"Game over! ({new_row}, {new_col})")
        game_over_condition = True
        break
    matrix[new_row][new_col] = "s"
    matrix[miner_row][miner_col] = "*"
    miner_row, miner_col = new_row, new_col
    if coal == 0:
        print(f"You collected all coal! ({new_row}, {new_col})")
        game_over_condition = True
        break

if not game_over_condition:
    print(f"{coal} pieces of coal left. ({miner_row}, {miner_col})")

