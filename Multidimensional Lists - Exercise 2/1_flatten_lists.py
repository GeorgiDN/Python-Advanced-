input_text = input().split("|")
joined_lists = []

for sublist in input_text:
    elements = sublist.split()
    cleaned_elements = [x.strip() for x in elements]
    joined_lists.append(cleaned_elements)

flattened_list = []

while joined_lists:
    current_list = joined_lists.pop()
    flattened_list.extend(current_list)
print(*flattened_list)
