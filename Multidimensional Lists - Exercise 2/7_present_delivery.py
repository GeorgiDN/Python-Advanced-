presents = int(input())
size = int(input())
neighbourhood = []
santa_row, santa_col = 0, 0
nice_kids = 0
count_nice_kids = 0

for row in range(size):
    current_row = input().split()
    neighbourhood.append(current_row)
    for symbol in current_row:
        if symbol == "S":
            santa_row, santa_col = row, current_row.index(symbol)
        elif symbol == "V":
            nice_kids += 1

new_row, new_col = 0, 0

while True:
    command = input()
    if command == "Christmas morning" or presents == 0:
        break
    if command == "up":
        new_row, new_col = santa_row - 1, santa_col
    elif command == "down":
        new_row, new_col = santa_row + 1, santa_col
    elif command == "left":
        new_row, new_col = santa_row, santa_col - 1
    elif command == "right":
        new_row, new_col = santa_row, santa_col + 1
    if new_row in range(size) and new_col in range(size):
        house = neighbourhood[new_row][new_col]
        if house == "V":
            nice_kids -= 1
            presents -= 1
            count_nice_kids += 1
        elif house == "C":
            surrounding_houses = [
                [new_row - 1, new_col],
                [new_row + 1, new_col],
                [new_row, new_col - 1],
                [new_row, new_col + 1]
            ]
            for h in surrounding_houses:
                if presents == 0:
                    break
                h_row, h_col = h
                if neighbourhood[h_row][h_col] == "X":
                    presents -= 1
                elif neighbourhood[h_row][h_col] == "V":
                    presents -= 1
                    nice_kids -= 1
                    count_nice_kids += 1
                neighbourhood[h_row][h_col] = "-"
        neighbourhood[new_row][new_col] = "S"
        neighbourhood[santa_row][santa_col] = "-"
        santa_row, santa_col = new_row, new_col
        if presents == 0:
            break

if nice_kids > 0 and presents == 0:
    print("Santa ran out of presents!")
[print(" ".join(element)) for element in neighbourhood]
if nice_kids == 0:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
