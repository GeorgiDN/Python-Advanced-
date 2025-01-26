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
