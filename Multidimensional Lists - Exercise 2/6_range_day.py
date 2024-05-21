def fill_the_matrix_and_find_shooter_and_targets(s_row, s_col, mtrx_size):
    num_targets = 0
    matrix = []
    for r in range(mtrx_size):
        row = input().split()
        matrix.append(row)
        if "A" in row:
            s_row = r
            s_col = row.index('A')
        if "x" in row:
            num_targets += row.count("x")
    return matrix, s_row, s_col, num_targets


def is_valid_index(value, max_value):
    return 0 <= value < max_value


def next_move(current_direction, curr_row, curr_col, mtrx_size, steps_number):
    directions = {
        "up": lambda r, c: (r - steps_number, c) if is_valid_index(r - steps_number, mtrx_size) else (None, None),
        "down": lambda r, c: (r + steps_number, c) if is_valid_index(r + steps_number, mtrx_size) else (None, None),
        "left": lambda r, c: (r, c - steps_number) if is_valid_index(c - steps_number, mtrx_size) else (None, None),
        "right": lambda r, c: (r, c + steps_number) if is_valid_index(c + steps_number, mtrx_size) else (None, None)
    }

    return directions[current_direction](curr_row, curr_col)


def shoot(matrix, current_direction, s_row, s_col, mtrx_size):
    possible_targets = []

    take_the_targets = {
        "up": lambda: [[row, s_col] for row in range(s_row - 1, -1, -1)],
        "down": lambda: [[row, s_col] for row in range(s_row + 1, mtrx_size)],
        "left": lambda: [[s_row, col] for col in range(s_col - 1, -1, -1)],
        "right": lambda: [[s_row, col] for col in range(s_col + 1, mtrx_size)]
    }

    possible_targets.extend(take_the_targets[current_direction]())

    for target in possible_targets:
        target_row, target_col = target
        if matrix[target_row][target_col] == "x":
            matrix[target_row][target_col] = "."
            return matrix, [target_row, target_col]
    return matrix, []


def main():
    size = 5
    shooter_row, shooter_col = None, None
    targets_number_left = 0

    field, shooter_row, shooter_col, targets_number_left = fill_the_matrix_and_find_shooter_and_targets(shooter_row, shooter_col, size)
    number_of_commands = int(input())
    shot_targets_coordinates = []

    for _ in range(number_of_commands):
        data = input().split()
        command, direction = data[0], data[1]

        if command == "shoot":
            field, coordinates = shoot(field, direction, shooter_row, shooter_col, size)
            if coordinates:
                shot_targets_coordinates.append(coordinates)
                targets_number_left -= 1
                if targets_number_left == 0:
                    break

        elif command == "move":
            steps = int(data[2])
            next_row, next_col = next_move(direction, shooter_row, shooter_col, size, steps)

            if next_row is None or next_col is None or field[next_row][next_col] != ".":
                continue

            field[shooter_row][shooter_col] = "."
            shooter_row, shooter_col = next_row, next_col
            field[shooter_row][shooter_col] = "A"

    if targets_number_left == 0:
        targets_left = len(shot_targets_coordinates)
        print(f"Training completed! All {targets_left} targets hit.")
    else:
        print(f"Training not completed! {targets_number_left} targets left.")

    for curr_row in shot_targets_coordinates:
        print(curr_row)


if __name__ == '__main__':
    main()




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
