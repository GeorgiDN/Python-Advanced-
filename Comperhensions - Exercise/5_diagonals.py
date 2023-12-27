rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
first_diagonal = [matrix[row][row] for row in range(rows)]
second_diagonal = [matrix[row][rows-row-1] for row in range(rows)]

print(f"First diagonal: {', '.join(map(str, first_diagonal))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}")
