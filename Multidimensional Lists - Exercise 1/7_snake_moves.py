rows, cols = [int(x) for x in input().split()]
text = input()

result = []
index = 0

for row in range(rows):
    curr_string = ''
    for col in range(cols):
        curr_string += text[index % len(text)]
        index += 1
    if row > 0 and row % 2 != 0:
        curr_string = curr_string[::-1]
    result.append(curr_string)

print('\n'.join(result))



# from collections import deque

# rows, columns = [int(x) for x in input().split()]
# snake = deque(input())
# matrix = []

# for row in range(rows):
#     current_row = ""
#     for col in range(columns):
#         current_symbol = snake.popleft()
#         current_row += current_symbol
#         snake.append(current_symbol)
#     if row % 2 != 0:
#         current_row = current_row[::-1]
#     matrix.append(current_row)

# [print(element) for element in matrix]
