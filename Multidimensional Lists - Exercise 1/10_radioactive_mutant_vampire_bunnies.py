def increase_bunnies():
    global player_is_dead
    bunny_coordinates = []
    for bunny_row in range(rows):
        for bunny_col in range(columns):
            if matrix[bunny_row][bunny_col] == "B":
                bunny_coordinates.append([bunny_row, bunny_col])
    for coordinates in bunny_coordinates:
        b_row, b_col = coordinates[0], coordinates[1]
        if b_row - 1 in range(rows):
            if matrix[b_row - 1][b_col] == "P":
                player_is_dead = True
            matrix[b_row - 1][b_col] = "B"  # spread up
        if b_row + 1 in range(rows):
            if matrix[b_row + 1][b_col] == "P":
                player_is_dead = True
            matrix[b_row + 1][b_col] = "B"  # spread down
        if b_col - 1 in range(columns):
            if matrix[b_row][b_col - 1] == "P":
                player_is_dead = True
            matrix[b_row][b_col - 1] = "B"  # spread left
        if b_col + 1 in range(columns):
            if matrix[b_row][b_col + 1] == "P":
                player_is_dead = True
            matrix[b_row][b_col + 1] = "B"  # spread right


rows, columns = [int(x) for x in input().split()]
matrix = []
player_row, player_col = 0, 0
new_row, new_col = 0, 0

for row in range(rows):
    current_row = list(input())
    matrix.append(current_row)
    if "P" in current_row:
        player_row, player_col = row, current_row.index("P")

commands = list(input())
player_wins = False
player_is_dead = False

for command in commands:
    # new_row, new_col = 0, 0
    if command == "L":
        if player_col - 1 in range(columns):
            new_row, new_col = player_row, player_col - 1
        else:
            player_wins = True
    elif command == "R":
        if player_col + 1 in range(columns):
            new_row, new_col = player_row, player_col + 1
        else:
            player_wins = True
    elif command == "U":
        if player_row - 1 in range(rows):
            new_row, new_col = player_row - 1, player_col
        else:
            player_wins = True
    elif command == "D":
        if player_row + 1 in range(rows):
            new_row, new_col = player_row + 1, player_col
        else:
            player_wins = True
    if player_wins:
        matrix[player_row][player_col] = "."
    else:
        if matrix[new_row][new_col] == "B":
            player_is_dead = True
            player_row, player_col = new_row, new_col
        else:
            matrix[player_row][player_col] = "."
            player_row, player_col = new_row, new_col
            matrix[player_row][player_col] = "P"
    increase_bunnies()
    if player_wins or player_is_dead:
        break

[print("".join(element)) for element in matrix]

if player_wins:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")
  
