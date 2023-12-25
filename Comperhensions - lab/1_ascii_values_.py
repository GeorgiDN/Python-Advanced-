def result():
    values = {char: ord(char) for char in input().split(", ")}
    return values


print(result())
