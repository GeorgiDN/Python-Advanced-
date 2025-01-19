def is_valid_index(value, max_value):
    return 0 <= value < max_value


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

rows = 5
matrix, player, target, empty = [], 'A', 'x', '.'
p_row, p_col = 0, 0
targets_left = 0
shoot_targets = []

for idx in range(rows):
    row = input().split()
    matrix.append(row)
    if player in row:
        p_row, p_col = idx, row.index(player)
    if target in row:
        targets_left += row.count(target)

count_targets = targets_left
number_commands = int(input())

for _ in range(number_commands):
    if targets_left == 0:
        break
    command_info = input().split()
    command = command_info[0]
    direction = command_info[1]
    d_row, d_col = directions[direction][0], directions[direction][1]

    if command == 'move':
        steps = int(command_info[2])
        next_row = p_row + d_row * steps
        next_col = p_col + d_col * steps
        if (is_valid_index(next_row, rows)
                and is_valid_index(next_col, rows)
                and matrix[next_row][next_col] == empty):
            matrix[p_row][p_col] = empty
            p_row, p_col = next_row, next_col
            matrix[p_row][p_col] = empty

    elif command == 'shoot':
        shoot_row, shoot_col = p_row + d_row, p_col + d_col
        while is_valid_index(shoot_row, rows) and is_valid_index(shoot_col, rows):
            if matrix[shoot_row][shoot_col] == target:
                targets_left -= 1
                shoot_targets.append([shoot_row, shoot_col])
                matrix[shoot_row][shoot_col] = empty
                break
            shoot_row, shoot_col = shoot_row + d_row, shoot_col + d_col

if targets_left == 0:
    print(f'Training completed! All {count_targets} targets hit.')
else:
    print(f"Training not completed! {targets_left} targets left.")

[print(t) for t in shoot_targets]
    



############################################################################################################################################################################################################
# def is_valid_index(idx, size):
#     return 0 <= idx < size


# size, matrix, shoot_targets, empty = 5, [], [], "."
# row, col, targets_left = 0, 0, 0

# directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

# for r in range(size):
#     current_row = input().split()
#     matrix.append(current_row)
#     for c in range(size):
#         if matrix[r][c] == "x":
#             targets_left += 1
#         if matrix[r][c] == "A":
#             row, col = r, c

# commands_count = int(input())

# for _ in range(commands_count):
#     if targets_left == 0:
#         break
#     data = input().split()
#     command, direction = data[0], data[1]
#     d_row, d_col = directions[direction][0], directions[direction][1]
#     if command == "move":
#         steps = int(data[2])
#         next_row = row + d_row * steps
#         next_col = col + d_col * steps
#         if is_valid_index(next_row, size) and is_valid_index(next_col, size) and \
#             matrix[next_row][next_col] == empty:
#                 matrix[next_row][next_col] = 'A'
#                 matrix[row][col] = '.'
#                 row, col = next_row, next_col

#     elif command == "shoot":
#         current_row, current_col = row, col
#         for _ in range(size):
#             if targets_left == 0:
#                 break
#             next_row, next_col = row + d_row, col + d_col
#             if is_valid_index(next_row, size) and is_valid_index(next_col, size):
#                 if matrix[next_row][next_col] == "x":
#                     matrix[next_row][next_col] = empty
#                     targets_left -= 1
#                     shoot_targets.append([next_row, next_col])
#                     break
#                 row, col = next_row, next_col
#             else:
#                 break
#         row, col = current_row, current_col

# print(f"Training completed! All {len(shoot_targets)} targets hit.") if targets_left == 0 \
#     else print(f"Training not completed! {targets_left} targets left.")

# for target in shoot_targets:
#     print(target)



############################################################################################################################################################################################################
# def fill_the_matrix_and_find_shooter_and_targets(s_row, s_col, mtrx_size):
#     num_targets = 0
#     matrix = []
#     for r in range(mtrx_size):
#         row = input().split()
#         matrix.append(row)
#         if "A" in row:
#             s_row = r
#             s_col = row.index('A')
#         if "x" in row:
#             num_targets += row.count("x")
#     return matrix, s_row, s_col, num_targets


# def is_valid_index(value, max_value):
#     return 0 <= value < max_value


# def next_move(current_direction, curr_row, curr_col, mtrx_size, steps_number):
#     directions = {
#         "up": lambda r, c: (r - steps_number, c) if is_valid_index(r - steps_number, mtrx_size) else (None, None),
#         "down": lambda r, c: (r + steps_number, c) if is_valid_index(r + steps_number, mtrx_size) else (None, None),
#         "left": lambda r, c: (r, c - steps_number) if is_valid_index(c - steps_number, mtrx_size) else (None, None),
#         "right": lambda r, c: (r, c + steps_number) if is_valid_index(c + steps_number, mtrx_size) else (None, None)
#     }

#     return directions[current_direction](curr_row, curr_col)


# def shoot(matrix, current_direction, s_row, s_col, mtrx_size):
#     possible_targets = []

#     take_the_targets = {
#         "up": lambda: [[row, s_col] for row in range(s_row - 1, -1, -1)],
#         "down": lambda: [[row, s_col] for row in range(s_row + 1, mtrx_size)],
#         "left": lambda: [[s_row, col] for col in range(s_col - 1, -1, -1)],
#         "right": lambda: [[s_row, col] for col in range(s_col + 1, mtrx_size)]
#     }

#     possible_targets.extend(take_the_targets[current_direction]())

#     for target in possible_targets:
#         target_row, target_col = target
#         if matrix[target_row][target_col] == "x":
#             matrix[target_row][target_col] = "."
#             return matrix, [target_row, target_col]
#     return matrix, []


# def main():
#     size = 5
#     shooter_row, shooter_col = None, None
#     targets_number_left = 0

#     field, shooter_row, shooter_col, targets_number_left = fill_the_matrix_and_find_shooter_and_targets(shooter_row, shooter_col, size)
#     number_of_commands = int(input())
#     shot_targets_coordinates = []

#     for _ in range(number_of_commands):
#         data = input().split()
#         command, direction = data[0], data[1]

#         if command == "shoot":
#             field, coordinates = shoot(field, direction, shooter_row, shooter_col, size)
#             if coordinates:
#                 shot_targets_coordinates.append(coordinates)
#                 targets_number_left -= 1
#                 if targets_number_left == 0:
#                     break

#         elif command == "move":
#             steps = int(data[2])
#             next_row, next_col = next_move(direction, shooter_row, shooter_col, size, steps)

#             if next_row is None or next_col is None or field[next_row][next_col] != ".":
#                 continue

#             field[shooter_row][shooter_col] = "."
#             shooter_row, shooter_col = next_row, next_col
#             field[shooter_row][shooter_col] = "A"

#     if targets_number_left == 0:
#         targets_left = len(shot_targets_coordinates)
#         print(f"Training completed! All {targets_left} targets hit.")
#     else:
#         print(f"Training not completed! {targets_number_left} targets left.")

#     for curr_row in shot_targets_coordinates:
#         print(curr_row)


# if __name__ == '__main__':
#     main()




####################################################################################################################################################################################################################################
# def fill_the_matrix_and_find_shooter_and_targets(s_row, s_col, mtrx_size):
#     num_targets = 0
#     matrix = []
#     for r in range(mtrx_size):
#         row = input().split()
#         matrix.append(row)
#         if "A" in row:
#             s_row = r
#             s_col = row.index('A')
#         if "x" in row:
#             num_targets += row.count("x")
#     return matrix, s_row, s_col, num_targets


# def is_valid_index(value, max_value):
#     return 0 <= value < max_value


# def next_move(current_direction, curr_row, curr_col, mtrx_size, steps_number):
#     if current_direction == "up" and is_valid_index(curr_row - steps_number, mtrx_size):
#         return curr_row - steps_number, curr_col
#     if current_direction == "down" and is_valid_index(curr_row + steps_number, mtrx_size):
#         return curr_row + steps_number, curr_col
#     if current_direction == "left" and is_valid_index(curr_col - steps_number, mtrx_size):
#         return curr_row, curr_col - steps_number
#     if current_direction == "right" and is_valid_index(curr_col + steps_number, mtrx_size):
#         return curr_row, curr_col + steps_number
#     return None, None


# def shoot(matrix, current_direction, s_row, s_col, mtrx_size):
#     possible_targets = []
#     if current_direction == "up":
#         for row in range(s_row - 1, -1, -1):
#             possible_targets.append([row, s_col])
#     elif current_direction == "down":
#         for row in range(s_row + 1, mtrx_size):
#             possible_targets.append([row, s_col])
#     elif current_direction == "left":
#         for col in range(s_col - 1, -1, -1):
#             possible_targets.append([s_row, col])
#     elif current_direction == "right":
#         for col in range(s_col + 1, mtrx_size):
#             possible_targets.append([s_row, col])
#     for target in possible_targets:
#         target_row, target_col = target
#         if matrix[target_row][target_col] == "x":
#             matrix[target_row][target_col] = "."
#             return matrix, [target_row, target_col]
#     return matrix, []


# def main():
#     size = 5
#     field = []
#     shooter_row, shooter_col = None, None
#     targets_number_left = 0

#     field, shooter_row, shooter_col, targets_number_left = fill_the_matrix_and_find_shooter_and_targets(shooter_row, shooter_col, size)
#     number_of_commands = int(input())
#     shot_targets_coordinates = []

#     for _ in range(number_of_commands):
#         data = input().split()
#         command, direction = data[0], data[1]

#         if command == "shoot":
#             field, coordinates = shoot(field, direction, shooter_row, shooter_col, size)
#             if coordinates:
#                 shot_targets_coordinates.append(coordinates)
#                 targets_number_left -= 1
#                 if targets_number_left == 0:
#                     break

#         elif command == "move":
#             steps = int(data[2])
#             next_row, next_col = next_move(direction, shooter_row, shooter_col, size, steps)

#             if next_row is None or next_col is None:
#                 continue

#             if field[next_row][next_col] == "x":
#                 continue

#             field[shooter_row][shooter_col] = "."
#             shooter_row, shooter_col = next_row, next_col
#             field[shooter_row][shooter_col] = "A"  # to check where is shooter

#     if targets_number_left == 0:
#         targets_left = len(shot_targets_coordinates)
#         print(f"Training completed! All {targets_left} targets hit.")
#     else:
#         print(f"Training not completed! {targets_number_left} targets left.")

#     for curr_row in shot_targets_coordinates:
#         print(curr_row)


# main()
