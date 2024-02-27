parenthesis = input()

my_stack = []
is_balanced = True
valid_parentheses = {"(": ")", "{": "}", "[": "]"}

for bracket in parenthesis:
    if bracket in "([{":
        my_stack.append(bracket)
    else:
        if not my_stack or bracket != valid_parentheses[my_stack.pop()]:
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")
