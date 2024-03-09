from collections import deque

numbers = [x for x in input().split("|")]
flatten_list = deque()

for sublist in numbers:
    elements = sublist.split()
    cleaned_elements = [x.strip() for x in elements]
    flatten_list.appendleft(cleaned_elements)

print(*[item for row in flatten_list for item in row])


# input_text = input().split("|")
# joined_lists = []

# for sublist in input_text:
#     elements = sublist.split()
#     cleaned_elements = [x.strip() for x in elements]
#     joined_lists.append(cleaned_elements)

# flattened_list = []

# while joined_lists:
#     current_list = joined_lists.pop()
#     flattened_list.extend(current_list)
# print(*flattened_list)



# joined_lists = [[x.strip() for x in sublist.split()] for sublist in input().split("|")]
# flattened_list = []
# while joined_lists:
#     current_list = joined_lists.pop()
#     flattened_list.extend(current_list)
# print(*flattened_list)

