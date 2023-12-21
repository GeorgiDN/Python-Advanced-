from string import punctuation

with open("text1..txt", 'r') as file_text:
    text = file_text.read().split("\n")

with open("output_2_zad.txt", 'w') as output_file:
    for i in range(len(text)):
        line = text[i]

        letters_num = len([x for x in line if x.isalpha()])
        pun_marks = len([x for x in line if x in punctuation])

        output_file.write(f"Line {i+1}: {line} ({letters_num})({pun_marks})\n")

