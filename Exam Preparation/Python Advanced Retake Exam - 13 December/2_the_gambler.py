def is_valid(value, max_value):
    return 0 <= value <= max_value


def next_move(command, current_row, current_col):
    if command == "up" and is_valid(current_row - 1, size):
        return current_row - 1, current_col
    if command == "down" and is_valid(current_row + 1, size):
        return current_row + 1, current_col
    if command == "left" and is_valid(current_col - 1, size):
        return current_row, current_col - 1
    if command == "right" and is_valid(current_col + 1, size):
        return current_row, current_col + 1
    return None, None


size = int(input())
field = []
gambler_row, gambler_col = None, None
amount = 100
stop_condition = False

for r in range(size):
    row = list(input())
    field.append(row)
    if "G" in row:
        gambler_row = r
        gambler_col = row.index("G")
        start_row = gambler_row
        start_col = gambler_col

while True:
    line = input()
    if line == "end":
        break
    next_row, next_col = next_move(line, gambler_row, gambler_col)
    field[gambler_row][gambler_col] = '-'
    if next_row is None or next_col is None:
        print("Game over! You lost everything!")
        stop_condition = True
        break
    if field[next_row][next_col] == "W":
        amount += 100
    if field[next_row][next_col] == "P":
        amount -= 200
        if amount <= 0:
            print("Game over! You lost everything!")
            stop_condition = True
            break
    if field[next_row][next_col] == "J":
        amount += 100000
        gambler_row, gambler_col = next_row, next_col
        field[gambler_row][gambler_col] = "G"
        print("You win the Jackpot!")
        break
    gambler_row, gambler_col = next_row, next_col
    field[gambler_row][gambler_col] = "G"

if not stop_condition:
    print(f"End of the game. Total amount: {amount}$")
    for row_ in field:
        print(''.join(row_))
