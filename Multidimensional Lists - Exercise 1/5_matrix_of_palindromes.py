rows, cols = [int(x) for x in input().split()]
matrix_of_palindromes = []

for row in range(rows):
    curr_row = []
    for col in range(cols):
        curr_string = chr(97 + row) + chr(97 + row + col) + chr(97 + row)
        if curr_string == curr_string[::-1]:
            curr_row.append(curr_string)
    matrix_of_palindromes.append(curr_row)

for palindrome in matrix_of_palindromes:
    print(' '.join(palindrome))



# rows, columns = [int(x) for x in input().split()]
# matrix = []

# for row in range(rows):
#     current_row = []
#     for col in range(columns):
#         first_letter = chr(97 + row)
#         second_letter = chr(97 + row + col)
#         third_letter = first_letter
#         palindrome = first_letter + second_letter + third_letter
#         current_row.append(palindrome)
#     matrix.append(current_row)

# [print(" ".join(el)) for el in matrix]
