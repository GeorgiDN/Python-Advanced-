from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = deque(input())
matrix = []

for row in range(rows):
    current_row = ""
    for col in range(columns):
        current_symbol = snake.popleft()
        current_row += current_symbol
        snake.append(current_symbol)
    if row % 2 != 0:
        current_row = current_row[::-1]
    matrix.append(current_row)

[print(element) for element in matrix]
