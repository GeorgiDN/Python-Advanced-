parenthesis = input()

my_stack = []
is_balanced = True
mapping = {"(": ")", "{": "}", "[": "]"}

for ch in parenthesis:
    if ch in "({[":
        my_stack.append(ch)
    else:
        if not my_stack or ch != mapping[my_stack.pop()]:
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")
