def func_executor(*args):
    result = ""

    for func in args:
        func_name, func_args = func
        result += f"{func_name.__name__} - {func_name(*func_args)}" + "\n"

    return result


def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
