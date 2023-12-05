
rows, columns = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    current_row = []
    for col in range(columns):
        first_letter = chr(97 + row)
        second_letter = chr(97 + row + col)
        third_letter = first_letter
        palindrome = first_letter + second_letter + third_letter
        current_row.append(palindrome)
    matrix.append(current_row)

[print(" ".join(el)) for el in matrix]
