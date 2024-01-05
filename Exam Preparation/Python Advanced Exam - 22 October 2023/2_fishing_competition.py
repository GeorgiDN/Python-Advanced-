def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up':
        if is_valid(current_row-1, size):
            return current_row-1, current_col
        else:
            return current_row + (size-1), current_col
    if command == 'down':
        if is_valid(current_row+1, size):
            return current_row+1, current_col
        else:
            return current_row - (size-1), current_col
    if command == 'left':
        if is_valid(current_col-1, size):
            return current_row, current_col-1
        else:
            return current_row, current_col + (size - 1)
    if command == 'right':
        if is_valid(current_col+1, size):
            return current_row, current_col+1
        else:
            return current_row, current_col - (size - 1)


size = int(input())
fishing_area = []
fish_amount = 0
boat_row, boat_col = None, None
whirlpool = False

for r in range(size):
    row = list(input())
    fishing_area.append(row)
    if 'S' in row:
        boat_row = r
        boat_col = row.index('S')
        start_row = boat_row
        start_col = boat_col

while True:
    line = input()
    if line == 'collect the nets':
        fishing_area[boat_row][boat_col] = "S"
        break
    next_row, next_col = next_move(line, boat_row, boat_col)

    if fishing_area[next_row][next_col] == "W":
        fishing_area[boat_row][boat_col] = '-'
        boat_row, boat_col = next_row, next_col
        fishing_area[boat_row][boat_col] = 'W'
        last_coordinates = boat_row, boat_col
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
              f" Last coordinates of the ship: [{','.join(map(str,last_coordinates))}]")
        whirlpool = True
        break
    if fishing_area[next_row][next_col].isdigit():
        passage = int(fishing_area[next_row][next_col])
        fish_amount += passage

    fishing_area[boat_row][boat_col] = 'S'
    fishing_area[boat_row][boat_col] = "-"
    boat_row, boat_col = next_row, next_col
    fishing_area[boat_row][boat_col] = "-"

if fish_amount >= 20 and not whirlpool:
    print(f"Success! You managed to reach the quota!")
elif fish_amount < 20 and not whirlpool:
    diff = 20 - fish_amount
    print(f"You didn't catch enough fish and didn't reach the quota!"
          f" You need {diff} tons of fish more.")
if fish_amount > 0 and not whirlpool:
    print(f"Amount of fish caught: {fish_amount} tons.")
if not whirlpool:
    for row_ in fishing_area:
        print(''.join(row_))
