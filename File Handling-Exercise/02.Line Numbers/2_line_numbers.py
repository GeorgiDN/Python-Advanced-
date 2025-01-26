from string import punctuation

text_file = 'text.txt'
output_text_file = 'output.txt'
chars_data = {}

with open(text_file, "r") as input_file:
    text = input_file.readlines()

for row in range(len(text)):
    punctuation_marks = 0
    letters_number = 0
    line = text[row].strip()
    for char in line:
        if char in punctuation:
            punctuation_marks += 1
        elif char.isalpha():
            letters_number += 1
    chars_data[f'Line {row + 1}'] = {
        'content': line,
        'letters': letters_number,
        'punctuation': punctuation_marks
    }

with open(output_text_file, "w") as output_file:
    total_lines = len(chars_data)
    for index, (key, data) in enumerate(chars_data.items(), 1):
        result = f'{key}: {data["content"]} ({data["letters"]})({data["punctuation"]})'
        if index < total_lines:
            result += '\n'
        output_file.write(result)




###################################################################################################################
# from string import punctuation

# text_file = 'text.txt'
# output_text_file = 'output.txt'


# def write_output_file(current_row, output_file, letters_num, punctuation_marks, idx, lines_num):
#     with open(output_file, 'a') as file:
#         file.write(f"Line {idx+1}: {' '.join(current_row)} ({letters_num})({punctuation_marks})")
#         if idx != lines_num - 1:
#             file.write('\n')


# def process_text_file(input_file, output_file):
#     with open(input_file, 'r') as file:
#         total_lines = sum(1 for line in file)
#         file.seek(0)
#         for index, line in enumerate(file):
#             letters_number = 0
#             punctuation_marks_number = 0
#             row = line.split()
#             for word in row:
#                 for char in word:
#                     if char in punctuation:
#                         punctuation_marks_number += 1
#                     elif char.isalpha():
#                         letters_number += 1

#             write_output_file(row, output_file, letters_number, punctuation_marks_number, index, total_lines)


# process_text_file(text_file, output_text_file)
