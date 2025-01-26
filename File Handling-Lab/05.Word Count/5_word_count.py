import re

words_text_file = 'words.txt'
input_text_file = 'input.txt'
output_text_file = 'output.txt'

words_count = {}

with open(words_text_file, 'r') as words_file:
    for line in words_file:
        words = line.split()
        for word in words:
            if word not in words_count:
                words_count[word] = 0

pattern = r'[A-Za-z\']+'
with open(input_text_file, 'r') as input_file:
    for row in input_file:
        words = row.split()
        for word in words:
            found_words = re.findall(pattern, word)
            for found_word in found_words:
                if found_word.lower() in words_count:
                    words_count[found_word.lower()] += 1

sorted_words_count = dict(sorted(words_count.items(), key=lambda x: x[1], reverse=True))

with open(output_text_file, 'w') as output_file:
    for word, count in sorted_words_count.items():
        output_file.write(f"{word} - {count}\n")



###################################################################################################
# import re

# file_name = "words.txt"
# input_text_file = 'input.txt'
# output_text_file = "output.txt"

# words_count = {}
# with open(file_name, "r") as file:
#     for row in file:
#         words = row.split()
#         for word in words:
#             words_count[word] = 0
# file.close()

# pattern = r"[A-Za-z\']+"
# with open(input_text_file, "r") as input_file:
#     for curr_row in input_file:
#         curr_words = curr_row.split()
#         for curr_word in curr_words:
#             found_words = re.findall(pattern, curr_word)
#             for found_word in found_words:
#                 if found_word.lower() in words_count:
#                     words_count[found_word.lower()] += 1
# input_file.close()

# with open(output_text_file, "w") as output_file:
#     sorted_items = sorted(words_count.items(), key=lambda x: -x[1])
#     for idx, (key, value) in enumerate(sorted_items):
#         output_file.write(f"{key} - {value}")
#         if idx < len(sorted_items) - 1:  # Check if it's not the last item
#             output_file.write("\n")

# output_file.close()
