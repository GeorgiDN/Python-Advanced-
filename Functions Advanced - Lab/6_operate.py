def operate(operator, *args):
    result = args[0]
    if operator in ["+", "-"]:
        for num in args[1:]:
            result = eval(f"{result}{operator}{num}")
    else:
        if 0 in args:
            result = 0
        else:
            for num in args[1:]:
                result = eval(f"{result}{operator}{num}")
    return result

# print(operate("*", 3, 4))
print(operate("+", 1, 2, 3))


# from functools import reduce


# def operate(operator, *args):
#     if operator == '+':
#         return reduce(lambda x, y: x + y, args)
#     elif operator == '-':
#         return reduce(lambda x, y: x - y, args)
#     elif operator == '*':
#         return reduce(lambda x, y: x * y, args)
#     elif operator == '/':
#         return reduce(lambda x, y: x / y, args)


# print(operate("+", 1, 2, 3))
