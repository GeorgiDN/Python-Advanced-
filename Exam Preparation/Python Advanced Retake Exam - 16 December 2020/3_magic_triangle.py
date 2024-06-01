def get_magic_triangle(rows):
    triangle = [[1], [1, 1]]

    for row in range(2, rows):
        current_row = []
        current_row.append(1)
        for col in range(row-1):
            current_row.append(triangle[-1][col] + triangle[-1][col+1])
        current_row.append(1)
        triangle.append(current_row)
    return triangle


print(get_magic_triangle(5))
