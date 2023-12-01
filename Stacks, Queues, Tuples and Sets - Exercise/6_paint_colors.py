from collections import deque
strings = deque(input().split())
primary_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
matched_colors = []
while strings:
    first_substring = strings.popleft()
    if strings:
        last_substring = strings.pop()
    else:
        last_substring = ""
    color = first_substring + last_substring
    if color in primary_colors or color in secondary_colors:
        matched_colors.append(color)
        continue
    color = last_substring + first_substring
    if color in primary_colors or color in secondary_colors:
        matched_colors.append(color)
        continue
    first_substring = first_substring[:-1]
    last_substring = last_substring[:-1]
    if first_substring:
        strings.insert(len(strings) // 2, first_substring)
    if last_substring:
        strings.insert(len(strings) // 2, last_substring)

result = []
for i in range(len(matched_colors)):
    current_color = matched_colors[i]
    if current_color in primary_colors:
        result.append(current_color)
        continue
    if current_color == "orange" and "yellow" in matched_colors and "red" in matched_colors:
        result.append(current_color)
    elif current_color == "purple" and "red" in matched_colors and "blue" in matched_colors:
        result.append(current_color)
    elif current_color == "green" and "yellow" in matched_colors and "blue" in matched_colors:
        result.append(current_color)

print(result)
