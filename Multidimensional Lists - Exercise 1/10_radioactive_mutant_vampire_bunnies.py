directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

rows, cols = list(map(int, input().split()))
p_row, p_col, matrix = 0, 0, []
player, bunny, empty = 'P', 'B', '.'
player_is_dead, player_win = False, False


def is_valid_idx(idx, value):
    return 0 <= idx < value


def next_move(b_row, b_col, dir_):
    d_row, d_col = directions[dir_][0], directions[dir_][1]
    next_row = b_row + d_row if is_valid_idx(b_row + d_row, rows) else None
    next_col = b_col + d_col if is_valid_idx(b_col + d_col, cols) else None

    return next_row, next_col


def bunny_spread(player_is_dead):
    bunnies = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == bunny:
                bunnies.append([row, col])

    for b_row, b_col in bunnies:
        for direction in directions.values():
            d_row, d_col = direction[0], direction[1]
            new_row, new_col = b_row + d_row, b_col + d_col
            if is_valid_idx(new_row, rows) and is_valid_idx(new_col, cols):
                if matrix[new_row][new_col] == player:
                    player_is_dead = True
                matrix[new_row][new_col] = bunny

    return matrix, player_is_dead


for idx in range(rows):
    row = list(input())
    matrix.append(row)
    if player in row:
        p_row = idx
        p_col = row.index(player)

moves = list(input())

for move in moves:
    next_row, next_col = next_move(p_row, p_col, move)

    if next_row is None or next_col is None:
        player_win = True
        matrix[p_row][p_col] = empty

    else:
        if matrix[next_row][next_col] == bunny:
            player_is_dead = True
            p_row, p_col = next_row, next_col
        else:
            matrix[p_row][p_col] = empty
            p_row, p_col = next_row, next_col
            matrix[p_row][p_col] = player

    matrix, player_is_dead = bunny_spread(player_is_dead)

    if player_is_dead or player_win:
        break

for row in matrix:
    print(''.join(row))

print(f'won: {p_row} {p_col}') if player_win else print(f'dead: {p_row} {p_col}')



# def fill_the_field_and_find_player(num_of_rows, cols, matrix, player_row, player_col):
#     for r in range(num_of_rows):
#         row = list(input())
#         matrix.append(row)
#         if "P" in row:
#             player_row = r
#             player_col = row.index('P')
#     return matrix, player_row, player_col
# 
# 
# def is_valid_index(value, max_value):
#     return 0 <= value < max_value
# 
# 
# def next_move(dir_, row, col, rows, cols):
#     directions = {"U": (-1, 0),
#                   "D": (1, 0),
#                   "R": (0, 1),
#                   "L": (0, -1)
#                   }
# 
#     d_row, d_col = directions[dir_][0], directions[dir_][1]
#     new_row, new_col = row + d_row, col + d_col
#     if is_valid_index(new_row, rows) and is_valid_index(new_col, cols):
#         return new_row, new_col
#     return None, None
# 
# 
# def out_of_boundaries(player_won, player_dead, pl_row, pl_col, matrix):
#     if not player_dead:
#         player_won = True
#         matrix[pl_row][pl_col] = "."
#     return matrix, player_won
# 
# 
# def bunny_spread(matrix, rows, cols, player_dead):
#     bunny_coordinates = []
#     for row in range(rows):
#         for col in range(cols):
#             if matrix[row][col] == "B":
#                 bunny_coordinates.append([row, col])
# 
#     def spread_bunny(b_row, b_col, d_row, d_col):
#         nonlocal player_dead
#         new_row, new_col = b_row + d_row, b_col + d_col
#         if is_valid_index(new_row, rows) and is_valid_index(new_col, cols):
#             if matrix[new_row][new_col] == "P":
#                 player_dead = True
#             matrix[new_row][new_col] = "B"
# 
#     all_directions = {
#         'up': (-1, 0),
#         'down': (1, 0),
#         'left': (0, -1),
#         'right': (0, 1)
#     }
# 
#     for b_row, b_col in bunny_coordinates:
#         for direction in all_directions.values():
#             spread_bunny(b_row, b_col, *direction)
# 
#     return matrix, player_dead
# 
# 
# def main():
#     rows, columns = [int(x) for x in input().split()]
#     field = []
#     player_row, player_col = 0, 0
#     player_is_dead = False
#     player_won = False
#     field, player_row, player_col = \
#         fill_the_field_and_find_player(rows, columns, field, player_row, player_col)
#     directions = list(input())
# 
#     for direction in directions:
#         next_row, next_col = next_move(direction, player_row, player_col, rows, columns)
#         if next_row is None or next_col is None:
#             field, player_won = out_of_boundaries(player_won, player_is_dead, player_row, player_col, field)
# 
#         else:
#             if field[next_row][next_col] == "B":
#                 player_is_dead = True
#                 player_row, player_col = next_row, next_col
# 
#             else:
#                 field[player_row][player_col] = "."
#                 player_row, player_col = next_row, next_col
#                 field[player_row][player_col] = "P"
# 
#         field, player_is_dead = bunny_spread(field, rows, columns, player_is_dead)
#         if player_won or player_is_dead:
#             break
# 
#     [print(''.join(element)) for element in field]
#     print(f"dead: {player_row} {player_col}") if player_is_dead else print(f"won: {player_row} {player_col}")
# 
# 
# if __name__ == '__main__':
#     main()




# def fill_the_field_and_find_player(num_of_rows, cols, matrix, player_row, player_col):
#     for r in range(num_of_rows):
#         row = list(input())
#         matrix.append(row)
#         if "P" in row:
#             player_row = r
#             player_col = row.index('P')
#     return matrix, player_row, player_col


# def is_valid_index(value, max_value):
#     return 0 <= value < max_value


# def next_move(current_direction, current_row, current_col, num_of_rows, cols):
#     if current_direction == "U" and is_valid_index(current_row - 1, num_of_rows):
#         return current_row - 1, current_col
#     if current_direction == "D" and is_valid_index(current_row + 1, num_of_rows):
#         return current_row + 1, current_col
#     if current_direction == "L" and is_valid_index(current_col - 1, cols):
#         return current_row, current_col - 1
#     if current_direction == "R" and is_valid_index(current_col + 1, cols):
#         return current_row, current_col + 1
#     return None, None


# def bunny_spread(matrix, num_of_rows, cols, player_dead):
#     bunny_coordinates = []
#     for row in range(num_of_rows):
#         for col in range(cols):
#             if matrix[row][col] == "B":
#                 bunny_coordinates.append([row, col])

#     for coordinates in bunny_coordinates:
#         b_row, b_col = coordinates[0], coordinates[1]
#         if is_valid_index(b_row - 1, num_of_rows):  # up
#             if matrix[b_row - 1][b_col] == "P":
#                 player_dead = True
#             matrix[b_row - 1][b_col] = "B"
#         if is_valid_index(b_row + 1, num_of_rows):
#             if matrix[b_row + 1][b_col] == "P":
#                 player_dead = True
#             matrix[b_row + 1][b_col] = "B"  # down
#         if is_valid_index(b_col - 1, cols):
#             if matrix[b_row][b_col - 1] == "P":
#                 player_dead = True
#             matrix[b_row][b_col - 1] = "B"  # left
#         if is_valid_index(b_col + 1, cols):
#             if matrix[b_row][b_col + 1] == "P":
#                 player_dead = True
#             matrix[b_row][b_col + 1] = "B"  # right

#     return matrix, player_dead


# def main():
#     rows, columns = [int(x) for x in input().split()]
#     field = []
#     player_row, player_col = 0, 0
#     player_is_dead = False
#     player_won = False
#     field, player_row, player_col = \
#         fill_the_field_and_find_player(rows, columns, field, player_row, player_col)
#     directions = list(input())

#     for direction in directions:
#         next_row, next_col = next_move(direction, player_row, player_col, rows, columns)
#         if next_row is None or next_col is None:
#             if not player_is_dead:
#                 player_won = True
#                 field[player_row][player_col] = "."
#         else:
#             if field[next_row][next_col] == "B":
#                 player_is_dead = True
#                 player_row, player_col = next_row, next_col
#             else:
#                 field[player_row][player_col] = "."
#                 player_row, player_col = next_row, next_col
#                 field[player_row][player_col] = "P"

#         field, player_is_dead = bunny_spread(field, rows, columns, player_is_dead)
#         if player_won or player_is_dead:
#             break

#     [print(''.join(element)) for element in field]
#     print(f"dead: {player_row} {player_col}") if player_is_dead else print(f"won: {player_row} {player_col}")


# if __name__ == '__main__':
#     main()
