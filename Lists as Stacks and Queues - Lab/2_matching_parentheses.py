expression = input()

stack = []
result = []

for i, char in enumerate(expression):
    if char == "(":
        stack.append(i)
    elif char == ")":
        start = stack.pop()
        result.append(expression[start:i+1])

print('\n'.join(result))


# data = input()
# indexes = []

# for i in range(len(data)):
#     ch = data[i]

#     if ch == '(':
#         indexes.append(i)
#     elif ch == ')':
#         l = indexes.pop()
#         print(data[l:i + 1])
        
