def move(direction, steps, s_row, s_col):
    new_row, new_col = 0, 0
    if direction == "up":
        new_row, new_col = s_row - steps, s_col
    elif direction == "down":
        new_row, new_col = s_row + steps, s_col
    elif direction == "left":
        new_row, new_col = s_row, s_col - steps
    elif direction == "right":
        new_row, new_col = s_row, s_col + steps
    if new_row in range(size) and new_col in range(size) and field[new_row][new_col] == ".":
        field[s_row][s_col] = "."
        s_row, s_col = new_row, new_col
        field[s_row][s_col] = "A"
    return s_row, s_col


def shoot(direction, s_row, s_col):
    possible_targets = []
    if direction == "up":
        possible_targets.extend([[row, s_col] for row in range(s_row - 1, - 1, - 1)])
    elif direction == "down":
        possible_targets.extend([[row, s_col] for row in range(s_row + 1, size)])
    elif direction == "left":
        possible_targets.extend([[s_row, col] for col in range(s_col - 1, - 1, - 1)])
    elif direction == "right":
        possible_targets.extend([[s_row, col] for col in range(s_col + 1, size)])
    for target in possible_targets:
        target_row, target_col = target
        if target_row in range(size) and target_col in range(size) and field[target_row][target_col] == "x":
            field[target_row][target_col] = "."
            return [target_row, target_col]
    return []


size = 5
field = []
shooter_row, shooter_col = 0, 0
targets = 0

for row in range(size):
    current_row = [x for x in input().split()]
    field.append(current_row)
    for symbol in current_row:
        if symbol == "A":
            shooter_row, shooter_col = row, current_row.index("A")
        elif symbol == "x":
            targets += 1

command_count = int(input())
shot_targets = []

for _ in range(command_count):
    command = input().split()
    if command[0] == "move":
        move_direction, steps = command[1], int(command[2])
        shooter_row, shooter_col = move(move_direction, steps, shooter_row, shooter_col)
    elif command[0] == "shoot":
        shoot_direction = command[1]
        coordinates = shoot(shoot_direction, shooter_row, shooter_col)
        if coordinates:
            shot_targets.append(coordinates)
            targets -= 1
    if targets == 0:
        break

if targets == 0:
    print(f"Training completed! All {len(shot_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

[print(element) for element in shot_targets]
