def divide_numbers(n1, n2):
    return n1 / n2


def multiply_numbers(n1, n2):
    return n1 * n2


def subtract_numbers(n1, n2):
    return n1 * n2


def add_numbers(n1, n2):
    return n1 + n2


def exponent_numbers(n1, n2):
    return n1 ** n2


def calculate_numbers(num1, operator, num2):
    result = None
    if operator == "/":
        result = divide_numbers(num1, num2)
    elif operator == "*":
        result = multiply_numbers(num1, num2)
    elif operator == "-":
        result = subtract_numbers(num1, num2)
    elif operator == "+":
        result = add_numbers(num1, num2)
    elif operator == "^":
        result = exponent_numbers(num1, num2)

    return f"{result:.2f}"


