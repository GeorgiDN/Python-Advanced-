from collections import deque

text_file = 'text.txt'
symbols_for_replace = ["-", ",", ".", "!", "?"]

with open(text_file, 'r') as file:
    for idx, line in enumerate(file):
        result = deque()
        if idx == 0 or idx % 2 == 0:
            words = line.split()
            for word in words:
                for letter in word:
                    if letter in symbols_for_replace:
                        word = word.replace(letter, "@")
                result.appendleft(word)
            print(' '.join(result))



##############################################################################################################################################
# text_file = "text.txt"

# result = []
# symbols_for_replace = ["-", ",", ".", "!", "?"]

# with open(text_file, "r") as file:
#     total_lines = sum(1 for line in file)  # Get the total number of lines
#     file.seek(0)  # Reset file pointer to the beginning
#     for idx, line in enumerate(file):
#         if idx % 2 == 0:
#             words = line.strip().split()
#             modified_line = []
#             for word in words:
#                 # Replace symbols in the word
#                 for symbol in symbols_for_replace:
#                     word = word.replace(symbol, "@")
#                 modified_line.append(word)
#             modified_line.reverse()  # Reverse the order of words
#             result.append(" ".join(modified_line))
#             if idx != total_lines - 1:  # Check if it's not the last line
#                 result.append("\n")

# print("".join(result))
