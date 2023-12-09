size = int(input())
wonderland = []
alice_row, alice_col = 0, 0

for row in range(size):
    current_row = [x for x in input().split()]
    wonderland.append(current_row)
    if "A" in current_row:
        alice_row, alice_col = row, current_row.index("A")

alice_left_wonderland = False
alice_got_to_the_party = False
tea_bags = 0

while True:
    wonderland[alice_row][alice_col] = "*"
    if alice_left_wonderland or alice_got_to_the_party:
        break
    direction = input()
    if direction == "up":
        next_row, next_col = alice_row - 1, alice_col
    elif direction == "down":
        next_row, next_col = alice_row + 1, alice_col
    elif direction == "left":
        next_row, next_col = alice_row, alice_col - 1
    else:
        next_row, next_col = alice_row, alice_col + 1

    if next_row in range(size) and next_col in range(size):
        symbol = wonderland[next_row][next_col]
        if symbol == "R":
            wonderland[next_row][next_col] = "*"
            alice_left_wonderland = True
            break
        elif symbol.isalnum():
            tea_bags += int(symbol)
        alice_row, alice_col = next_row, next_col
        if tea_bags >= 10:
            alice_got_to_the_party = True
    else:
        alice_left_wonderland = True

if alice_got_to_the_party:
    print("She did it! She went to the party.")
if alice_left_wonderland:
    print("Alice didn't make it to the tea party.")
[print(" ".join(element)) for element in wonderland]

