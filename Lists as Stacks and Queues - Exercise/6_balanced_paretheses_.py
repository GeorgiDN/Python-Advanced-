parenthesis = input()

my_stack = []
is_balanced = True
valid_parentheses = {"(": ")", "{": "}", "[": "]"}


for bracket in parenthesis:
    if bracket in "({[":
        my_stack.append(bracket)
    else:
        if not my_stack or bracket != valid_parentheses[my_stack.pop()]:
            is_balanced = False
            break

print("YES") if is_balanced and len(my_stack) % 2 == 0 else print("NO")
