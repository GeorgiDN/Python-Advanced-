def best_path(b_row, b_col):
    best_direction = ""
    best_positions = []
    max_eggs = 0
    for path in ["up", "down", "left", "right"]:
        sum_eggs = 0
        bunny_positions = []
        if path == "up":
            for idx in range(b_row - 1, -1, -1):
                current_egg = field[idx][b_col]
                if current_egg == "X":
                    break
                sum_eggs += current_egg
                bunny_positions.append([idx, b_col])
        elif path == "down":
            for idx in range(b_row + 1, size):
                current_egg = field[idx][b_col]
                if current_egg == "X":
                    break
                sum_eggs += current_egg
                bunny_positions.append([idx, b_col])
        elif path == "left":
            for idx in range(b_col - 1, -1, -1):
                current_egg = field[b_row][idx]
                if current_egg == "X":
                    break
                sum_eggs += current_egg
                bunny_positions.append([b_row, idx])
        elif path == "right":
            for idx in range(b_col + 1, size):
                current_egg = field[b_row][idx]
                if current_egg == "X":
                    break
                sum_eggs += current_egg
                bunny_positions.append([b_row, idx])
        if sum_eggs >= max_eggs and len(bunny_positions) > 0:
            best_direction = path
            best_positions = bunny_positions
            max_eggs = sum_eggs
    return best_direction, best_positions, max_eggs


size = int(input())
field = []
bunny_row, bunny_col = 0, 0

for row in range(size):
    current_row = [x if x in ["X", "B"] else int(x) for x in input().split()]
    field.append(current_row)
    for col in range(size):
        if current_row[col] == "B":
            bunny_row, bunny_col = row, col

direction, positions, collected_eggs = best_path(bunny_row, bunny_col)
print(direction)
[print(position) for position in positions]
print(collected_eggs)
