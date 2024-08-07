def fill_matrix_and_takes_positions(b_row, b_col, size):
    field = []
    for idx in range(size):
        row = list(input())
        field.append(row)
        if "B" in row:
            b_row = idx
            b_col = row.index("B")
    return field, b_row, b_col


def next_move(b_row, b_col, direction, size):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    row, col = moves[direction][0], moves[direction][1]
    next_row = (b_row + row) % size
    next_col = (b_col + col) % size
    return next_row, next_col


def main():
    size = int(input())
    b_row, b_col = 0, 0
    field, b_row, b_col = fill_matrix_and_takes_positions(b_row, b_col, size)
    nectar_goal, bee_energy, hive = 30, 15, "H"
    collected_nectar = 0
    hive_reached, restored_once = False, False

    while True:
        if bee_energy == 0 and collected_nectar >= 30:
            if not restored_once:
                amount_restored = collected_nectar - nectar_goal
                bee_energy += amount_restored
                collected_nectar = 30
                restored_once = True
            else:
                break

        if hive_reached or bee_energy == 0:
            break

        direction = input()
        next_row, next_col = next_move(b_row, b_col, direction, size)
        bee_energy -= 1

        if field[next_row][next_col].isdigit():
            nectar_sum = int(field[next_row][next_col])
            collected_nectar += nectar_sum

        elif bee_energy == 0 and collected_nectar < 30:
            field[b_row][b_col] = "-"
            field[next_row][next_col] = "B"
            break

        elif field[next_row][next_col] == hive:
            hive_reached = True

        field[b_row][b_col] = "-"
        b_row, b_col = next_row, next_col
        field[next_row][next_col] = "B"

    if hive_reached:
        if collected_nectar >= nectar_goal:
            print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
    else:
        print("This is the end! Beesy ran out of energy.")

    for row in field:
        print("".join(row))


if __name__ == '__main__':
    main()





# def next_move(rows, row, col, direction):
#     moves = {
#         "up": (-1, 0),
#         "down": (1, 0),
#         "left": (0, -1),
#         "right": (0, 1)
#     }

#     d_row, d_col = moves[direction]
#     row = (row + d_row) % rows
#     col = (col + d_col) % rows
#     return row, col


# def fill_the_matrix_and_take_positions(rows, b_row, b_col):
#     field = []
#     for r in range(rows):
#         row = list(input())
#         field.append(row)
#         if "B" in row:
#             b_row = r
#             b_col = row.index("B")

#     return field, b_row, b_col


# def mark_passed_moves(field, b_row, b_col, next_row, next_col):
#     field[b_row][b_col] = "-"
#     b_row, b_col = next_row, next_col
#     field[b_row][b_col] = "B"
#     return field, b_row, b_col, next_row, next_col


# def check_energy(bee_energy, collected_nectar, nectar_goal, restored_energy, successful_restored):
#     if bee_energy == 0:
#         if collected_nectar >= nectar_goal and not restored_energy:
#             successful_restored = True
#             energy_restore = collected_nectar - nectar_goal
#             bee_energy += energy_restore
#             collected_nectar = nectar_goal
#             restored_energy = True

#     return bee_energy, collected_nectar, nectar_goal, restored_energy, successful_restored


# def check_if_hive_reached(field, next_row, next_col, bee_energy, collected_nectar, nectar_goal, hive_reached):
#     if field[next_row][next_col] == "H":
#         hive_reached = True
#         if collected_nectar >= nectar_goal:
#             print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
#         else:
#             print("Beesy did not manage to collect enough nectar.")
#     return hive_reached


# def flowers_check(field, next_row, next_col, collected_nectar):
#     if field[next_row][next_col].isdigit():
#         flower = int(field[next_row][next_col])
#         collected_nectar += flower
#     return collected_nectar


# def main():
#     field = []
#     bee_row, bee_col = 0, 0
#     rows = int(input())

#     field, bee_row, bee_col = (
#         fill_the_matrix_and_take_positions(rows, bee_row, bee_col))
#     nectar_goal = 30
#     bee_energy = 15
#     collected_nectar = 0
#     restored_energy = False
#     successful_restored = False
#     hive_reached = False
#     out_of_energy_message = "This is the end! Beesy ran out of energy."

#     while True:
#         bee_energy, collected_nectar, nectar_goal, restored_energy, successful_restored =\
#             check_energy(bee_energy, collected_nectar, nectar_goal, restored_energy, successful_restored)

#         if not successful_restored and bee_energy == 0:
#             print(out_of_energy_message)
#             break

#         direction = input()
#         next_row, next_col = next_move(rows, bee_row, bee_col, direction)
#         bee_energy -= 1

#         hive_reached = (
#             check_if_hive_reached(field, next_row, next_col, bee_energy, collected_nectar, nectar_goal, hive_reached))

#         if hive_reached:
#             field, bee_row, bee_col, next_row, next_col = (
#                 mark_passed_moves(field, bee_row, bee_col, next_row, next_col))  # Mark field with - and B
#             break

#         collected_nectar = flowers_check(field, next_row, next_col, collected_nectar)  # Check for flowers

#         if restored_energy and bee_energy == 0:
#             field, bee_row, bee_col, next_row, next_col = (
#                 mark_passed_moves(field, bee_row, bee_col, next_row, next_col))  # Mark field with - and B
#             print(out_of_energy_message)
#             break

#         field, bee_row, bee_col, next_row, next_col = (
#             mark_passed_moves(field, bee_row, bee_col, next_row, next_col))  # Mark field with - and B

#     for row in field:
#         print(''.join(row))


# if __name__ == '__main__':
#     main()







# def is_valid(value, size):
#     return 0 <= value < size
#
#
# def next_move(rows, current_row, current_col, direction):
#     if direction == 'up':
#         if is_valid(current_row-1, rows):
#             return current_row-1, current_col
#         return current_row + (rows - 1), current_col
#     if direction == 'down':
#         if is_valid(current_row+1, rows):
#             return current_row+1, current_col
#         return current_row - (rows - 1), current_col
#     if direction == 'left':
#         if is_valid(current_col-1, rows):
#             return current_row, current_col-1
#         return current_row, current_col + (rows - 1)
#     if direction == 'right':
#         if is_valid(current_col+1, rows):
#             return current_row, current_col+1
#         return current_row, current_col - (rows - 1)
#
#
# def fill_the_matrix_and_take_positions(rows, b_row, b_col):
#     field = []
#     for r in range(rows):
#         row = list(input())
#         field.append(row)
#         if "B" in row:
#             b_row = r
#             b_col = row.index("B")
#     return field, b_row, b_col
#
#
# def main():
#     field = []
#     bee_row, bee_col = 0, 0
#     rows = int(input())
#
#     field, bee_row, bee_col = fill_the_matrix_and_take_positions(rows, bee_row, bee_col)
#     nectar_goal = 30
#     bee_energy = 15
#     restored_energy = False
#     collected_nectar = 0
#
#     while True:
#         if bee_energy == 0:
#             if collected_nectar >= nectar_goal and not restored_energy:
#                 restored_energy = collected_nectar - nectar_goal
#                 bee_energy += restored_energy
#                 collected_nectar = nectar_goal
#                 restored_energy = True
#             else:
#                 print("This is the end! Beesy ran out of energy.")
#                 break
#
#         direction = input()
#         next_row, next_col = next_move(rows, bee_row, bee_col, direction)
#         bee_energy -= 1
#
#         if field[next_row][next_col] == "H":
#             if collected_nectar >= nectar_goal:
#                 print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
#             else:
#                 print("Beesy did not manage to collect enough nectar.")
#             field[bee_row][bee_col] = "-"
#             bee_row, bee_col = next_row, next_col
#             field[bee_row][bee_col] = "B"
#             break
#
#         if field[next_row][next_col].isdigit():
#             flower = int(field[next_row][next_col])
#             collected_nectar += flower
#
#         if restored_energy and bee_energy == 0:
#             field[bee_row][bee_col] = "-"
#             bee_row, bee_col = next_row, next_col
#             field[bee_row][bee_col] = "B"
#             print("This is the end! Beesy ran out of energy.")
#             break
#
#         field[bee_row][bee_col] = "-"
#         bee_row, bee_col = next_row, next_col
#         field[bee_row][bee_col] = "B"
#
#     for r in field:
#         print(''.join(r))
#
#
# if __name__ == '__main__':
#     main()

