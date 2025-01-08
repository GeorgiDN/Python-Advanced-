valid_parenthesis = {'(': ')', '[': ']', '{': '}'}
parenthesis_input = input()
is_balanced = True
my_stack = []

if len(parenthesis_input) % 2 != 0:
    is_balanced = False
else:
    for bracket in parenthesis_input:
        if bracket in '({[':
            my_stack.append(bracket)
        else:
            if not my_stack or bracket != valid_parenthesis[my_stack.pop()]:
                is_balanced = False
                break

print('YES') if is_balanced else print('NO')


# parenthesis = input()

# my_stack = []
# is_balanced = True
# valid_parentheses = {"(": ")", "{": "}", "[": "]"}


# for bracket in parenthesis:
#     if bracket in "({[":
#         my_stack.append(bracket)
#     else:
#         if not my_stack or bracket != valid_parentheses[my_stack.pop()]:
#             is_balanced = False
#             break

# print("YES") if is_balanced and len(my_stack) % 2 == 0 else print("NO")
