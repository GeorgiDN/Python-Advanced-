rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

primary_diagonal_numbers = ([matrix[i][i] for i in range(rows)])
primary_diagonal_sum = sum(primary_diagonal_numbers)

secondary_diagonal_numbers = ([matrix[i][rows - 1 - i] for i in range(rows)])
secondary_diagonal_sum = sum(secondary_diagonal_numbers)

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal_numbers))}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal_numbers))}. Sum: {secondary_diagonal_sum}")




# rows = int(input())
# matrix = []

# primary_diagonal_numbers = []
# secondary_diagonal_numbers = []

# for _ in range(rows):
#     matrix.append([int(x) for x in input().split(", ")])

# for i in range(rows):
#     primary_diagonal_numbers.append(matrix[i][i])
#     secondary_diagonal_numbers.append(matrix[i][(rows - 1) - i])


# print(f"Primary diagonal: {', '.join(map(str, primary_diagonal_numbers))}. Sum: {sum(primary_diagonal_numbers)}")
# print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal_numbers))}. Sum: {sum(secondary_diagonal_numbers)}")
